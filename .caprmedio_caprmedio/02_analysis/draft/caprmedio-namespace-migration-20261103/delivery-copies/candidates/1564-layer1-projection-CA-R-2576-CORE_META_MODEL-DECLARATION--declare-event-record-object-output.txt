---
atom_id: CA-R-2576
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Event Record.object_output
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2576-CORE_META_MODEL-DECLARATION--declare-event-record-object-output.md
  source_atom_id: CA-R-2576
  source_atom_revision: 2
  source_sha256: eff93b679bec3762f89b2e8470c795ddbaa4f6b08c2b195610857bfceb0b86bf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record.object_output

## Claim

```CFEL
Event Record.object_output{:0..1}: []{:0};
Event Record.object_output.*[in(id,version,updated_at)]{:2..3}
```
