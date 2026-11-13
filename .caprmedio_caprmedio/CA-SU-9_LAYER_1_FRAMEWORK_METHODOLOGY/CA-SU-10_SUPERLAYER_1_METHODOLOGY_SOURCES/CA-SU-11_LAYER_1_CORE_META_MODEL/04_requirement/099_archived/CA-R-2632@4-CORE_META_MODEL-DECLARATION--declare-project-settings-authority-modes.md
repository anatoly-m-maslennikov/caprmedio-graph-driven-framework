---
atom_id: CA-R-2632
ref_id: CA-R-2632@4
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Authority Modes
tier: 3
status: archived
version: 4
updated_at: 2026-11-11 16:04:42 +0400
container:
  scope_unit: CA-SU-11
destination:
  file:
    name: CA-R-2632@4-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
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
