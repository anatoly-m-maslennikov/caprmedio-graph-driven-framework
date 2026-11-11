---
atom_id: CA-R-2447
ref_id: CA-R-2447
container:
  scope_unit: CA-SU-22
role: Requirement
form: Goal
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation <+ Traceability
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Workflow
  - MODEL//CAPRMEDIO <+ Atom
  - MODEL//CAPRMEDIO <+ Journal
  - MODEL//CAPRMEDIO <+ Event Record
  - MODEL//CAPRMEDIO <+ Actor/Operator
tier: 3
status: Active
version: 3
updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: AGENTIC
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-2447-AGENTIC-GOAL--record-each-review-run-and-its-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement
---
## Summary

Record each review Run and its evidence

## Claim scope

evidence produced by the prompt Implementation for an Operator-authorized RMED Atoms Base Revise Run.

## Claim


### Prose Claim
The Implementation **must** provide a traceable record for every Run, including partial, blocked, **and** empty Runs, through **both**:

- its Markdown report; **and**
- correlated shared Project Journal Records.

## Details

- The report retains requested **and** selected scope, source **and** rule bindings, **all** per-Atom check evidence, findings, correction dispositions, pending work, blockers, **and** actual outcome.
- The Journal records actual execution Events with the same Run ID **and** report reference. The report presents saved review evidence; it does **not** establish another Journal **or** independently authored Event source.
- Evidence-recording failures remain explicit. Successful checks **or** fixes do **not** prove that a report write **or** Journal append succeeded.
- The existing review Workflow owns the required operations. This Goal defines their required evidence; it does not define another Workflow.
