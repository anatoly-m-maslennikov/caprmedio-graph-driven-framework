---
atom_id: CA-R-2629
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Project.Settings.RMED Review.Context Headroom Fraction
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2629-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-context-headroom-fraction.md
  source_atom_id: CA-R-2629
  source_atom_revision: 1
  source_sha256: c270271b57fb58487029dfd08d5aac5669c6942a8a911aa34e6916e5f2f3048d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.RMED Review.Context Headroom Fraction

## Claim

When present, the value is finite and strictly between zero and one.

```CFEL
Project.Settings.RMED Review.Context Headroom Fraction{:0..1}: [float]{:1};
Project.Settings.RMED Review.Context Headroom Fraction.*[]{:0}
```
