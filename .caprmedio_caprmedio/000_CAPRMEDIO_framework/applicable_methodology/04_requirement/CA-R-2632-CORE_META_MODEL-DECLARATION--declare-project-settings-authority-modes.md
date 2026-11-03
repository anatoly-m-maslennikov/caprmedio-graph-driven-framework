---
subjects:
  governs: Project.Settings.Authority Modes
version: 2
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
atom_id: CA-R-2632
status: Active
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2632-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes.md
  source_atom_id: CA-R-2632
  source_atom_revision: 2
  source_sha256: e2a99af37c0876bcf3f6bcf707b90ef7b65091c79516ff63be571475030570c1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Project.Settings.Authority Modes

## Claim

When authored, Project Authority Mode and Default Scope Unit Authority Mode are both required. Each value is `strict` or `casual`.

```CFEL
Project.Settings.Authority Modes{:0..1}: []{:0};
Project.Settings.Authority Modes.*[in (Default Scope Unit Authority Mode, Project Authority Mode)]{:2}
```
