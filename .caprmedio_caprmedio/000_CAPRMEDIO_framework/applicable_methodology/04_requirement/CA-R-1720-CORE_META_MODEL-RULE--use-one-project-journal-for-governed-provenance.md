---
subjects:
  active: Journal
  passive:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - Project
  - Term//Artifact
  - Entity/Object/Continuant/Package/Project Implementation
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Operations)/(.Type: Action)'
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Operations)/(.Type: Workflow)'
  - Entity/Object/Continuant/History/Journal <+ Event Record
  - Projection
  - Carrier
  - Atom/(.Role := Delivery)
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1720-CORE_META_MODEL-RULE--use-one-project-journal-for-governed-provenance.md
  source_atom_id: CA-R-1720
  source_atom_revision: 38
  source_sha256: cac82b49fc8bf208483d722df302eb98b0a270ef89658fdf4e1af6dba7286a82
  original_relations_sha256: edef9085fddd1e905afd02423e8d88f5300a99b1f0a711703db5055e0c42a859
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
