---
subject_scopes:
  - framework-engine-python
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Use Python branch coverage as navigation evidence

Collect branch coverage when control-flow alternatives matter, and use missing branches to locate unobserved behavior for review. Pair the result with assertions about public outcomes and failure behavior.

Do not accept a coverage percentage as proof of correctness, and do not classify every uncovered branch as a defect. State the target set, omitted carriers, branch data, and the reliance decision made from it.

Candidate alignment: CA-E-001, CA-E-002, CA-O-003.

## Sources

- [Coverage.py: branch coverage measurement](https://coverage.readthedocs.io/en/latest/branch.html)
- [Pytest documentation](https://docs.pytest.org/en/stable/)
