---
version: 21
updated_at: 2026-10-27 19:59:44 +0400
relations:
  child_of:
  - CA-R-1487
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//PROJECT_PRIORITY_MODEL
atom_id: CA-O-022
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Resolve and activate Operator priorities

## Operation

Resolve Operator Priorities **means** the Action that turns applicable Operator input into the effective priority model for an identified Scope **and** Project stage.

### execution

1. identify the affected Scope **and** Project stage from the Operator input **and** its applicable context.
2. resolve the Operator-selected model, effective parameters, active criteria, applicable authority, **and** non-negotiable constraints. retain **every** applicable criterion **without** imposing a fixed catalog **or** comparison by priority order on another model.
3. check whether the input determines an admissible model **and** the parameters needed **to** apply it.
4. **if** that resolution succeeds, activate the resolved priorities **in** the CAPRMEDIO Framework Instance for the identified context **and** return them as the Action result.

### unresolved input

**if** the selected model, required parameters, authority, **or** context remains unresolved:

- present the known input **and** the exact unresolved point **to** the Operator.
- do **not** invent a model, infer a missing preference, **or** activate an unresolved change.
- report the Action as unresolved, **not** successfully completed.

## Details
