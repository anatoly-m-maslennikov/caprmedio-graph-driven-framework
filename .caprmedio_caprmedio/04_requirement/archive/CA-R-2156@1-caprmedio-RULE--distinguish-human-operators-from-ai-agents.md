---
atom_id: CA-R-2156@1
content_role: Requirement
type: Rule
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
tier: 3
subjects:
  governs: Subject/Domain/Node/Continuant/Actor/Type
  depends_on:
  - Subject/Domain/Node/Continuant/Actor
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
version: 1
updated_at: 2026-10-24 07:31:22 +0400
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
