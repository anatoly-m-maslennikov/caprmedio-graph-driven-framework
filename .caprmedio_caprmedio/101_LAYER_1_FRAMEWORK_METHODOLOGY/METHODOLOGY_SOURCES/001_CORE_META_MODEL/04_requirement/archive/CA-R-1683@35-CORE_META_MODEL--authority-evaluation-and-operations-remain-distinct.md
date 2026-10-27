---
subjects:
  governs: Subject/Graph/Rule
  depends_on:
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/History
  - Subject/Engineering/Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Actor
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Verification
version: 35
updated_at: 2026-10-24 10:48:25 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1683@35
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Authority, Evaluation, and Operations remain distinct

## Scope

RMED Spec authority, CAPO Change content, concrete Implementation, actual executions, Verification judgments.

## Claim

CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549, including specific reusable Operations definitions under CA-R-1530; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but **must not** themselves establish, edit, replace, **or** override semantic authority.

## Details
