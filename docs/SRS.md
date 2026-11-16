# Software Requirements Specification (Reconstruction)

Date: 16 Nov 2026. The original previously submitted SRS was not available; reconcile before claiming agreement.

## Scope
Python application with automated PR code-quality checks, explicit local formatting, and unit tests. No GUI, database or automatic merging.

## Functional requirements
| ID | Requirement | Tests |
|---|---|---|
| FR-01 | Calculator supports add, subtract, multiply | TC-01 to 03 |
| FR-02 | PR triggers `.github/workflows/lint.yml` | TC-04 |
| FR-03 | Flake8 detects violations and fails nonzero | TC-05 |
| FR-04 | Authentic red-to-green failure correction | TC-06 |
| FR-05 | Black formats explicitly; check validates | TC-07,08 |
| FR-06 | Pytest unit tests execute in CI | TC-09,10 |
| FR-07 | Two real sprint videos, 60s and 120s | TC-11 |

## Nonfunctional requirements
- NFR-01: Reproducible setup using Python 3.12 and documented README.
- NFR-02: Pinned development dependencies, least-privilege CI, no secrets.
- NFR-03: Traceable backlog, sprint plans, deviations and release freeze.
- NFR-04: Nonzero exit codes cause CI failure.
- NFR-05: Exclude generated files and credentials from commits.

## Actors and interfaces
Developer pushes a branch; GitHub Actions executes checks; a real human reviewer approves/merges. Inputs: source, PR events, `check`/`format` CLI. Outputs: tool logs and status.
