---
subject_scopes:
  - installation
version: 1
updated_at: 2026-08-21 20:35:00
relations: {}
---
# Evaluate the installed Toolset across supported boundaries

Build or install the same deliverable that an Operator uses, then run its public evaluations under every declared Python and platform boundary. Verify that the installed Toolset does not import project-source code or depend on undeclared state outside its installation and runtime places.

Report unsupported combinations explicitly. A local source-tree pass does not establish reliance on the installed realization.

Candidate alignment: CA-E-001, CA-E-002, CA-D-001, CA-R-861.

## Sources

- [Pytest: tests outside application code and installed-package testing](https://docs.pytest.org/en/stable/explanation/goodpractices.html)
- [PyPA: requires-python](https://packaging.python.org/en/latest/specifications/core-metadata/#requires-python)
