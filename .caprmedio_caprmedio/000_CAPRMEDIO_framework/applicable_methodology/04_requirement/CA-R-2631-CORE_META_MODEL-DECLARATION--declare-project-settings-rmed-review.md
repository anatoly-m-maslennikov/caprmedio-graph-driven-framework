---
atom_id: CA-R-2631
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2631-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review.md
  source_atom_id: CA-R-2631
  source_atom_revision: 1
  source_sha256: c16309a9f2dd08faca661f747f7622d799a0b507434e37d90939466c187ea759
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.RMED Review

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.RMED Review{:0..1}: []{:0};

Project.Settings.RMED Review.*[in (Context Headroom Fraction, Max Atoms)]{:0..2}
```

