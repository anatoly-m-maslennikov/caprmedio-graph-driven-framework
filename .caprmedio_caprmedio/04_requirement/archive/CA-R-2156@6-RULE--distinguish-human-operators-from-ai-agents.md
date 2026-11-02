---
atom_id: CA-R-2156@6
content_role: Requirement
type: Rule
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
tier: 3
subjects:
  governs: Entity/Object/Continuant/Actor
  depends_on:
  - Entity/Object/Continuant/Actor
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
version: 6
updated_at: 2026-10-29 07:17:14 +0400
relations:
  child_of:
  - CA-R-2155
cce_version: cce_1
cce_form: classification
---
# Summary

Distinguish human Operators from AI Agents

## Claim

**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
