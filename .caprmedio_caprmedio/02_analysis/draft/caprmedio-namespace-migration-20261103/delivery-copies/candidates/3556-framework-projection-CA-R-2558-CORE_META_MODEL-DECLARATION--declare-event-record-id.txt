---
atom_id: CA-R-2558
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Event Record.ID
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2558-CORE_META_MODEL-DECLARATION--declare-event-record-id.md
  source_atom_id: CA-R-2558
  source_atom_revision: 2
  source_sha256: 8a460c945b3434c6357a23152cffedf2a770aa94c817c33db299e09962ae3c92
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record.ID

## Claim

```CFEL
Event Record.ID{:1}: [string]{:1};
Event Record.ID.*[]{:0};
UNIQUE(Event Record//, (.ID))
```
