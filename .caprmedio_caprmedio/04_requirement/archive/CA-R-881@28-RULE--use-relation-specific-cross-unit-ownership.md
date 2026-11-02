---
version: 28
updated_at: 2026-10-29 07:45:26 +0400
relations:
  child_of:
  - CA-R-1407
  - CA-M-001
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Demand'
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-881@28
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Rule
tier: 1
---
## Summary
Use relation-specific cross-unit ownership

## Claim

cross-unit relation ownership **must** follow the applicable relation-family authority rather than a universal common-ancestor rule; a Demand **must** be owned by its Consumer Scope Unit under CA-R-932 **and** **must** constrain **only** the Producer result that Consumer is permitted **to** depend on, with the applicable ancestry **and** ordered-sibling restrictions preserved.
