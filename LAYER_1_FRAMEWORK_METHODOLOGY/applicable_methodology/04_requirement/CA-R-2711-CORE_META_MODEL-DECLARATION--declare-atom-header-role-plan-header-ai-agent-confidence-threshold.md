---
atom_id: CA-R-2711
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold
version: 2
relations: {}
tier: 3
updated_at: 2026-11-04 05:21:15 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
  source_atom_id: CA-R-2711
  source_atom_revision: 2
  source_sha256: af3db8d7f4041a599002215975f96b3101e0f9383224b80eede75e93ffd24949
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold: [int]{:0..1};

Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold.*[]{:0};

# instances
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold
  ?= LOOKUP(Relation//IS_CONTAINED_BY, Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
```
