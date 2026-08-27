---
subject_scopes:
  - framework-engine-software
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Select software Evaluation techniques by failure mode

Select the smallest complementary Evaluation set that can expose the target software component's declared failure modes. Use examples for known behavior, property-based or stateful generation for broad input and transition spaces, mutation testing for weak assertions, contract checks for machine boundaries, and reviewed golden baselines for large deterministic outputs.

Keep fast syntax, format, lint, type, and focused behavioral checks in the changed-code gate. Run expensive mutation, fuzz, broad compatibility, and snapshot-review work outside synchronous Git or host Hooks unless a measured bound proves it acceptably fast.

Record the target, configuration, source frontier, seed or generated case when applicable, tool versions, result, and a replay command. Passing one technique never substitutes for an uncovered failure mode.

Candidate alignment: CA-E-001, CA-E-002, CA-M-005, CA-O-003, CA-R-861.

## Sources

- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
