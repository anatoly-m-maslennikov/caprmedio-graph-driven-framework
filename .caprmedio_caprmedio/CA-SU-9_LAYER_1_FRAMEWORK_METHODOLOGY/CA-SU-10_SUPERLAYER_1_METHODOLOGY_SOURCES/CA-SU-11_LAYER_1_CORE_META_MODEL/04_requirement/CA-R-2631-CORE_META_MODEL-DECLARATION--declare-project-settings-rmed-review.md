---
atom_id: CA-R-2631
ref_id: CA-R-2631
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2631-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
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

