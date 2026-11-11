---
atom_id: CA-R-2156
current_scope_unit: caprmedio
status: Active
tier: 3
subjects:
  active: Actor
  passive:
  - Actor
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2452
cce_version: cce_1
cce_form: classification
role: Requirement
form: Rule
---
## Summary

Distinguish human Operators from AI Agents

## Claim

**every** Actor that performs **or** authorizes a governed action **must** have **`=1`** Type **in** (Operator, AI Agent).
