---
atom_id: CA-R-2630
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Max Atoms
version: 2
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
---

## Summary

Declare Project.Settings.RMED Review.Max Atoms

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.RMED Review.Max Atoms: [int]{:0..1};

Project.Settings.RMED Review.Max Atoms.*[]{:0}
```

### Prose Claim


When present, the value is positive. Its absence supplies no default.

