---
subject_scopes:
  - framework-engine-software
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Require Python or an accepted native-boundary exception

Given every hand-authored Framework Engine software carrier in the target set, classify its implementation language and native-interface dependency. Verify that each carrier is Python or has one explicit Operator-accepted exception that names the required native boundary or measured benefit and its added operating cost.

The case fails on an unexplained non-Python carrier or a blanket exception without a bounded target.

Candidate alignment: CA-E-001, CA-E-002, CA-M-005, CA-M-006, CA-D-001, CA-R-861.

## Sources

- [Python Packaging User Guide: pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Python documentation: platform](https://docs.python.org/3/library/platform.html)
