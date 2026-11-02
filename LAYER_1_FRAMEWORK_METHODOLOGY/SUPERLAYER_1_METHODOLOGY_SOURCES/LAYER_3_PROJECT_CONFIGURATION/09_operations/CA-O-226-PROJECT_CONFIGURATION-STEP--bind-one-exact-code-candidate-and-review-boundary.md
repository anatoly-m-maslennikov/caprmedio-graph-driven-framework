---
atom_id: "CA-O-226"
content_role: "Operations"
type: "Step"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
author: "Anatoly Maslennikov"
status: "Active"
version: 3
updated_at: "2026-10-22T21:21:30+04:00"
global_tier: 11
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step"
  depends_on:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
    - "Entity/Node/Continuant/Atom/Content Role: Method"
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
    - "Entity/Node/Continuant/Atom/Content Role: Delivery"
    - "Entity/Node/Continuant/Implementation"
    - "Entity/Carrier"
    - "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action"
    - "Entity/Node/Occurrent/Execution/Step Run"
    - "Entity/Node/Occurrent/Execution/Workflow Run"
relations:
  relates_to:
    - "CA-O-223"
    - "CA-O-224"
    - "CA-R-1515"
    - "CA-M-404"
    - "CA-M-395"
---
# Summary

Bind one exact code candidate and review boundary

## Operation

This Step invokes CA-O-224 in Integrated context. Bind candidate digest, owned paths, either an existing Plan or an actually admitted in-session P/task with instruction, Definition of Done, and source context, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project Principles, permissions, allowed commands, context authority, source revisions/hashes, report, and Run ID. An optional legacy `method_projection` may accompany direct rows but is not required.

Return the Action's `bound` or `blocked` result unchanged. Missing Plan/P-task content is blocked. No hidden next Step, retry, candidate substitution, Plan fabrication, or source edit.

## Details

The Step performs boundary inspection only and has no mutation authority.
