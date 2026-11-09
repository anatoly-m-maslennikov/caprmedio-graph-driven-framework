---
atom_id: CA-O-043
ref_id: CA-O-043
container:
  scope_unit: CA-SU-16
role: Operations
form: Action
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
tier: 1
status: Active
version: 16
updated_at: 2026-10-27 19:59:44 +0400
cce_version: cce_1
cce_form: definition
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Apply one generic Artifact migration

Apply Generic Artifact Migration **means** the reusable Action that produces one complete approved generic Carrier-and-reference migration with its required attributable Journal evidence, **or** restoration of the complete prior mutable Carrier-and-reference state under CA-R-1139. its modeled boundary is the complete selected mutable-state transition; a partial application is **not** an independently accepted result.

## Applicable when

use this Action **when** one approved generic Artifact migration plan **must** be applied against its unchanged recorded preconditions.

## Action

1. resolve the approved migration plan **and** seal its plan digest, source preconditions, carrier mappings, **and** required reference mutations.
2. recheck **every** recorded precondition against the current source frontier **and** reject **any** changed, missing, **or** additional required source fact.
3. construct one transaction containing exactly the approved carrier **and** reference mutations; exclude unplanned effects.
4. apply the transaction rollbackably, appending the governed migration event through the Work Journal Tool **only** **after** **all** mutation effects succeed.
5. return the applied transaction identity **and** exact resulting frontier **without** interpreting it as a CAPRMEDIO Atom migration.

## Outcome

one approved unchanged generic Artifact migration is applied as one rollbackable carrier-**and**-reference transaction with attributable Work Journal evidence.

## Failure or stop

do **not** apply an unapproved **or** stale plan; roll back **every** carrier **and** reference mutation on **any** failed effect **or** Journal append failure.
