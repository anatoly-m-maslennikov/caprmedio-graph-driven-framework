---
atom_id: CA-R-2772
ref_id: CA-R-2772
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: Active
version: 2
updated_at: 2026-11-04 20:33:17 +0400
carrier_destination:
  file:
    name: CA-R-2772-RULE--cfel-format-constraint-intersection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2772-CORE_META_MODEL-RULE--cfel-format-constraint-intersection.md
  source_atom_id: CA-R-2772
  source_atom_revision: 2
  source_sha256: 9841dd37b3a32eceeb84d4720bc76e41f3a1358fe8f1c0c5488b3a9d8704a799
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

CFEL Format constraint intersection

## Claim

### Prose Claim

A comma inside one square-bracket value Format annotation combines constraints by intersection. Each direct value must satisfy every listed constraint. Thus `[int, 0..100]` admits integer values from 0 through 100 inclusive. An empty or incompatible intersection admits no values. Existing curly-brace occurrence and value-cardinality annotations keep their current meanings and remain independent.
### Formal Claim

```CFEL
# model
p:: [int, 0..100]{:value count}
```

