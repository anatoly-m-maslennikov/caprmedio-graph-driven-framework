---
atom_id: CA-R-2539
ref_id: CA-R-2539
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Updated At
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2539-CORE_META_MODEL-DECLARATION--declare-projection-updated-at.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Projection.Updated At

## Claim

### Formal Claim

```CFEL
# model
Projection.Updated At{::1}:: [datetime]{::1};

Projection.Updated At.*[]{::0};

# instances
Projection//$projection.Updated At == MAX(Event Record//$event_record(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update)).happened_at)
```

