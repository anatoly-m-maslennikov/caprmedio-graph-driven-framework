---
atom_id: CA-M-328
ref_id: CA-M-328
container:
  scope_unit: CA-SU-14
role: Method
form: Direct Policy
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Failure Handling
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Evaluation)
  - MODEL//CAPRMEDIO <+ Execution/Workflow Run
  - MODEL//CAPRMEDIO <+ Journal
tier: 3
status: Active
version: 17
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-M-328-FRAMEWORK_ENGINE-DIRECT_POLICY--diagnose-admit-and-repair-implementation-failures.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
---

## Summary

Diagnose, admit, and repair implementation failures

## Claim

### Prose Claim

**to** handle a failure, retain failing evidence, diagnose its category, admit retry only through current permission, confidence and retry guards, repair the admitted defect, and return for renewed preparation or checking.

## Details

### Scope

the diagnosed repair path after a selected Implementation Workflow check does not pass.

Changed failures, stale evidence, unavailable authority or non-progressing work block. Repair preserves issue evidence and does not create or promote an M atom.
