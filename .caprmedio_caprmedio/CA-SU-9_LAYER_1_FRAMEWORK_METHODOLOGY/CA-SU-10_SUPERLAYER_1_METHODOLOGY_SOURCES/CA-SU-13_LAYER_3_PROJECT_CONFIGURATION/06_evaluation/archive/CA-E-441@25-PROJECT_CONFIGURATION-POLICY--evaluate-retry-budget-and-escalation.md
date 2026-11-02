---
version: 25
updated_at: 2026-10-25 15:37:17 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-O-024
  - CA-O-016
  - CA-R-1559
  - CA-M-295
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Implementation Retry Control'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Subject/Engineering/Operation-Local Failure Containment
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run.Implementation Retry Limit
atom_id: CA-E-441@25
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
