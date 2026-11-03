---
atom_id: CA-R-2518
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Concern).Priority
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom/(.Role := Concern).Priority

## Claim

```CFEL
Atom/(.Role: Concern).Priority{:1}: [string]{:1};
Atom/(.Role: Concern).Priority.*[]{:0};
Atom/(.Role: Concern).Priority: High;
Atom/(.Role: Concern).Priority: Medium;
Atom/(.Role: Concern).Priority: Low
```
