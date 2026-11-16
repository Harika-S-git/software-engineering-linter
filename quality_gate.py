"""CLI for checking and applying consistent Python formatting."""

import argparse
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_PATHS = ("calculator.py", "quality_gate.py", "scripts", "tests")


def run_command(arguments: list[str], cwd: Path = PROJECT_ROOT) -> int:
    """Run a vetted tool command and return its exit status."""
    command = [sys.executable, "-m", *arguments]
    print("$ " + " ".join(command), flush=True)
    try:
        result = subprocess.run(command, cwd=cwd, check=False)
    except OSError as error:
        print(f"Unable to run command: {error}", file=sys.stderr)
        return 2
    return result.returncode


def check() -> int:
    """Run Flake8, Black check, and unit tests in order."""
    commands = (
        ["flake8", *SOURCE_PATHS],
        ["black", "--check", *SOURCE_PATHS],
        ["pytest", "-q", "tests"],
    )
    for args in commands:
        result = run_command(args)
        if result != 0:
            print(f"Quality gate FAILED (exit code {result})")
            return result
    print("Quality gate PASSED")
    return 0


def format_code() -> int:
    """Apply Black to the project's Python sources."""
    return run_command(["black", *SOURCE_PATHS])


def main(argv: list[str] | None = None) -> int:
    """Parse the command and return an automation-friendly status."""
    parser = argparse.ArgumentParser(description="Python quality gate")
    parser.add_argument("action", choices=("check", "format"))
    arguments = parser.parse_args(argv)
    return check() if arguments.action == "check" else format_code()


if __name__ == "__main__":
    sys.exit(main())
