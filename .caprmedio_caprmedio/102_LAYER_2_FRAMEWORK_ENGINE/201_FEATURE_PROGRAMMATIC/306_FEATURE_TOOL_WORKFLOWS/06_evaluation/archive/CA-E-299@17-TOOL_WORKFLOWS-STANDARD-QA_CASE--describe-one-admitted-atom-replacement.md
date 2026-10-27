---
atom_id: CA-E-299@17
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Validate And Describe Atom Replacement
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.ID
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
version: 17
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-R-1041
  - CA-O-031
  - CA-R-807
  derived_from:
  - CA-A-057
tier: 4
---
# Summary

Describe one admitted Atom replacement

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

CA-O-031's mutation-free description of one predecessor replacement and independent replacement descriptions under CA-M-372.

## Claim

The description preserves the exact predecessor and explicit proposed or admitted successor set, with currentness and permission evidence. It does not turn a description into an applied replacement or one cross-Atom transaction.

## Details

### Required test cases

- Describe one exact predecessor and one explicit fresh-ID successor proposal. Separately retain the complete already-active successor set where the governing replacement rules admit it; no pair-only normalization drops an admitted successor.
- Change the Summary only by wording. Verify the description requires a new Atom ID and predecessor archival; ordinary same-ID Modify is rejected even when the Claim is unchanged.
- Reject missing, unresolved, inactive, duplicate, self-referential, stale or unadmitted existing successor evidence. A proposal is not falsely reported as an existing active Atom.
- For several predecessor mappings, describe each independent action in order. On the first failure, retain earlier descriptions, leave later mappings unperformed and invent no transactional batch or application.
- Independently check the example target 100, created 200 and archived 100. Before application, created and archived remain proposed, not observed effects. Incoming references to 100 are listed or discoverable but never automatically rewritten.

### Acceptance criteria

Descriptions are mutation-free and distinguish proposed from observed identities. Every mapping preserves the explicit predecessor/successor inputs and its own admission boundary. Application needs separately current sealed authorization; the description's permission does not authorize a new action. Resume/retry of the new workflow family remains deferred.

### Failure disposition

Reject lost or invented IDs, changed mappings, false effect/completion claims, implicit reference rewrites or cross-Atom rollback guarantees. Retain the exact descriptions and source-state evidence. These cases specify later checks and record no observed pass.
