---
atom_id: CA-O-224@4
content_role: "Operations"
type: "Action"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
author: "Anatoly Maslennikov"
status: Archived
version: 4
updated_at: 2026-10-23 03:06:32 +0400
global_tier: 11
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Node/Continuant/Implementation
  - Entity/Carrier
  - 'Entity/Node/Continuant/Actor/Type: Operator'
relations:
  relates_to:
    - "CA-R-1515"
    - "CA-M-404"
    - "CA-M-417"
    - "CA-M-395"
    - "CA-M-401"
    - "CA-D-251"
    - "CA-D-638"
---
# Summary

Bind the exact code candidate and bounded review context

## Operation

Code Candidate Review Binding means the read-only Action that freezes the review boundary before checks run. Required initiative input is either an existing bounded Plan or an actually admitted in-session P/task with instruction, Definition of Done, and source context. Required review inputs also include candidate digest, owned paths, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project Principles, permissions, allowed commands, context authority, report destination, Run identity, source revisions/hashes, and prior evidence. An optional legacy `method_projection` may accompany direct rows but is not required.

Return `bound` only when the selected Plan or in-session P/task is real, complete, current, and sufficient for downstream CA-O-020/CA-O-089. Return `blocked` when it is absent, stale, ambiguous, or missing required content. Never invent a Plan Atom ID, create a Plan artifact, substitute a target, widen permissions, or use a remembered projection.

## Details

This Action inspects only the candidate and boundary metadata. It does not execute checks, edit code, change expectations or Atoms, write a Journal event, publish MCP, or choose a hidden next Step.
