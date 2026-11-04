---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand).Target Scope Unit
version: 29
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-D-287
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Demand Type and Producer Scope

## Claim

### Prose Claim


Demand Atom filenames.


**every** Demand Atom filename **must** serialize its Type **and** Producer Scope as `DEMANDS_FROM-<PRODUCER_SCOPE>`.
