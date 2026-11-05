---
atom_id: CA-R-2571
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2571-CORE_META_MODEL-RULE--capture-atom-input-and-output-metadata.md
  source_atom_id: CA-R-2571
  source_atom_revision: 2
  source_sha256: 05d16ac5cd49e37e3b7d1fa012c3bfcb9e3a22a597de4b7deb6b461bc2dd5cee
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Capture Atom input and output metadata

## Claim

### Prose Claim


An Event Record for Atom creation or update has object_output. An update record also has object_input; creation input is optional.

For each present Atom input or output, the Event Record captures:

- Atom.Header.ID.
- Atom.Header.Version.
- Atom.Header.Updated At.

object_input contains the values before the change. object_output contains the values after it. Their IDs may differ. The captured values remain as recorded.
