---
atom_id: CA-R-2158
current_scope_unit: caprmedio
status: Active
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
version: 12
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-2157
cce_version: cce_1
cce_form: permission
role: Requirement
form: Rule
---
## Summary

AI Agents act within permission

## Claim

### Prose Claim


an AI Agent has no original authority, **must not** create **or** expand its own authority, **and** **may** perform **or** authorize a governed action **only** **when** a current Operator-established AI Agent Delegation **or** authorization rule identifies that AI Agent **and** permits the complete action, its target, **and** its decision boundary.
