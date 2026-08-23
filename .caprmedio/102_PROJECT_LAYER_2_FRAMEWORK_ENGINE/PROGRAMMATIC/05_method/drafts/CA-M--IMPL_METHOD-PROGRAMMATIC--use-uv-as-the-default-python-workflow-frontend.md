---
subject_scopes:
  - framework-engine-python
  - python-toolchain
version: 1
updated_at: 2026-08-23 16:32:00
relations: {}
---
# Use uv as the default Python workflow frontend

Use uv as the default frontend for every admitted Python workflow capability that uv provides: supported Python installation and selection, the project environment, dependency addition and removal, dependency resolution and locking, environment synchronization, project command execution, isolated Python tool execution, and package build or publication when packaging is separately authorized.

Apply this procedure:

1. Resolve the supported Python boundary from the canonical Project technical configuration and install or select it through `uv python`.
2. Declare project and development dependencies in `pyproject.toml`; change them through `uv add` or `uv remove` so the declared dependency graph and `uv.lock` change together.
3. Reproduce the project environment with `uv sync --locked` and execute governed Python commands with `uv run --locked`.
4. Run an isolated Python CLI through `uv tool run` only with a pinned tool version and command when it is not an admitted project dependency. Unpinned ephemeral execution cannot supply acceptance evidence.
5. Use `uv build` or `uv publish` only when an accepted Delivery authorizes a package or publication target.

Do not mix pip, venv, virtualenv, pipx, Poetry, Conda, or another overlapping Python workflow manager into the same governed path unless uv lacks a required capability or an external boundary requires the alternative. Record any exception with its capability, bounded carriers, exact commands, added operational cost, cleanup or recovery procedure, and Operator acceptance.

Keep uv outside the installed CAPRMEDIO runtime contract. Installed Tools remain self-contained under `.caprmedio_install` and must execute without uv, a project virtual environment, or another dependency outside that installation. uv governs development, evaluation, and authorized packaging workflows; it does not own CAPRMEDIO project settings, business decisions, runtime state, or Git authority.

The Method succeeds when one declared Python boundary and one reviewed lockfile reproduce the admitted Python environment and commands without an undeclared manager or dependency source. Stop when the supported interpreter cannot be resolved, the lockfile is stale, a command would update the environment implicitly during evidence collection, or an exception lacks its accepted boundary.

## Sources

- [uv: Features](https://docs.astral.sh/uv/getting-started/features/)
- [uv: Installing and managing Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv: Tools](https://docs.astral.sh/uv/concepts/tools/)
- [uv: Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
