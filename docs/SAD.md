# Software Architecture Document (Reconstruction)

Date: 16 Nov 2026. Original SAD was not provided.

## Event-driven CI architecture
```
Developer PR -> GitHub Repo -> GitHub Actions
                               | checkout + Python 3.12
                               | Flake8 -> Black --check -> Pytest
                               v
                          PASS/FAIL status -> Reviewer
Developer -> quality_gate.py format -> Black (local only)
```

## Components
- `calculator.py`: deterministic arithmetic demo.
- `quality_gate.py`: command dispatcher, first failure stops the gate.
- `scripts/reproduce_failure.py`: temp-file red/repair/green demo.
- `.github/workflows/lint.yml`: PR event automation.
- `tests/`: application and quality-gate unit tests.

## Decisions
Flake8 for lint, Black for formatting, Pytest for regression, pinned Python 3.12, read-only GitHub token. Separate approval from CI status. Workflow file placement corrected from legacy `.github/lint.yml`.
