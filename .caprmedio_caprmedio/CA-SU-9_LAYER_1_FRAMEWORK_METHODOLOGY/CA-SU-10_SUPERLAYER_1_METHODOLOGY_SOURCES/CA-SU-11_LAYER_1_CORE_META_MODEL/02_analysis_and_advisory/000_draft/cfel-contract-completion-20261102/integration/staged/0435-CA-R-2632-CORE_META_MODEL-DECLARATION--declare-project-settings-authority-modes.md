---
atom_id: CA-R-2632
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.Authority Modes
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 07:49:21 +0400
---

## Summary

Declare Project.Settings.Authority Modes

## Claim

When this group is authored, both Project Authority Mode and Default Scope Unit Authority Mode are required. Each value is either `strict` or `casual`. An omitted override follows its governed fallback. A local Scope Unit override belongs only to its Project Structure declaration.

```CFEL
Project.Settings.Authority Modes{:0..1}: []{:0};
Project.Settings.Authority Modes.*[in (Default Scope Unit Authority Mode, Project Authority Mode)]{:2}
```
