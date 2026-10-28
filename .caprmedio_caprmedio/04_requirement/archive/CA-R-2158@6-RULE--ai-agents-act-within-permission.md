---
atom_id: CA-R-2158@6
content_role: Requirement
type: Rule
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
tier: 4
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
version: 6
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-R-2157
cce_version: cce_1
cce_form: permission
---
# Summary

AI Agents act within permission

## Claim

an AI Agent has no original authority, **must not** create **or** expand its own authority, **and** **may** perform **or** authorize a governed action **only** **when** a current Operator-established AI Agent Delegation **or** authorization rule identifies that AI Agent **and** permits the complete action, its target, **and** its decision boundary.
