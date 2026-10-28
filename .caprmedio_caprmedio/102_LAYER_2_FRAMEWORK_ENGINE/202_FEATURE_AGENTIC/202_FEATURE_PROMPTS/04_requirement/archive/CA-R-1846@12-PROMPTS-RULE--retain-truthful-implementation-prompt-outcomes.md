---
atom_id: CA-R-1846@12
content_role: Requirement
type: Rule
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Execution Control/Failure Handling
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History
relations: {}
tier: 3
---
# Summary

Retain truthful implementation prompt outcomes

## Scope

result and evidence returned by a current Implementation Workflow prompt.

## Claim

the Implementation **must** return only a result label admitted by its current Step plus actual outputs, input/source bindings, retained state, evidence references, and blockers; absent or unperformed checks never become a passing result.

## Details

An initial expected failing Evaluation consumes zero retries. Diagnosis, retry admission, repair, and renewed checking retain real state; a repair does not imply success. Method learning remains a separate CA-O-102 Workflow.
