---
atom_id: CA-R-2628
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Tool Selections
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 07:52:54 +0400
---

## Summary

Declare Project.Settings.Tool Selections

## Claim

Encode selected active and background Tools with their per-Tool settings.

```CFEL
Project.Settings.Tool Selections{:0..1}: []{:0};
Project.Settings.Tool Selections.*[string]{:0+}
```
