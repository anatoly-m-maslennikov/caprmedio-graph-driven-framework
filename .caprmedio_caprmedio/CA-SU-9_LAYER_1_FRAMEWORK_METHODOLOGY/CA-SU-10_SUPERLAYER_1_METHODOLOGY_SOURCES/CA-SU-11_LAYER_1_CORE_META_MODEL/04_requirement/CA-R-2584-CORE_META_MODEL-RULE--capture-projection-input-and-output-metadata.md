---
atom_id: CA-R-2584
ref_id: CA-R-2584
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Event Record
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2584-CORE_META_MODEL-RULE--capture-projection-input-and-output-metadata.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Capture Projection input and output metadata

## Claim

### Prose Claim


An Event Record for Projection creation or update has object_output. An update record also has object_input; creation input is optional.

For each present Projection input or output, the Event Record captures:

- Projection.ID.
- Projection.Updated At.

object_input contains the values before the change. object_output contains the values after it. Neither side contains a Version. The captured values remain as recorded.
