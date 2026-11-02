---
subject_scopes:
- authority
version: 14
updated_at: 2026-10-29 07:45:26 +0400
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
atom_id: CA-R-025@14
type: Rule
tier: 3
subjects:
  governs: Subject/CAPRMEDIO/Graph/Rule
  depends_on: []
---
## Summary
Preserve higher-tier authority in cross-tier conflicts

## Claim

a conflict between active Requirements at different global tiers **must** preserve the lower-numbered claim **and** reconcile the higher-numbered claim **without** changing the lower-numbered meaning.
