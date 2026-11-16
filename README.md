# Custom Code Linter and Formatter Workflow

Software Engineering mini-project using **Python, Flake8, Black, Pytest and GitHub Actions**.

## Setup (Windows PowerShell)
```powershell
git clone https://github.com/Harika-S-git/software-engineering-linter.git
cd software-engineering-linter
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python calculator.py
python quality_gate.py check
python quality_gate.py format
python scripts/reproduce_failure.py
```

On Linux/macOS use `python3.12 -m venv .venv` and `source .venv/bin/activate`.

## Pipeline
Developer PR -> GitHub Actions -> Flake8 style -> Black format check -> Pytest -> red/green status -> human review/merge. The formatter is run locally only when explicitly requested. The workflow has read-only repository permissions.

## Local output
Calculator displays 10+5, 10-5 and 10*5. The isolated demo creates malformed code in a temporary folder, confirms a lint failure, runs Black, then confirms the corrected code passes. No tracked application files are intentionally left broken.

## Existing authentic historical evidence (9 Sep 2026)
- Failed: https://github.com/Harika-S-git/software-engineering-linter/actions/runs/34309181142
- Passed: https://github.com/Harika-S-git/software-engineering-linter/actions/runs/34310540851

These prove the original Flake8 stage and are not proof that the expanded workflow has already passed. Check the latest PR run for the new pipeline.

## Assignment deliverables
`docs/` contains reconstructed SRS, SAD, Test Plan, story-point backlog, two sprint records, requirement mapping, deviations, video scripts and release freeze procedure. Original SRS/SAD/Test Plan were not provided and must be reconciled. Actual GitHub Project creation, teammate-authored PR approval, 1- and 2-minute screen recordings and freeze tag require authentic GitHub/team actions.

See `docs/SUBMISSION_CHECKLIST.md`.
