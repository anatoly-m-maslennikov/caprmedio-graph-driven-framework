---
subject_scopes:
- authority
version: 10
updated_at: 2026-10-24 04:48:21 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-024
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-025@10
type: Rule
tier: 3
subjects:
  governs: Subject/Graph/Rule
  depends_on: []
---
# Preserve higher-tier authority in cross-tier conflicts

a conflict between active Requirements at different global tiers **must** preserve the lower-numbered claim **and** reconcile the higher-numbered claim **without** changing the lower-numbered meaning.
