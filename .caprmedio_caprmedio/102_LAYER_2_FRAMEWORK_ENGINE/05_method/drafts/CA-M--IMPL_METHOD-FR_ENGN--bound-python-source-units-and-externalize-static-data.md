---
subject_scopes:
  - framework-engine-python
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Bound Python source units and externalize static data

Keep every hand-authored Python file distributed with FRAMEWORK_ENGINE software at or below 200 physical lines. Target at most 25 logical lines for each function, method, coroutine, closure, or other independently executable decision unit; permit 26–40 only when the unit still performs one coherent job and splitting it would reduce clarity. Reject an executable unit above 40 lines unless the Operator accepts a documented exception.

Judge declarative data classes and schemas by one responsibility rather than the executable-line limit, while retaining the 200-line file limit. Treat the thresholds as navigation constraints, not proof of quality; also evaluate complexity, cohesion, typing, and behavior.

Move a static mapping larger than 20 entries or 25 source lines out of Python. Use TOML by default, JSON for schemas or machine interchange, and YAML only when its distinct features are required. Generated Runtime or Delivery outputs are outside this source-distribution rule.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002, CA-R-861.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python documentation: `tomllib`](https://docs.python.org/3/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3/library/json.html)
