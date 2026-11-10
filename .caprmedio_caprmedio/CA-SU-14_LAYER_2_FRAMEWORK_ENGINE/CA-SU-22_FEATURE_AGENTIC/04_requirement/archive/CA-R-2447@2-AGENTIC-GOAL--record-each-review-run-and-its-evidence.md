---
atom_id: CA-R-2447
ref_id: CA-R-2447@2
container:
  scope_unit: CA-SU-22
role: Requirement
form: Goal
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation/Traceability
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 3
status: Archived
version: 2
updated_at: 2026-10-30 03:53:02 +0400
current_scope_unit: AGENTIC
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-R-2447@2-AGENTIC-GOAL--record-each-review-run-and-its-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement/archive
---
## Summary

Record each review Run and its evidence

## Claim scope

evidence produced by the prompt Implementation for an Operator-authorized RMED Atoms Base Revise Run.

## Claim

The Implementation **must** provide a full traceable Run record, including partial, blocked, **and** empty Runs, through **both**:

- its Markdown report; **and**
- correlated shared Project Journal Records.

## Details

- The full report retains **all** of the following:
  - requested **and** selected scope;
  - source **and** rule bindings;
  - **all** per-Atom check evidence;
  - findings;
  - correction dispositions;
  - pending work;
  - blockers; **and**
  - actual outcome.
- The Journal records actual execution Events with the same Run ID **and** report reference. The report presents the saved review evidence; it does **not** establish another Journal **or** independently authored source of Events.
- Evidence-recording failures remain explicit alongside saved work. Successful checks **or** fixes do **not** prove that a report write **or** Journal append succeeded.
- The existing review Workflow owns the required operations. This Goal defines the evidence those operations must produce; it does not define another Workflow.
