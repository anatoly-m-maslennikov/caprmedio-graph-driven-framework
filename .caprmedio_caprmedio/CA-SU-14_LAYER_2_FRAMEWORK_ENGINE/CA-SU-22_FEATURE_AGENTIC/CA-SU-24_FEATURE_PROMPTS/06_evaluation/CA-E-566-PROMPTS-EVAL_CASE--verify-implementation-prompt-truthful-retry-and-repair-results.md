---
atom_id: CA-E-566
ref_id: CA-E-566
role: Evaluation
form: Eval Case
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-27 19:59:37 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Retry and Repair Results
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Retry
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
tier: 3
container:
  scope_unit: CA-SU-24
carrier_destination:
  file:
    name: CA-E-566-PROMPTS-EVAL_CASE--verify-implementation-prompt-truthful-retry-and-repair-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/06_evaluation
---
# Summary

Verify implementation prompt truthful retry and repair results

## Scope

diagnosis, retry admission, repair, and renewed checking prompts.

## Claim

the Implementation passes this Evaluation only when it preserves initial failure evidence, counts retries truthfully, blocks unadmitted repair, and never labels repaired or unperformed work as passed.

## Details

Method learning is excluded from this Implementation Workflow case and remains separately initiated under CA-O-102.
