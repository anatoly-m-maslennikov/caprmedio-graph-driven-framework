---
atom_id: CA-E-566
ref_id: CA-E-566
container:
  scope_unit: CA-SU-24
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control <+ Failure Handling
  dependencies:
  - MODEL//CAPRMEDIO <+ Execution/Workflow Run
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Evaluation)
  - MODEL//CAPRMEDIO <+ Journal
tier: 3
status: Active
version: 12
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-E-566-PROMPTS-EVAL_CASE--verify-implementation-prompt-truthful-retry-and-repair-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/06_evaluation
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---

## Summary

Verify implementation prompt truthful retry and repair results

## Claim

### Prose Claim

the Implementation passes this Evaluation only when it preserves initial failure evidence, counts retries truthfully, blocks unadmitted repair, and never labels repaired or unperformed work as passed.

## Details

### Scope

diagnosis, retry admission, repair, and renewed checking prompts.

Method learning is excluded from this Implementation Workflow case and remains separately initiated under CA-O-102.
