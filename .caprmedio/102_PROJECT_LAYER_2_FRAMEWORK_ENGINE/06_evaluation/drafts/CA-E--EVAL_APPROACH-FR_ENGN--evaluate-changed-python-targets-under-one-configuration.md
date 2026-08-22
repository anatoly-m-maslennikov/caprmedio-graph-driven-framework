---
subject_scopes:
  - framework-engine-python
version: 3
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Evaluate changed Python targets under one configuration

For each changed or newly added Python target, require syntax compilation, canonical Ruff formatting, the admitted Ruff lint rules, strict Mypy checking, and the relevant behavioral tests under the same declared interpreter and technical configuration. Reject a new unexplained suppression. Report each mechanism independently so one passing check cannot mask another mechanism's failure.

Adopt the checks from a bounded passing target set and ratchet their scope without forcing untouched legacy modules into the gate. A failure must identify the target, tool, rule or diagnostic, supported-runtime boundary, and replay command involved.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-R-861.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy: using mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [PyPA: pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
