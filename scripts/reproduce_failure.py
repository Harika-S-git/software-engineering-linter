"""Reproduce a real lint failure and fix without modifying tracked files."""

import subprocess
import sys
import tempfile
from pathlib import Path


BAD_SAMPLE = "def add(a,b):\n return a+b\n"


def invoke(*args: str, path: Path) -> subprocess.CompletedProcess[str]:
    """Execute a Python module against a scratch test file."""
    command = [sys.executable, "-m", *args, str(path)]
    print("$ " + " ".join(command), flush=True)
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    print(result.stdout, end="")
    print(result.stderr, end="", file=sys.stderr)
    print(f"Exit code: {result.returncode}")
    return result


def main() -> int:
    """Demonstrate RED lint, automatic repair, and GREEN lint."""
    with tempfile.TemporaryDirectory(prefix="se-lint-demo-") as directory:
        sample = Path(directory) / "bad_example.py"
        sample.write_text(BAD_SAMPLE, encoding="utf-8")
        print("STAGE 1: intentionally bad sample")
        bad = invoke("flake8", path=sample)
        if bad.returncode == 0:
            print("Unexpected result: malformed sample passed lint")
            return 1
        print("STAGE 2: format sample using Black")
        formatted = invoke("black", path=sample)
        if formatted.returncode != 0:
            return formatted.returncode
        print("STAGE 3: verify repaired sample")
        good = invoke("flake8", path=sample)
        if good.returncode != 0:
            return good.returncode
        print("SUCCESS: proven failure -> repair -> passing check")
        return 0


if __name__ == "__main__":
    sys.exit(main())
