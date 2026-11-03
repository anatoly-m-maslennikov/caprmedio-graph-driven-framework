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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-022-PROJECT_CONFIGURATION-ACTION--resolve-and-activate-operator-priorities.md
  source_atom_id: CA-O-022
  source_atom_revision: 21
  source_sha256: 7aa00d35c4a202ca7e1e63605515156580a34e7ef08b6440dd1aceac70489b23
  original_relations_sha256: 2cccfab5f9eb53e0f786c8f141ca6d892cd6285d32a2aceff4e7a46010d8ba97
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
