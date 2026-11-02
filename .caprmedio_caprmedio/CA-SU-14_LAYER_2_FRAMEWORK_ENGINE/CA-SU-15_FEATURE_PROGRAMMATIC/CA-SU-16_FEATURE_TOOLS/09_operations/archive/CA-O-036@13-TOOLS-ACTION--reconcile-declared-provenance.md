---
cce_version: cce_1
cce_form: definition
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Reconcile Declared Provenance'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Artifact/Revision
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
version: 13
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-O-036@13
status: Archived
content_role: Operations
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Action
tier: 1
---
# Reconcile declared provenance

Reconcile Declared Provenance **means** the reusable Action that produces a complete read-only reconciliation of the selected declared provenance **without** inferring repair **or** adoption under CA-R-1146. its modeled boundary is the complete requested result; partial comparison, incomplete attribution, **or** an unreported unresolved input is **not** an independently successful outcome.

## Applicable when

use this Action **when** selected Artifacts require a read-only comparison of their declared source, draft, session, revision, **and** content-digest provenance.

## Action

1. resolve the selected Artifacts **and** their declared provenance fields **without** modifying carriers **or** following undeclared inferences.
2. compare **every** declared source, draft, session, revision, **and** content digest with the referenced current carrier **or** recorded value.
3. classify **every** link as current, missing, conflicting, stale, **or** unverifiable **and** retain the exact observed evidence.
4. attribute **every** finding **to** its source Artifact, declared field, target reference, **and** observed digest **or** revision.
5. return the reconciliation result **without** creating authority, repairing provenance, **or** deciding semantic adoption.

## Outcome

one read-only provenance reconciliation result reports **every** current, missing, conflicting, stale, **or** unverifiable declared link **in** the selected scope.

## Failure or stop

do **not** mutate Artifacts **or** infer provenance; return an explicit unresolved result **when** a selected Artifact **or** declared target cannot be read.
