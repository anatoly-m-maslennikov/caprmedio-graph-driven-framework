---
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Authority Modes
version: 3
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
atom_id: CA-R-2632
status: Active
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Project.Settings.Authority Modes

## Claim

When authored, Project Authority Mode and Default Scope Unit Authority Mode are both required. Each value is `strict` or `casual`.

```CFEL
# model
Project.Settings.Authority Modes{:0..1}: []{:0};

Project.Settings.Authority Modes.*[in (Default Scope Unit Authority Mode, Project Authority Mode)]{:2};

Project.Settings.Authority Modes.*: [string]
```
