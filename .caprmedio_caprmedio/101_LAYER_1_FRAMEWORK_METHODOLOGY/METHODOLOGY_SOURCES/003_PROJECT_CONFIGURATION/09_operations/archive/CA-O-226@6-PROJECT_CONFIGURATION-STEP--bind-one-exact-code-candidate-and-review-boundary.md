---
atom_id: CA-O-226@6
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
version: 6
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Node/Continuant/Implementation
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
relations:
  relates_to:
  - CA-O-223
  - CA-O-224
  - CA-R-1515
  - CA-M-404
  - CA-M-395
tier: 3
---
# Summary

Bind one exact code candidate and review boundary

## Operation

This Step invokes CA-O-224 in Integrated context. Bind candidate digest, owned paths, either an existing Plan or an actually admitted in-session P/task with instruction, Definition of Done, and source context, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project Principles, permissions, allowed commands, context authority, source revisions/hashes, report, and Run ID. An optional legacy `method_projection` may accompany direct rows but is not required.

Return the Action's `bound` or `blocked` result unchanged. Missing Plan/P-task content is blocked. No hidden next Step, retry, candidate substitution, Plan fabrication, or source edit.

## Details

The Step performs boundary inspection only and has no mutation authority.
