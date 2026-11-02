---
subjects:
  governs: Git Hook/Path
  depends_on: []
version: 12
updated_at: 2026-10-23 03:17:34 +0400
relations:
  evaluation_for:
  - CA-R-856
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-215@12
status: Archived
---
# Reject a custom Git Hooks path conflict without mutation

## Claim checked

Installing the managed Git Hooks fails safely **when** the repository already declares another local `core.hooksPath`.

## Test case

Prepare a repository with a custom local `core.hooksPath`, executable Hook carriers **and** recorded bytes **and** modes, but no managed CAPRMEDIO Git Hook registration; invoke `INSTALL_TOOLS run --apply`.

## Acceptance criteria

Installation returns one stable conflict diagnostic. The configured path, **every** referenced Hook byte **and** mode, adapter registry, Git configuration, index, refs, `.caprmedio_runtime/tools`, **and** `.caprmedio_runtime` remain unchanged, **and** no backup carrier is created.

## Failure disposition

Reject the delivery **if** installation replaces, merges, copies, backs up, **or** partially registers over the custom Hook configuration, **or** **if** the failure is **not** deterministic.
