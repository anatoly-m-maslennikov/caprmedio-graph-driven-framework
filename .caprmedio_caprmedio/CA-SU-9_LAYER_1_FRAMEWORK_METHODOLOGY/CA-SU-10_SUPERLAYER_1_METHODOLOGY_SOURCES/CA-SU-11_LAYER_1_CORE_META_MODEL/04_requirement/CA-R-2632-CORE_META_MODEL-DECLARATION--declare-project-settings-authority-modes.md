---
atom_id: CA-R-2632
ref_id: CA-R-2632
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Authority Modes
tier: 3
status: Active
version: 4
updated_at: '2026-11-11 16:04:42 +0400'
---
## Summary

Declare Project.Settings.Authority Modes

## Claim

### Prose Claim

When authored, Project Authority Mode and Default Scope Unit Authority Mode are both required. Each value is `strict` or `casual`.

### Formal Claim

```CFEL
# model
Project.Settings.Authority Modes{::0..1}:: []{::0};

Project.Settings.Authority Modes.*[in (Default Scope Unit Authority Mode, Project Authority Mode)]{::2};

Project.Settings.Authority Modes.*:: [string]
```
