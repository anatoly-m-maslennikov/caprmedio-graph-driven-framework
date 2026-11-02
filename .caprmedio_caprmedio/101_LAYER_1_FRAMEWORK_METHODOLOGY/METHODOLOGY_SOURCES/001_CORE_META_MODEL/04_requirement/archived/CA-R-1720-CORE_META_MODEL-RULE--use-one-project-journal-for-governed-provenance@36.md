---
subjects:
  governs: Entity/Object/Continuant/History/Journal
  depends_on:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Term//Artifact
  - Entity/Object/Continuant/Package/Project Implementation
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Entity/Object/Continuant/History/Journal > Event Record
  - Entity/Object/Continuant/Projection
  - Entity/Carrier
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
version: 36
updated_at: 2026-10-29 07:45:27 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1720
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Use one Project Journal for governed provenance

## Claim scope

CAPRMEDIO-governed provenance events in a Project.

## Claim

**every** Project **must** use **`=1`** authoritative Work Journal for **all** CAPRMEDIO-governed provenance events, including Artifact changes, Workflow Runs, Step Runs, Action executions, **and** Implementation lifecycle events. append supplied actual observations to that Project Journal and read them as recorded. each explicit append is an append, including repeated data; no canonical-once, deduplication, prior-history, chain, validation, receipt, retry or recovery prerequisite applies.

Existing Journal entries remain unchanged and readable without migration or synthetic baselines. The Journal is a log of supplied observations, not permission or proof of source, lifecycle, Run or Git correctness; it does not promise historical replay or recovery. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.

## Details

Runtime technical and business Journals may preserve their own operational histories in configured local or remote sinks. They are not additional Project Work Journals. Preserve actually supplied references without inventing canonical bindings. Distinct operational observations remain distinct facts under CA-R-1470; the Project Journal imposes no cross-log reconciliation or recording gate.
