---
atom_id: CA-R-2490
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Relations.IS_CONTAINED_BY
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Relations.IS_CONTAINED_BY

## Claim

```CFEL
Atom.Relations.IS_CONTAINED_BY{:0..1}: []{:0};
Atom.Relations.IS_CONTAINED_BY.*[in(atom,scope_unit)]{:1}
```
