"""Focused tests for argument parsing, tool errors and stop-on-fail logic."""

from unittest.mock import patch

import pytest

import quality_gate


def test_check_passes_when_all_three_commands_pass():
    with patch.object(quality_gate, "run_command", return_value=0) as run:
        assert quality_gate.check() == 0
        assert run.call_count == 3


def test_check_stops_at_first_failure():
    with patch.object(quality_gate, "run_command", side_effect=[1, 0, 0]) as run:
        assert quality_gate.check() == 1
        assert run.call_count == 1


def test_check_returns_test_failure():
    with patch.object(quality_gate, "run_command", side_effect=[0, 0, 1]):
        assert quality_gate.check() == 1


def test_format_runs_black():
    with patch.object(quality_gate, "run_command", return_value=0) as run:
        assert quality_gate.format_code() == 0
        assert run.call_args.args[0][0] == "black"


def test_main_rejects_unknown_action():
    with pytest.raises(SystemExit) as error:
        quality_gate.main(["something-else"])
    assert error.value.code == 2


def test_main_check_dispatches():
    with patch.object(quality_gate, "check", return_value=0) as check:
        assert quality_gate.main(["check"]) == 0
        check.assert_called_once_with()
