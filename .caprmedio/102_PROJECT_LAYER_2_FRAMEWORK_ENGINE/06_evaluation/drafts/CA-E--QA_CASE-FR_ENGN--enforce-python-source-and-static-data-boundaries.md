---
subject_scopes:
  - framework-engine-python
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Enforce Python source and static-data boundaries

Given every changed hand-authored Python carrier in Tools, App services, and MCP components, measure physical file lines, logical executable-unit lines, and static mapping size. Verify files do not exceed 200 lines, executable units target 25 lines and do not exceed 40 without an accepted exception, declarative classes keep one responsibility, and mappings above 20 entries or 25 lines are carried outside Python.

Verify external carriers use TOML by default, JSON for schema or interchange needs, and YAML only for a declared distinct feature. Report each violation separately; generated Runtime and Delivery outputs are outside this case.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-M-005, CA-D-002, CA-R-861.

## Sources

- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python documentation: tomllib](https://docs.python.org/3/library/tomllib.html)
- [Python documentation: json](https://docs.python.org/3/library/json.html)
