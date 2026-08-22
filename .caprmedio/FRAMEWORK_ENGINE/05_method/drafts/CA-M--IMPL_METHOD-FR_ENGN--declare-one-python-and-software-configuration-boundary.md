---
subject_scopes:
  - framework-engine-python
version: 4
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Declare one Python and software configuration boundary

Declare the supported Python range and the canonical technical configuration for formatting, linting, typing, testing, and packaging before adopting syntax or behavior that depends on them. Keep interpreter targets and development-tool rules in one project-owned `pyproject.toml` surface so local, installed, and automated evaluation do not silently disagree.

Do not treat the newest locally available interpreter as the project minimum. Change the boundary deliberately and verify every supported runtime before using a runtime-specific idiom as the default.

Keep this technical configuration distinct from CAPRMEDIO project settings. Runtime behavior reads the generated `.caprmedio/caprmedio_project_settings.toml` Projection only through the centralized Settings Reader.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-R-861.

## Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
