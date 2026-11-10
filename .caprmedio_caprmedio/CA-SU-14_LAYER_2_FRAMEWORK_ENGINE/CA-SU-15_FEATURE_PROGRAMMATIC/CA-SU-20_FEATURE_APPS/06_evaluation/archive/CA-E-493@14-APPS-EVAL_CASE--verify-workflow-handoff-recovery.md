---
atom_id: CA-E-493
ref_id: CA-E-493
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 5
relations:
  evaluation_for:
  - CA-R-1524
  - CA-M-302
  depends_on:
  - CA-E-352
status: Archived
version: 14
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-E-493@14-APPS-EVAL_CASE--verify-workflow-handoff-recovery.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/06_evaluation/archive
current_scope_unit: APPS
destination:
  file:
    name: CA-E-493-WORKFLOW_ORCHESTRATOR-EVAL_CASE--verify-workflow-handoff-recovery.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/06_evaluation
---

## Summary

Verify Workflow handoff recovery

## Claim

### Prose Claim

the Evaluation **must** check WORKFLOW_ORCHESTRATOR recovery at the boundaries of an update-to-replacement handoff under CA-R-1524.

## Details

### Interruption cases

- interrupt **before** the handoff is durable: recovery **must not** assume an accepted successor dispatch.
- interrupt **after** durable handoff but **before** successor start: resume the same continuation intent **without** losing the accepted request.
- interrupt **after** successor start but **before** its acknowledgement: repeated dispatch delivery **must not** create another successor Run.
- lose the response **after** a non-repeatable effect: require reconciliation evidence **or** escalation rather than blind replay.
- change the target Revision **or** revoke permission **before** resumed execution: require paused dispatch under the applicable validation rules rather than use of stale approval **or** inputs.
- change a bound Workflow **or** Action definition during a wait **or** service restart: require paused dispatch under CA-R-1525, retained original bindings, **and** recorded revalidation **before** continuation; silently selecting the new Revision **or** continuing an unvalidated old binding fails.
- provide valid revalidation for remaining work: resume **only** with its exact admitted bindings, current authorization, **and** compatible effects **and** inputs; completed Step Runs retain their original bindings **and** are **not** replayed.
- change a definition while an Action is **in** flight: follow the admitted interruption policy, retain its actual binding **and** result, **and** block subsequent dispatch **until** revalidation; do **not** force termination **or** repeat its effect merely because the definition changed.
- rebuild the execution view **after** restart: canonical Journal facts **must** remain its historical authority; predecessor completion alone **must not** appear as completed replacement.

pass **only** with evidence of retained request identity, correct Run associations, no duplicate successor effects, preserved retry allowance, **and** truthful outcomes. reuse the general App restart boundary under CA-E-352; no real Project Atom replacement is required for this fixture.
