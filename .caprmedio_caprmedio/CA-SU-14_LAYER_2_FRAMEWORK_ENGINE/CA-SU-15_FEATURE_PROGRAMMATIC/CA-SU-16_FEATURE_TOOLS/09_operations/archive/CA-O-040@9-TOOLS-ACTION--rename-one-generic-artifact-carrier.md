---
cce_version: cce_1
cce_form: definition
subjects:
  governs: Rename Generic Artifact Carrier
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Artifact
  - Subject/Engineering/Carrier
  - Artifact/Revision
  - Subject/Graph/Relation
version: 9
updated_at: 2026-10-24 01:28:26 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-O-040@9
status: Archived
content_role: Operations
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Action
---
# Rename one generic Artifact carrier

Rename Generic Artifact Carrier **means** the reusable Action that produces one complete authorized generic Carrier rename with its required canonical-reference rewrites, **or** restoration of the complete prior mutable state under CA-R-1133. its modeled boundary is the complete selected mutable-state transition; a partial application is **not** an independently accepted result.

## Applicable when

use this Action **when** one generic Artifact carrier requires a filename change under the active generic filename grammar.

## Action

1. resolve the exact source carrier, current identity, **and** requested target filename, **then** validate the target against the active grammar.
2. preflight the target path **and** reject **every** collision, unresolved canonical reference, **or** unavailable source carrier.
3. discover **every** current mutable governed canonical reference that **must** change **and** construct the complete old-to-new identity mapping. preserve accepted Journal Records **and** exact historical Revisions; their observed old identity is historical evidence, **not** a current reference **to** rewrite under CA-R-1491.
4. expose one dry-run containing the rename, mapping, **and** **all** required reference rewrites.
5. on authorized apply, perform the rename **and** **every** required rewrite as one rollbackable transaction, **then** verify that no required current mutable governed reference retains the old identity.

## Outcome

one generic Artifact carrier has a grammar-valid new name, an attributable identity mapping, **and** fully rewritten governed canonical references.

## Failure or stop

stop **or** roll back on an invalid filename, collision, stale source, incomplete rewrite set, **or** failed required rewrite; do **not** use this helper as an Atom move operation.
