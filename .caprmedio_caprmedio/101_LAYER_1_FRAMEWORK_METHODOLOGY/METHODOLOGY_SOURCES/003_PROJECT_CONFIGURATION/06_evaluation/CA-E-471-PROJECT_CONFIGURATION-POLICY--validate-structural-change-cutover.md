---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
version: 20
updated_at: 2026-10-27 19:59:35 +0400
relations:
  evaluation_for:
  - CA-O-012
  - CA-O-013
  - CA-O-014
  - CA-O-015
atom_id: CA-E-471
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 4
---
# Summary
Validate structural change cutover

## Scope
structural changes **and** no-change repeats, including create, rename, reparent, reorder, rebind, reconciliation, **and** declaration removal.

## Claim

the Evaluation **must** fail a structural change **if** it:

- starts from stale declarations;
- exceeds authorization;
- bypasses the effective confidence gate;
- loses a Goal **or** reference;
- violates post-change consistency;
- changes another Project;
- silently overwrites concurrent changes; **or**
- reports completion **after** partial failure.

test the following groups:

- create, rename, reparent, reorder, rebind, reconciliation **and** declaration removal against their exact before/after states;
- rejection, invalid proposal, stale-state failure, injected apply failure **and** authorized recovery.

the following conditions also apply:

- a no-change repeat **must** preserve authority bytes **and** have no additional structural effects.
- declaration removal **must not** delete a folder **unless** that exact deletion is authorized.
- a missing structural Projection **must not** prevent an **otherwise** valid change.

## Details
