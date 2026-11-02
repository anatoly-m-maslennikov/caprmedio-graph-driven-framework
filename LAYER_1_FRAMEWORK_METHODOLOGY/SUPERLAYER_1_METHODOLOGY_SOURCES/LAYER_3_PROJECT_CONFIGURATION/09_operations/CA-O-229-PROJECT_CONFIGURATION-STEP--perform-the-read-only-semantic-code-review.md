---
atom_id: "CA-O-229"
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
    - "CA-O-225"
    - "CA-M-402"
    - "CA-M-411"
    - "CA-M-396"
    - "CA-M-397"
    - "CA-M-398"
    - "CA-M-399"
    - "CA-M-400"
    - "CA-E-389"
    - "CA-E-539"
    - "CA-E-540"
    - "CA-D-638"
---
# Summary

Perform the read-only semantic code review

## Operation

This Step invokes CA-O-225 in Isolated context only when that context is admitted. Bind candidate, owned paths, all actual Evaluation/diagnosis results, selected Plan or actual admitted in-session P/task with instruction/Definition of Done/source context, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project Principles, permissions, allowed commands, source revisions/hashes, report, and Run ID. An optional legacy `method_projection` may accompany direct rows but is not required.

Check evidence coverage and selected Method-policy compliance without restating policy. Map `implementation_defect` and `test_implementation_defect` to completed `findings`; map `authority_change_required`, `environment_blocker`, and `unresolved` to `unresolved` with actual results retained; report `expected_initial_failure` as an expected-phase observation and never accept the candidate unless admitted expected-phase criteria genuinely hold. Return `passed`, completed `findings`, `partial`, or `unresolved` according to CA-O-225.

## Details

No auto-fix, source/Atom edit, expected-result edit, retry, promotion, release, or Journal-completeness gate. Temporary fixture writes require explicit permission.
