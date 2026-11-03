---
version: 35
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-O-024
  - CA-O-016
  - CA-R-1559
  - CA-M-295
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action//Implementation Retry Control'
  passive:
  - Entity/Object/Continuant/Actor/Operator
  - Atom/(.Role := Evaluation)
  - Aspects <+ Engineering <+ Execution Control <+ Failure Handling
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Project
  - Entity/Object/Occurrent/Execution/Workflow Run.Implementation Retry Limit
atom_id: CA-E-441
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-441-PROJECT_CONFIGURATION-POLICY--evaluate-retry-budget-and-escalation.md
  source_atom_id: CA-E-441
  source_atom_revision: 35
  source_sha256: 28ea301e87c9b58695036d58b30a6cc4afbae957218f504d55e9fd335429e402
  original_relations_sha256: 52c1f0b5c3a2b439de8cfe87809ef5d2ebda914234b7522c46871c374e39bf08
---
## Summary

Evaluate retry budget **and** escalation

## Claim scope

the retry-policy Evaluation.

## Claim

the retry-policy Evaluation **must** return `fail` **if** **any** of the following occurs:

- the initial failed Evaluation consumes a retry.
- an automatic retry exceeds the effective Implementation Retry Limit resolved under CA-M-295-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-implementation-retry-limits-by-source-precedence **and** enforced by CA-O-024-PROJECT_CONFIGURATION-ACTION--control-implementation-retries.
- starting a permitted fix-and-evaluate round is **not** counted once, **or** checking its permission again consumes another retry.
- a changed failure set **or** automatic next loop silently resets the budget.
- the last permitted retry fails **without** pausing **and** reporting remaining failures **to** the Operator.
- retrying bypasses a confidence gate, governing-Atom approval rule, **or** additional Operator constraint.
- successful completion under CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior still triggers another automatic repair retry.

earlier escalation required by governing authority **must not** be rejected merely because retries remain.
