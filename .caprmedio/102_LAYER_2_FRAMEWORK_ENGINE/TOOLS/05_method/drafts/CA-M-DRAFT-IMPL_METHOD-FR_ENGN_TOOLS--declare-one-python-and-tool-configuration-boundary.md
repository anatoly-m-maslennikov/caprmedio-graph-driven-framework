---
subject_scopes:
  - python-engineering
version: 1
updated_at: 2026-08-21 20:30:00
relations: {}
---
# Declare one Python and tool configuration boundary

Declare the supported Python range and the canonical configuration for formatting, linting, typing, testing, and packaging before adopting syntax or behavior that depends on them. Keep interpreter targets and tool rules in one project-owned configuration surface so local, installed, and automated execution do not silently disagree.

Do not treat the newest locally available interpreter as the project minimum. Change the boundary deliberately and verify every supported runtime before using a runtime-specific idiom as the default.

## Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
