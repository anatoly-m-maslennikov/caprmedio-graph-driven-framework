---
subjects:
  governs: Subject/Engineering/Commit Automation
  depends_on: []
version: 20
updated_at: 2026-10-24 12:35:51 +0400
relations:
  evaluation_for:
  - CA-M-087
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-234@20
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Form one folder action during reconciliation

## Test case

Given multiple Git-admitted changes below one non-root folder **and** an explicitly declared grouping policy, **when** COMMIT_AUTOMATION reconciles the current repository frontier, **then** its pure manager forms one folder-subject action with one frozen ordered entry set **and** preserves **every** contributing event identity. COMMIT_TRIGGER does **not** scan **or** group the repository.

## Sources

- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-ENG_DECISION--process-one-project-path-action.md)
