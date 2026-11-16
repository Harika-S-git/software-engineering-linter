# Verified local results (16 Nov 2026)

- `python -m pytest -q tests`: **15 passed** (0.08s)
- `python -m compileall -q calculator.py quality_gate.py scripts tests`: successful
- `python calculator.py`: 10 + 5 = 15; 10 - 5 = 5; 10 * 5 = 50
- `flake8` / `black`: **not executed locally**, because offline environment cannot install missing packages.

GitHub hosted runner should install dependencies from pinned requirements. Check the actual new PR Actions logs before declaring new CI validated.
