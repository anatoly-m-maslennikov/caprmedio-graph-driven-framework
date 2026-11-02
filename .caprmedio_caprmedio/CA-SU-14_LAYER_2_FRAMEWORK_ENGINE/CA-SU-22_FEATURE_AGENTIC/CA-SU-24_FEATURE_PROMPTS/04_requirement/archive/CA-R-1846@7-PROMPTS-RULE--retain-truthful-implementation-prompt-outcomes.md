---
atom_id: CA-R-1846@7
content_role: Requirement
type: Rule
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Engineering/Implementation prompt outcomes
  depends_on:
  - Subject/Engineering/Prompt
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Evidence
relations:
  relates_to:
  - CA-O-016
  - CA-O-020
  - CA-O-024
  - CA-O-089
  - CA-O-021
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
