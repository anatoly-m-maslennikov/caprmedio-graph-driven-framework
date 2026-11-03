---
subjects:
  active: CAPRMEDIO_MODEL <+ Journal
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Operations)/(.Header.Form: Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Operations)/(.Header.Form: Workflow)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal <+ Event Record
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
version: 38
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1720
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Use one Project Journal for governed provenance

## Claim

### Prose Claim


CAPRMEDIO-governed provenance events in a Project.


**every** Project **must** use **`=1`** authoritative Work Journal for **all** CAPRMEDIO-governed provenance events, including Artifact changes, Workflow Runs, Step Runs, Action executions, **and** Implementation lifecycle events. append supplied actual observations to that Project Journal and read them as recorded. each explicit append is an append, including repeated data; no canonical-once, deduplication, prior-history, chain, validation, receipt, retry or recovery prerequisite applies.

Existing Journal entries remain unchanged and readable without migration or synthetic baselines. The Journal is a log of supplied observations, not permission or proof of source, lifecycle, Run or Git correctness; it does not promise historical replay or recovery. its logical event table does **not** require **`=1`** physical file **or** a database table; Carrier representation remains governed by Delivery authority.

## Details

Runtime technical and business Journals may preserve their own operational histories in configured local or remote sinks. They are not additional Project Work Journals. Preserve actually supplied references without inventing canonical bindings. Distinct operational observations remain distinct facts under CA-R-1470; the Project Journal imposes no cross-log reconciliation or recording gate.
