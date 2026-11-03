---
atom_id: CA-R-2631
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.RMED Review
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Declare Project.Settings.RMED Review

## Claim

```CFEL
Project.Settings.RMED Review{:0..1}: []{:0};
Project.Settings.RMED Review.*[in (Context Headroom Fraction, Max Atoms)]{:0..2}
```
