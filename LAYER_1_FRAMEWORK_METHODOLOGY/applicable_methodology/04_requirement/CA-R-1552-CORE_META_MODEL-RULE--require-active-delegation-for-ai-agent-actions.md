---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent.Permissions
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2158
atom_id: CA-R-1552
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1552-CORE_META_MODEL-RULE--require-active-delegation-for-ai-agent-actions.md
  source_atom_id: CA-R-1552
  source_atom_revision: 22
  source_sha256: 17a5820534c23076f91bb2bee93f2145ea048c6fe1acb08790c6265028c2c8fe
  original_relations_sha256: 0846560adec6e797c5d882986f62e94d5629228d50d23e6fc9dd80a0ea12d72a
---
## Summary

Require active delegation for AI Agent actions

## Claim

### Prose Claim


AI Agent actions under active Operator-issued delegation.


an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** **when** an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.
