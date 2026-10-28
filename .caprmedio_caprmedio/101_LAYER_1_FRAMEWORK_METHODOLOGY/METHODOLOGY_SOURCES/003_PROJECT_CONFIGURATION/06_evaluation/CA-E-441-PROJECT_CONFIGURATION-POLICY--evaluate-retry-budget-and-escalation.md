---
version: 28
updated_at: 2026-10-27 19:59:35 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-O-024
  - CA-O-016
  - CA-R-1559
  - CA-M-295
subjects:
  governs: Subject/caprmedio/Action//Implementation Retry Control
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Implementation Retry Limit
atom_id: CA-E-441
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 6
---
# Summary

Evaluate retry budget **and** escalation

## Scope

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

## Details
