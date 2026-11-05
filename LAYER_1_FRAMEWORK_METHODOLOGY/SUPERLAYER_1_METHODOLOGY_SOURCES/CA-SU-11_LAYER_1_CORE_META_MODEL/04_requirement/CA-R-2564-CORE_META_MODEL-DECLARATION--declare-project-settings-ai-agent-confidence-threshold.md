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

