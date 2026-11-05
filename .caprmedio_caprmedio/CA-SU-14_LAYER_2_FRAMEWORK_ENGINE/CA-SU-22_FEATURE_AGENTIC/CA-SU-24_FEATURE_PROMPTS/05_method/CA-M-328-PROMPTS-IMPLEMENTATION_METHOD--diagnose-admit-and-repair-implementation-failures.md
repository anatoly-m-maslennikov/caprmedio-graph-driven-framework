---
atom_id: CA-M-328
ref_id: CA-M-328
role: Method
form: Implementation Method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 19:59:42 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Retry
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
tier: 3
container:
  scope_unit: CA-SU-24
carrier_destination:
  file:
    name: CA-M-328-PROMPTS-IMPLEMENTATION_METHOD--diagnose-admit-and-repair-implementation-failures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/05_method
---
# Summary

Diagnose, admit, and repair implementation failures

## Scope

the diagnosed repair path after a selected Implementation Workflow check does not pass.

## Claim

**to** handle a failure, retain the actual failing evidence, diagnose its category, admit retry only through current permission/confidence/retry guards, repair the admitted defect, and return for renewed preparation or checking.

## Details

Changed failures, stale evidence, unavailable authority, or non-progressing work block. Repair preserves issue evidence and does not create or promote an M atom.
