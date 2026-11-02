---
atom_id: CA-R-2447@1
content_role: Requirement
current_scope_unit: AGENTIC
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: 2026-10-30 03:11:57 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation/Traceability
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
relations: {}
tier: 3
type: Goal
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
- this Goal describes the review evidence. Recording steps belong to the existing review Workflow, not another Workflow.
