---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method).Header.Status'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1397
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Register Core Method Status Values

## Claim

### Prose Claim


the Core Method Status model.


the Core allowed values of Method Status **must** be exactly (Draft, Active, Archived).
