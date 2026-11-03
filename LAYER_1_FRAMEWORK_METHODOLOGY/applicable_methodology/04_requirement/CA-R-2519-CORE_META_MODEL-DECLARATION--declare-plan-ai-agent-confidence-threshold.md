---
atom_id: CA-R-2519
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Plan).AI Agent Confidence Threshold
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2519-CORE_META_MODEL-DECLARATION--declare-plan-ai-agent-confidence-threshold.md
  source_atom_id: CA-R-2519
  source_atom_revision: 2
  source_sha256: a010d7fa397535e84978f284a700ddc81d3a35ce00158254e7b595dcb57cdc8f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Role := Plan).AI Agent Confidence Threshold

## Claim

```CFEL
Atom/(.Role: Plan).AI Agent Confidence Threshold{:0..1}: [int]{:1};
Atom/(.Role: Plan).AI Agent Confidence Threshold.*[]{:0};
Atom/(.Role: Plan).AI Agent Confidence Threshold
  ?= LOOKUP(IS_CONTAINED_BY, Atom/(.Role: Plan).AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
```
