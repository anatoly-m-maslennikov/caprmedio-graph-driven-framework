---
atom_id: CA-R-1591
ref_id: CA-R-1591
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
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
tier: 2
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1591-CORE_META_MODEL-RULE--apply-autonomous-confidence-thresholds-to-plan-execution.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Apply autonomous confidence thresholds to Plan execution

## Claim

### Prose Claim


autonomous continuation of Plan work.


autonomous continuation of Plan work **must** satisfy its effective Autonomous Confidence Threshold:

- resolve the value under CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.
- **if** confidence **in** correct execution is below it, request Operator disposition **before** continuing.
- **otherwise**, continue **only** within existing authority; meeting the threshold does **not** grant additional authority.
