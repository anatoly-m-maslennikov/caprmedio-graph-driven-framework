---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Filename.Scope Unit Token
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-302
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary
Serialize Scope Unit References as Filename Tokens

## Claim

### Prose Claim

Scope Unit references serialized **in** Atom filenames.


**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.
