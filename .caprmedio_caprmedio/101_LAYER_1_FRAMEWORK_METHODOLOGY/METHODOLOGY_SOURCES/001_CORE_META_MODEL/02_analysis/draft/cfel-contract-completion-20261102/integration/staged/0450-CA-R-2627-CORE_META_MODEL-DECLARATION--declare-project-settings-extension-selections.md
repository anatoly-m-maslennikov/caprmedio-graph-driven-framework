---
atom_id: CA-R-2627
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Extension Selections
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Declare Project.Settings.Extension Selections

## Claim

Encode enabled and disabled installed Extensions. Retain the selected revision when applicable and retain per-Extension settings. Retained settings do not activate a disabled Extension.

```CFEL
Project.Settings.Extension Selections{:0..1}: []{:0};
Project.Settings.Extension Selections.*[string]{:0+}
```
