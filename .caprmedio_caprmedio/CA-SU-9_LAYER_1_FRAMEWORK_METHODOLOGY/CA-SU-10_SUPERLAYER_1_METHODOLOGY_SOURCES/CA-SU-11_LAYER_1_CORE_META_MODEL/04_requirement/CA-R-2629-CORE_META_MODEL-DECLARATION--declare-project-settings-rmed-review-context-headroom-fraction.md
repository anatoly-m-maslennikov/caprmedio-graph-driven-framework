---
atom_id: CA-R-2629
ref_id: CA-R-2629
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Context Headroom Fraction
version: 2
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2629-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-context-headroom-fraction.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Project.Settings.RMED Review.Context Headroom Fraction

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.RMED Review.Context Headroom Fraction:: [float]{::0..1};

Project.Settings.RMED Review.Context Headroom Fraction.*[]{::0}
```

### Prose Claim


When present, the value is finite and strictly between zero and one.

