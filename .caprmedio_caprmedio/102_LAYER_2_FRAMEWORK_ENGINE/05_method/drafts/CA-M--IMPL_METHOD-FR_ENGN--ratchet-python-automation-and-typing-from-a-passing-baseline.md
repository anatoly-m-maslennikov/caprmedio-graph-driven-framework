---
subject_scopes:
  - framework-engine-python
version: 3
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Ratchet Python automation and typing from a passing baseline

Give formatting, linting, typing, and testing one canonical technical configuration, but let each mechanism own its distinct evidence. Start from a bounded target set that passes, require every changed or newly added Python module to pass the strict admitted profile, prevent regressions in that set, and expand legacy coverage deliberately.

Automate mechanical style decisions. Require syntax compilation, canonical Ruff formatting and linting, strict Mypy checking without new unexplained suppressions, and relevant behavioral tests for changed targets. Do not treat any mechanism as a substitute for another or block all current work solely because untouched legacy code has not yet reached the target level.

Candidate alignment: CA-M-002, CA-M-005, CA-R-819, CA-E-001, CA-D-002.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy: using mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
