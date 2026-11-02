---
subjects:
  governs: Subject/Engineering/Git/Hook
  depends_on: []
version: 19
updated_at: 2026-10-24 13:39:34 +0400
relations:
  evaluation_for:
  - CA-R-856
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-215@19
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
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
