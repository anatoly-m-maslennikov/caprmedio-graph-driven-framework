---
atom_id: CA-R-2771
ref_id: CA-R-2771
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: Active
version: 2
updated_at: 2026-11-04 20:33:16 +0400
carrier_destination:
  file:
    name: CA-R-2771-RULE--cfel-numeric-range-constraint.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2771-CORE_META_MODEL-RULE--cfel-numeric-range-constraint.md
  source_atom_id: CA-R-2771
  source_atom_revision: 2
  source_sha256: 078785173723997ae7295a588b6a7fa1e59ca1465e427c89e47d3d0df63eaae5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

CFEL numeric range constraint

## Claim

### Prose Claim

Inside a square-bracket value Format annotation, `lower..upper` is a closed numeric interval: both endpoints are included. It constrains each direct Property value and does not state Property occurrence or value cardinality. This square-bracket value constraint is distinct from the existing curly-brace cardinality range `{:n..m}`.
### Formal Claim

```CFEL
# model
p:: [0..100]{:value count}
```

