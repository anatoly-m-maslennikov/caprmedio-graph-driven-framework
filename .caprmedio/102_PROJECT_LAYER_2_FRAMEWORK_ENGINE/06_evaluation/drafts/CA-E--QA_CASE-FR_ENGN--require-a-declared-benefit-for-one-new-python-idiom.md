---
subject_scopes:
  - framework-engine-python
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Require a declared benefit for one new Python idiom

Given a change that replaces a supported Python idiom with a newer runtime-dependent construct, identify the claimed correctness, understandability, safety, or measured-performance benefit. Verify the construct lies inside the declared runtime boundary and that the evidence distinguishes it from the simpler supported form.

The case rejects novelty alone as a benefit and specifically rejects a t-string where immediate trusted string construction needs no interpolation processor.

Candidate alignment: CA-E-001, CA-E-002, CA-M-005, CA-D-001, CA-R-861.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
