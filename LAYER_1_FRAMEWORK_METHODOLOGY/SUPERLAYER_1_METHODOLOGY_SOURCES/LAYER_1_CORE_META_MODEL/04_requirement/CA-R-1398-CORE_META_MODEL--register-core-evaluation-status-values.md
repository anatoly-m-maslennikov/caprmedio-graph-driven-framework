---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Status'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1398
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Register Core Evaluation Status Values

## Claim

### Prose Claim


the Core Evaluation Status model.


the Core allowed values of Evaluation Status **must** be exactly (Draft, Active, Archived).
