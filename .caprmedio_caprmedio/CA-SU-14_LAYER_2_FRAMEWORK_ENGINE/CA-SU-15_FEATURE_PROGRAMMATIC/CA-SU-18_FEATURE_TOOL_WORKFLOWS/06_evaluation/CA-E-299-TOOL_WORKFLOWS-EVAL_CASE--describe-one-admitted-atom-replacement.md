---
atom_id: CA-E-299
ref_id: CA-E-299
container:
  scope_unit: CA-SU-18
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Header.Identity.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
tier: 4
relations:
  evaluation_for:
  - CA-R-1041
  - CA-O-031
  - CA-R-807
  derived_from:
  - CA-A-057
status: Active
version: 23
updated_at: 2026-10-27 19:59:32 +0400
carrier_destination:
  file:
    name: CA-E-299-TOOL_WORKFLOWS-EVAL_CASE--describe-one-admitted-atom-replacement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/06_evaluation
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
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
