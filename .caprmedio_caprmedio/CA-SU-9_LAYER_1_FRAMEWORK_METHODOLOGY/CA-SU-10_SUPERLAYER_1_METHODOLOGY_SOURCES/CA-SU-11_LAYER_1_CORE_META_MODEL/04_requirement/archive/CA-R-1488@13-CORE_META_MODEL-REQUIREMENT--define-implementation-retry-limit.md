---
version: 13
updated_at: 2026-10-24 00:51:05 +0400
relations: {}
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run.Implementation Retry Limit
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Implementation Retry Control'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
atom_id: CA-R-1488@13
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Define Implementation Retry Limit

## Scope

Implementation Retry Limit values in an Implementation Workflow Run.

## Claim

Implementation Retry Limit **means** the maximum number of additional fix-and-evaluate rounds permitted **after** the initial failed Evaluation **in** one Implementation Workflow Run.

- its value **must** be an integer **`>=0`**.
- a value **`=0`** permits no retry **after** the initial failure.
- the limit does **not** grant permission **to** repair, change authority, **or** bypass an applicable confidence threshold.

## Details
