---
version: 24
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-004
  - CA-R-827
  - CA-R-846
  - CA-P-033
  - CA-P-034
subjects:
  governs: Project/authority change
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - CAPRMEDIO Framework Instance
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-1058
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Rule
tier: 2
---
# Require operator authority for governed change

CAPRMEDIO **must** establish **or** change governed Project meaning **only** through explicit per-action acceptance by the Operator **or** active authority explicitly delegated by the Operator **to** the identified AI Agent performing the change.
