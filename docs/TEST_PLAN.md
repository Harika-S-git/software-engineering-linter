# Test Plan (Reconstruction)

Date: 16 Nov 2026. Original Test Plan unavailable; verify against original.

| Case | Action | Expected result |
|---|---|---|
| TC-01 | `add(2,3)` | 5 |
| TC-02 | `subtract(9,4)` | 5 |
| TC-03 | `multiply(-4,2)` | -8 |
| TC-04 | Raise PR | Workflow starts |
| TC-05 | Introduce bad style on test PR | Flake8 fails |
| TC-06 | Fix the same PR | Workflow passes |
| TC-07 | `python quality_gate.py format` | Black formats |
| TC-08 | `python quality_gate.py check` | Green on clean files; red on violations |
| TC-09 | `python -m pytest -q tests` | 15 tests pass |
| TC-10 | Mock failed tool | Gate stops immediately |
| TC-11 | Watch both videos | Actual 60s and 120s working-product demos |
| TC-12 | Fresh clone + dependency install | Setup works from README |

Historical authentic September Flake8 red/green evidence:
https://github.com/Harika-S-git/software-engineering-linter/actions/runs/34309181142
https://github.com/Harika-S-git/software-engineering-linter/actions/runs/34310540851

Local build had 15 passing Pytest checks and compiled successfully. Offline environment could not install Flake8/Black; do not claim those locally passed. Confirm actual workflow CI run for expanded version.
