---
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  - CAPRMEDIO_MODEL <+ Atom.Content
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1292
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Require an Accepted Goal for Every Scope Unit

## Claim

### Prose Claim


Scope Units and their Claim Target Scope Unit references.


**every** Scope Unit **must** remain the Claim Target Scope Unit of **`>=1`** accepted Goal Atom.
