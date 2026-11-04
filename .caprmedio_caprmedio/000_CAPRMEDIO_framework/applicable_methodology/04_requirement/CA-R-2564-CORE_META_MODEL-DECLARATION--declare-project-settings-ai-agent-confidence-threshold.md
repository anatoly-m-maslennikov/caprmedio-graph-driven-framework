---
atom_id: CA-R-2564
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.AI Agent Confidence Threshold
version: 4
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-04 20:33:16 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2564-CORE_META_MODEL-DECLARATION--declare-project-settings-ai-agent-confidence-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2564-CORE_META_MODEL-DECLARATION--declare-project-settings-ai-agent-confidence-threshold.md
  source_atom_id: CA-R-2564
  source_atom_revision: 4
  source_sha256: 6c1dc5f3c6f0d1f6aec7380c769824760da4de9497f46122fa45e660055e69b9
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Declare Project.Settings.AI Agent Confidence Threshold

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.AI Agent Confidence Threshold{:1}: [int, 0..100]{:1} ?== 90;

Project.Settings.AI Agent Confidence Threshold.*[]{:0}
```

