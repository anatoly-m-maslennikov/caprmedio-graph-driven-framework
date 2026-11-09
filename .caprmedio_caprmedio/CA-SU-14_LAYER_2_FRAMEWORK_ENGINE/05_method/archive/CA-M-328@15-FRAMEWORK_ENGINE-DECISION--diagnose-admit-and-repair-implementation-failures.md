---
atom_id: CA-M-328@15
ref_id: CA-M-328@15
container:
  scope_unit: CA-SU-14
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Failure
    Handling
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Retry
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
tier: 3
status: Archived
version: 15
updated_at: 2026-11-09 14:41:40 +0400
carrier_destination:
  file:
    name: CA-M-328@15-FRAMEWORK_ENGINE-DECISION--diagnose-admit-and-repair-implementation-failures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/archive
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
---

## Summary

Diagnose, admit, and repair implementation failures

## Claim

### Prose Claim

**to** handle a failure, retain the actual failing evidence, diagnose its category, admit retry only through current permission/confidence/retry guards, repair the admitted defect, and return for renewed preparation or checking.

## Details

### Scope

the diagnosed repair path after a selected Implementation Workflow check does not pass.

Changed failures, stale evidence, unavailable authority, or non-progressing work block. Repair preserves issue evidence and does not create or promote an M atom.
