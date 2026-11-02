---
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Engineering/Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
version: 30
updated_at: 2026-10-24 10:48:25 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1720@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Use one Project Journal for governed provenance

## Scope

CAPRMEDIO-governed provenance events in a Project.

## Claim

**every** Project **must** use **`=1`** authoritative Work Journal for **all** CAPRMEDIO-governed provenance events, including Artifact changes, Workflow Runs, Step Runs, Action executions, **and** Implementation lifecycle events. append supplied actual observations to that Project Journal and read them as recorded. each explicit append is an append, including repeated data; no canonical-once, deduplication, prior-history, chain, validation, receipt, retry or recovery prerequisite applies.

Existing Journal entries remain unchanged and readable without migration or synthetic baselines. The Journal is a log of supplied observations, not permission or proof of source, lifecycle, Run or Git correctness; it does not promise historical replay or recovery. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.

## Details

Runtime technical and business Journals may preserve their own operational histories in configured local or remote sinks. They are not additional Project Work Journals. Preserve actually supplied references without inventing canonical bindings. Distinct operational observations remain distinct facts under CA-R-1470; the Project Journal imposes no cross-log reconciliation or recording gate.
