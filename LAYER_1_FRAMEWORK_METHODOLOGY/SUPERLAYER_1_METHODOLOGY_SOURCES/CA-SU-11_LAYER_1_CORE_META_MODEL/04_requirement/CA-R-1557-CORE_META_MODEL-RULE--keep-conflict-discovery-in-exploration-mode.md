---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent.Permissions
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1557
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep conflict discovery in Exploration Mode

## Claim

### Prose Claim


AI Agent discovery of conflicts in Exploration Mode.


an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.
