---
version: 15
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CA-R-1407
  - CA-M-001
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Project/cross-unit relation ownership
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Scope Unit
  - Relational Atom
  - Atom/Scope
  - Atom/Claim
  - Consumer
  - Producer
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Demand'
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-881@15
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Rule
tier: 1
---
# Use relation-specific cross-unit ownership

cross-unit relation ownership **must** follow the applicable relation-family authority rather than a universal common-ancestor rule; a Demand **must** be owned by its Consumer Scope Unit under CA-R-932 **and** **must** constrain **only** the Producer result that Consumer is permitted **to** depend on, with the applicable ancestry **and** ordered-sibling restrictions preserved.
