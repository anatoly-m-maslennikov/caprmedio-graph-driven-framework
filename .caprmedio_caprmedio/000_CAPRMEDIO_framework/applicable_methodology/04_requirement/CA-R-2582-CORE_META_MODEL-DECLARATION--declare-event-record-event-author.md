---
atom_id: CA-R-2582
ref_id: CA-R-2582
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record.Relations.HAS_EVENT_AUTHOR
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2582-CORE_META_MODEL-DECLARATION--declare-event-record-relations-has-event-author.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2582-CORE_META_MODEL-DECLARATION--declare-event-record-event-author.md
  source_atom_id: CA-R-2582
  source_atom_revision: 2
  source_sha256: dafec5d4f9623de4f81da0684ce47a70956fc4e77cf22aa06ace77a7abc5d5be
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record.Relations.HAS_EVENT_AUTHOR

## Claim

### Formal Claim

```CFEL
# model
Event Record.Relations.HAS_EVENT_AUTHOR.*[]{::0};

# instances
Event Record.Relations.HAS_EVENT_AUTHOR{::1}:: [Actor//$actor]{::1};
```

