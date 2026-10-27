---
version: 28
updated_at: 2026-10-24 10:48:25 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-004
  - CA-R-827
  - CA-R-846
  - CA-R-2157
  - CA-R-2158
subjects:
  governs: Subject/Domain/Node/Continuant/Project
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - CAPRMEDIO Framework Instance
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-1058@28
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Rule
tier: 5
---
# Require operator authority for governed change

CAPRMEDIO **must** establish **or** change governed Project meaning **only** through explicit per-action acceptance by the Operator **or** active authority explicitly delegated by the Operator **to** the identified AI Agent performing the change.
