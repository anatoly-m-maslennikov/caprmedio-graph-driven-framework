---
atom_id: CA-R-2711
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold
version: 6
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
updated_at: 2026-11-04 21:11:03 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
  source_atom_id: CA-R-2711
  source_atom_revision: 6
  source_sha256: 0506c8ab90381874d50fd3f368b97217a392271e555c495b2b03d47bcf8267c3
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold: [int, 0..100]{:0..1};

Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold.*[]{:0};

# instances
Atom/(.Header.Role: Plan)//$plan;
Scope Unit/Project//$project{:1};

$plan.Header.AI Agent Confidence Threshold
  ?== LOOKUP(Relation//IS_CONTAINED_BY, Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold)
  ?== $project.Settings.AI Agent Confidence Threshold
```
