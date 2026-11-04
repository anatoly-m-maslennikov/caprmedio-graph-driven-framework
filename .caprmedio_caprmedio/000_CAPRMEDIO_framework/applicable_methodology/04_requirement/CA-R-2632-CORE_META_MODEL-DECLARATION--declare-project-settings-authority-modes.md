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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2632-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes.md
  source_atom_id: CA-R-2632
  source_atom_revision: 3
  source_sha256: 7c8d9f295f35dbba9b64b6e3e8873731c92d4ce1e2198e02cf735bcff0b69078
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
