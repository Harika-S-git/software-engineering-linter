"""Behavioural tests for the sample application."""

import pytest

from calculator import add, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 3, 5), (-2, 2, 0), (0.5, 0.25, 0.75)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(9, 4, 5), (-3, 3, -6), (0, 4, -4)],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [(2, 3, 6), (-4, 2, -8), (0, 100, 0)],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
