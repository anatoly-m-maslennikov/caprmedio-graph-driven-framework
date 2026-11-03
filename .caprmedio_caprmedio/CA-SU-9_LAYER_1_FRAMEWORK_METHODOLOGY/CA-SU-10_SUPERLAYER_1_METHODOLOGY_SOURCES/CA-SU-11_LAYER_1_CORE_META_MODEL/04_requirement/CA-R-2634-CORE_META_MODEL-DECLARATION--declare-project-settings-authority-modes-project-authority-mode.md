---
atom_id: CA-R-2634
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Authority Modes.Project Authority Mode
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Declare Project.Settings.Authority Modes.Project Authority Mode

## Claim

### Formal Claim

```CFEL
Project.Settings.Authority Modes.Project Authority Mode{:1}: [string]{:1};
Project.Settings.Authority Modes.Project Authority Mode.*[]{:0}
```

### Prose Claim


The permitted values are `strict` and `casual`. The effective selection follows the applicable authority-mode resolution.

