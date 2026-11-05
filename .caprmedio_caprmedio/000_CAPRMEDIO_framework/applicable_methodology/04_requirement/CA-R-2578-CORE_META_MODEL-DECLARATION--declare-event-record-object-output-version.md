---
atom_id: CA-R-2578
ref_id: CA-R-2578
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.object_output.version
tier: 3
status: Active
version: 3
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2578-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-version.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2578-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-version.md
  source_atom_id: CA-R-2578
  source_atom_revision: 3
  source_sha256: b43d73694fff3e8e510ff9f2eae4e3dd497d53c6a23cd4055212398b3f7a4539
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record.object_output.version

## Claim

### Formal Claim

```CFEL
# model
Event Record.object_output.version:: [int]{::0..1};

Event Record.object_output.version.*[]{::0}
```

