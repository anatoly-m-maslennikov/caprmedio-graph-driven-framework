---
atom_id: CA-R-2572
ref_id: CA-R-2572
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.object_input
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2572-CORE_META_MODEL-DECLARATION--declare-event-record-object-input.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2572-CORE_META_MODEL-DECLARATION--declare-event-record-object-input.md
  source_atom_id: CA-R-2572
  source_atom_revision: 2
  source_sha256: 10bd6268ed7202b9107e2d2495e1b607b512edc72bc0c18f4c0b1d17b73fef87
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record.object_input

## Claim

### Formal Claim

```CFEL
# model
Event Record.object_input{::0..1}:: []{::0};

Event Record.object_input.*[in(id,version,updated_at)]{::2..3}
```

