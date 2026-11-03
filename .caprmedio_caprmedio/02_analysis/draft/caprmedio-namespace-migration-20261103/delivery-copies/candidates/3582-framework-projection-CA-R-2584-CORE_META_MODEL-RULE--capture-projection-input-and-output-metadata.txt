---
atom_id: CA-R-2584
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Event Record
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2584-CORE_META_MODEL-RULE--capture-projection-input-and-output-metadata.md
  source_atom_id: CA-R-2584
  source_atom_revision: 2
  source_sha256: 8dbc1d6732eacb83873555f2fd33b5766fb39cfbb33d989ac5179b516f674917
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Capture Projection input and output metadata

## Claim

An Event Record for Projection creation or update has object_output. An update record also has object_input; creation input is optional.

For each present Projection input or output, the Event Record captures:

- Projection.ID.
- Projection.Updated At.

object_input contains the values before the change. object_output contains the values after it. Neither side contains a Version. The captured values remain as recorded.
