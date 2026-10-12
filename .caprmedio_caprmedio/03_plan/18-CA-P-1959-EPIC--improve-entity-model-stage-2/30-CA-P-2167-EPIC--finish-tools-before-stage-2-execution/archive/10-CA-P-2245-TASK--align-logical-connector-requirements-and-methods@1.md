---
atom_id: CA-P-2245
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Scope Unit, Workflow, Configuration, Plan, Operator]
version: 1
updated_at: "2026-10-12 23:10:03 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Align logical connector Requirements and Methods

## Objective

The affected Tool Requirements and Methods express the approved logical connector and Workflow behavior without stale cross-Atom transaction or indexed-list assumptions.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Use CA-P-2167's prospective rebuild decisions and the actual existing declared Engine authority roots. Exclusive source scope: the Root-assigned Requirements/Methods packet, including new CA-R-1933–1935 for shared section edits, property edits and TOML, new CA-M-372–375, and the affected existing Requirements/Methods. Other workers own Evaluation/Delivery and Operations. Serialize any overlapping existing carrier with its assigned owner; do not create a new Scope Unit or edit code/Core/migration/projections.

Require logical storage-neutral connectors with file/database details private. Keep Find, Read and Modify independent generally, including independent findWorkflow/modifyWorkflow. Include createAtom and createSU; no Atom deletion, only archive. Any Summary change requires a fresh ID plus predecessor archival, and the property Tool rejects it as a same-ID update. Replacement reports target/created/archived IDs without automatic reference retargeting.

Bind the shared section-edit family to add/replace/remove/title-rename/order. Property-list edits use one item by VALUE, never index, or full-set replacement; add/remove are approved. The shared TOML connector has distinct Project Structure/Project Settings Workflows with their respective schema checks. Subject search uses governs/depends_on, scope and exact/prefix/suffix/contains matching.

Each Atom action is independent: stop a multiple-action request on its first failure, retain earlier successful actions and leave the remaining targets untouched. Reject cross-Atom all-or-nothing rollback while retaining one-Atom safety, exact currentness/authorization and truthful effects/recording. Resume/retry and the older concurrent-publication design remain deferred; do not invent either mechanism.

Preserve established Summary/ID and current filenames for admitted same-identity semantic revisions, Version +1, actual offset timestamp and exact predecessor archives. A required Summary change follows replacement identity rules, not a same-ID repair. Deliver complete current/predecessor source pins and declared semantic deltas to CA-P-2248; the author does not accept their own packet. Historical receipts remain frozen and do not establish new-design readiness. This Task remains Active until actual independent acceptance; split a concrete overrun before execution.

### Definition of Done

The Plan is **not** Done if an affected contract retains conflicting assumptions, current/predecessor pins or exact history are missing, independent source acceptance is absent, one-Atom safeguards weaken, deferred policies are silently chosen, forbidden surfaces change, source authoring is reported as implementation/live capability, or own work exceeds 15 minutes without decomposition.
