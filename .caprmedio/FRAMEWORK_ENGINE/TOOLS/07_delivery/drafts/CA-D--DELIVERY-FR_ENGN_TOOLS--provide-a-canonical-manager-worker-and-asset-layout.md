---
subject_scopes:
  - python-engineering
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Provide a canonical manager, worker, and asset layout

Deliver each Tool under its safe uppercase Tool directory with exactly one pure manager named `<tool_name>.py`. Place effectful or independently executable atomic workers under `<tool_name>_workers/` and reusable non-Python static resources under `<tool_name>_assets/`. Omit an empty optional directory.

Use the shared Tool transport adapter for CLI parsing and result emission so the manager remains I/O-free. Keep the manager-produced execution graph explicit and keep direct worker handoffs acyclic. Static mappings larger than the declared source threshold live in assets: TOML by default, JSON for schemas or machine interchange, and YAML only when its distinct features are required.

Register every long-running worker through the background-service lifecycle so it is supervised independently and does not terminate merely because an invoking manager exits.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-M-005, CA-R-861.

## Sources

- [Python documentation: modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Packaging User Guide: package discovery](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: `subprocess`](https://docs.python.org/3/library/subprocess.html)
