---
atom_id: CA-R-1587
ref_id: CA-R-1587
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Plan).Header.Context.Plan.AI Agent Confidence Threshold
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)'
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
tier: 1
status: Active
version: 26
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1587-CORE_META_MODEL-RULE--require-an-effective-confidence-threshold-for-plan-execution.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Require an effective confidence threshold for Plan execution

## Claim

### Prose Claim


autonomous Plan execution decisions.


**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.
