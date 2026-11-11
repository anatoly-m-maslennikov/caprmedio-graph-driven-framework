---
atom_id: CA-R-1720
ref_id: CA-R-1720@39
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Operations)/(.Header.Form: Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Operations)/(.Header.Form: Workflow)'
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
tier: 1
relations:
  child_of:
  - CA-R-007
status: archived
version: 39
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-1720@39-CORE_META_MODEL-RULE--use-one-project-journal-for-governed-provenance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
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
