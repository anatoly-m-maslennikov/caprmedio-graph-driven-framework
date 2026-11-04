---
atom_id: CA-R-2574
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record.object_input.version
version: 3
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2574-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-version.md
  source_atom_id: CA-R-2574
  source_atom_revision: 3
  source_sha256: f2fa27e7ba696155c96618cc6cb2248b5d2236f38bc163d942774d0b5f4dbb03
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record.object_input.version

## Claim

### Formal Claim

```CFEL
# model
Event Record.object_input.version: [int]{:0..1};

Event Record.object_input.version.*[]{:0}
```

