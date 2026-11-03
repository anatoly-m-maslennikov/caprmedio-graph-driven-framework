---
atom_id: CA-R-2271
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
relations: {}
version: 3
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2271-CORE_META_MODEL-ENTITY_DEFINITION--define-framework-settings-confidence-and-capability-selections.md
  source_atom_id: CA-R-2271
  source_atom_revision: 3
  source_sha256: 2e29ec4833af86d4395e34c9e56131decec0bcc01b7b82fd51e80cd2c7d02e52
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Framework Settings confidence and capability selections

## Claim

Framework Settings may explicitly override the necessary-information and semantic-resolution confidence defaults as integer percentages. Their effective defaults remain Operator-configurable under CA-R-1652 and CA-R-380; absence of an explicit value preserves the governed default resolution.

Tool Selections groups the selected active/background capabilities and their per-capability settings. Extension Selections groups enabled or disabled installed Extensions, selected Versions where applicable, and retained per-Extension settings. These are structured groups with no direct scalar value; retaining settings does not enable a disabled Extension. Their internal declarations remain governed by applicable D authority, not a new generic schema.

### Formal claim

```text
Project.Framework Settings.Confidence.Necessary Information Threshold[int]{0..1}
Project.Framework Settings.Confidence.Semantic Resolution Threshold[int]{0..1}
Project.Framework Settings.Tool Selections{0}
Project.Framework Settings.Extension Selections{0}
```

## Details

CA-D-368, CA-D-369, CA-D-372 and CA-D-373 retain their serialization requirements. No current Settings value changes, unknown field migration, Tool catalog or Extension object is introduced. C613 tracks the minimal shared-schema continuation.
