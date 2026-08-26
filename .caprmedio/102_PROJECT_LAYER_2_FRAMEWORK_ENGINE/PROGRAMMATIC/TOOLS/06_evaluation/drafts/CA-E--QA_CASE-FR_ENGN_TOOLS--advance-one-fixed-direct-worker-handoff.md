---
subject_scopes:
  - tool-orchestration
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Advance one fixed direct worker handoff

Given a manager-produced two-step execution graph whose second step depends on the first, execute the first worker and its synchronous handoff. Verify that the exact typed result reaches only the declared second worker, the manager is not re-entered for a new decision, and neither worker can select or alter the downstream transition.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-M-005, CA-R-861.

## Sources

- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
