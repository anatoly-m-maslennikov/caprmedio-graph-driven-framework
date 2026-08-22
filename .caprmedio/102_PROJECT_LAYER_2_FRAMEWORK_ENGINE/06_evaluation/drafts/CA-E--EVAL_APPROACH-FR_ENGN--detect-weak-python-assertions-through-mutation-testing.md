---
subject_scopes:
  - framework-engine-python
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Detect weak Python assertions through mutation testing

Run mutation testing against decision-dense managers, validators, parsers, and safety boundaries after their normal behavioral tests pass. Review every surviving relevant mutant as evidence of a missing assertion, an unreachable branch, equivalent behavior, or intentionally uncovered scope; do not reduce the result to a coverage percentage alone.

Start with changed or high-risk targets and preserve the exact source frontier, mutation-tool configuration, surviving mutant identity, affected test selection, and replay command. Keep mutation execution outside synchronous Hooks.

Candidate alignment: CA-E-001, CA-E-002, CA-M-005, CA-O-003, CA-R-861.

## Sources

- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [Mutmut configuration](https://mutmut.readthedocs.io/en/latest/#configuration)
