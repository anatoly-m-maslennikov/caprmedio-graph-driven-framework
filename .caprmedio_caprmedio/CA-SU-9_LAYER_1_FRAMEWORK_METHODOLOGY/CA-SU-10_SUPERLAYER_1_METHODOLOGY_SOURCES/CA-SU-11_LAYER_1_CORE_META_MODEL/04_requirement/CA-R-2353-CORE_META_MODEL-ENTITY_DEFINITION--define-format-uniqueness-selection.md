---
atom_id: CA-R-2353
ref_id: CA-R-2353
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format.Uniqueness Selection
version: 6
updated_at: 2026-11-04 05:21:15 +0400
tier: 1
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2353-CORE_META_MODEL-DECLARATION--define-format-uniqueness-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Format Uniqueness Selection

## Claim

### Formal Claim

```CFEL
# model
Format.Uniqueness Selection:: [string]{::0..1};

Format.Uniqueness Selection.*[]{::0}
```

### Prose Claim


Format Uniqueness Selection identifies the comparison population for a
Property uniqueness check. It is optional and does not itself impose
uniqueness. It does not define a notation.



