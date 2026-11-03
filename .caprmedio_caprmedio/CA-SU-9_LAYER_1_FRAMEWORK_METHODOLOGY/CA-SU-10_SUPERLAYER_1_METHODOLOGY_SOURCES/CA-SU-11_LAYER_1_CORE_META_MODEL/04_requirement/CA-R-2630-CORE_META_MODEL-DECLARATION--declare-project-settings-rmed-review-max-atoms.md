---
atom_id: CA-R-2630
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Max Atoms
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Declare Project.Settings.RMED Review.Max Atoms

## Claim

When present, the value is positive. Its absence supplies no default.

```CFEL
Project.Settings.RMED Review.Max Atoms{:0..1}: [int]{:1};
Project.Settings.RMED Review.Max Atoms.*[]{:0}
```
