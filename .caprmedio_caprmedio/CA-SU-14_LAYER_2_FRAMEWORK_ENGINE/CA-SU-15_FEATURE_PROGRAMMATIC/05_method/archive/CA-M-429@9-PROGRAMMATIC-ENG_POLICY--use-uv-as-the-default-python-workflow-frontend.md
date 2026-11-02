---
atom_id: CA-M-429@9
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Engineering/Python Environment Frontend
  depends_on:
  - Subject/Engineering/Technical Configuration Boundary
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
version: 9
updated_at: 2026-10-24 10:48:25 +0400
cce_version: cce_1
cce_form: method
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-415
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 4
author: Anatoly Maslennikov
---
# Summary

Use uv as the default Python workflow frontend

use uv as the default frontend for **every** admitted Python workflow capability
that uv provides. this Method owns that tool selection; configuration **and**
Implementation materialize it, Delivery governs its carriers, Operations defines reusable workflow behavior,
**and** Journal Records carry evidence of actual workflow execution.

## Details

Candidate source: [CA-M-221@15](archive/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend@15.md)

## Applicable when

apply **when** developing, evaluating, building, packaging, **or** executing
PROGRAMMATIC Python source, including installed Project Tools **and** host launchers.

## Procedure

1. resolve the supported Python boundary from its accepted Method **and** canonical
   Project technical-configuration materialization, **then** install **or** select it
   through `uv python`.
2. materialize dependencies selected by accepted Methods **in** `pyproject.toml`;
   change them through `uv add` **or** `uv remove` so the declaration **and** `uv.lock`
   change together.
3. reproduce the project environment with `uv sync --locked` **and** execute
   governed Python commands with `uv run --locked`.
4. run an isolated Python CLI through `uv tool run` **only** with a pinned tool
   version **and** command **when** it is **not** an admitted project dependency.
   unpinned ephemeral execution cannot supply acceptance evidence.
5. use `uv build` **or** `uv publish` **only** **when** an accepted Delivery authorizes a
   package **or** publication target.
6. do **not** mix pip, venv, virtualenv, pipx, Poetry, Conda, a naked/system
   Python interpreter, system-installed libraries, **or** another overlapping
   Python workflow manager into the governed Project-Python path. A capability
   gap or external boundary does not authorize a non-uv fallback for Project Python.
7. stop rather than record a non-uv fallback exception for Project Python.
8. apply CA-M-423's uv-managed environment boundary to installed Tools **and**
   host launchers as well as development commands. Packaged runtimes retain
   their selected isolated environment **and** locked dependencies; child
   processes reuse **only** that environment's interpreter. Route uv cache,
   build, **and** staging state into `.caprmedio_tmp/`.

## Outcome

one declared Python boundary **and** one reviewed lockfile reproduce the admitted
Python environment **and** commands **without** an undeclared manager **or** dependency
source.

## Failure or stop

stop **when** the supported interpreter cannot be resolved, the lockfile is stale,
a command would update the environment implicitly during evidence collection,
or a Project-Python command would use a non-uv, naked/system, or system-library
fallback.

## Sources

- [uv: Features](https://docs.astral.sh/uv/getting-started/features/)
- [uv: Installing and managing Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv: Tools](https://docs.astral.sh/uv/concepts/tools/)
- [uv: Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
