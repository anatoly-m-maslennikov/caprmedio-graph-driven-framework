---
subject_scopes:
- authority
version: 9
updated_at: 2026-10-24 04:48:21 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-028
  - CA-R-031
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-033@9
type: Rule
tier: 2
subjects:
  governs: Subject/Graph/Rule
  depends_on: []
---
# Preserve ancestor Core authority across structural levels

a conflict between active Core Requirements on one ancestor–descendant path **must** preserve the ancestor-scope Core **and** reconcile the descendant-scope Core **without** changing the ancestor meaning.
