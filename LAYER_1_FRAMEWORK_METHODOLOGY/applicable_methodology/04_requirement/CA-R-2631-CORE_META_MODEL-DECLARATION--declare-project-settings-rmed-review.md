---
atom_id: CA-R-2631
ref_id: CA-R-2631
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-2631-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2631-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review.md
  source_atom_id: CA-R-2631
  source_atom_revision: 1
  source_sha256: 3685461945b24def89d610671eaf051cff4a8ea3bfea90088a5f1fcb747c0f3f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.RMED Review

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.RMED Review{::0..1}:: []{::0};

Project.Settings.RMED Review.*[in (Context Headroom Fraction, Max Atoms)]{::0..2}
```

