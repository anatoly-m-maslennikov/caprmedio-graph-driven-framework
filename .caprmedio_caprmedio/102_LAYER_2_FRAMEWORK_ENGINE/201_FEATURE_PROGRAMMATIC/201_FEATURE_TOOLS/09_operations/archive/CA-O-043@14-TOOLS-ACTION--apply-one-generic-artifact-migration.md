---
cce_version: cce_1
cce_form: definition
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Storage
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
version: 14
updated_at: 2026-10-26 00:46:35 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-O-043@14
status: Archived
content_role: Operations
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Action
tier: 1
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
