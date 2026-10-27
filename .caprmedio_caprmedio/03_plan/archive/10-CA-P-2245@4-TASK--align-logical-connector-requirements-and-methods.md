---
atom_id: CA-P-2245@4
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
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Scope Unit
  - Workflow
  - Configuration
  - Plan
  - Operator
version: 4
updated_at: 2026-10-23 23:03:23 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
---
# Summary

Align logical connector Requirements and Methods

## Objective

The affected Tool Requirements and Methods express the approved logical connector and Workflow behavior without stale cross-Atom transaction or indexed-list assumptions.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Use CA-P-2167's prospective rebuild decisions and the approved CONNECTOR_TOOLS/TOOL_WORKFLOWS FEATURE authority roots. Exclusive source scope: the Root-assigned Requirements/Methods packet, including new CA-R-1933–1935 for shared section edits, property edits and TOML, new CA-M-372–376, common Connector Core CA-R-1936, and the affected existing Requirements/Methods. Other workers own Evaluation/Delivery and Operations. Serialize any overlapping existing carrier with its assigned owner; Root alone declares the two approved FEATURE Scope Units; do not create any other Scope Unit or edit code/CORE_META_MODEL/migration/projections.

The Operator approved the two FEATURE siblings CONNECTOR_TOOLS and TOOL_WORKFLOWS under PROGRAMMATIC (Level 3, navigation 5/6), with flat role folders and shared Core policies inside each. Root alone updates Project Structure; only rebuilt RMEDO moves to `305_FEATURE_CONNECTOR_TOOLS`/`306_FEATURE_TOOL_WORKFLOWS`. Their future `305_CONNECTOR_TOOLS`/`306_TOOL_WORKFLOWS` delivery roots remain unmaterialized; existing TOOLS, unrelated legacy authority, existing delivery bindings and code paths stay unchanged. This approval supersedes the prior prospective no-new-Scope-Unit restriction for exactly this split.

Require logical storage-neutral connectors with file/database details private. Keep Find, Read and Modify independent generally, including independent findWorkflow/modifyWorkflow. Include createAtom and createSU; no Atom deletion, only archive. Any Summary change requires a fresh ID plus predecessor archival, and the property Tool rejects it as a same-ID update. Replacement reports target/created/archived IDs without automatic reference retargeting.

Connector Core CA-R-1936/CA-M-376/CA-E-628/CA-D-625 must supply a coherent broad logical API across ALL connector Tools: common input/result/precondition/error/effect contracts, not a new transport, database or retry design. Workflow Core policies remain separate. Actual code work must explicitly address hardcoded authority paths, release/admission bindings, selected-execution refresh/seals/pins and the graph generator's incorrect delivery derivation, with legacy Core/content alignment and independent runtime/admission/fixture gates retained. New source ownership or a matching receipt does not make existing code compatible, and successful source authoring grants no live readiness.

Author the common logical input/result/precondition/error/effect contract in Connector Core CA-R-1936/CA-M-376 for ALL connector Tools. Retain operation-specific refinements and independent connector operations; align shared Workflow policies at Core in TOOL_WORKFLOWS, including affected CA-R-1093. This is not a new transport/API server or another retry policy.

Bind the shared section-edit family to add/replace/remove/title-rename/order. Property-list edits use one item by VALUE, never index, or full-set replacement; add/remove are approved. The shared TOML connector has distinct Project Structure/Project Settings Workflows with their respective schema checks. Subject search uses governs/depends_on, scope and exact/prefix/suffix/contains matching.

Each Atom action is independent: stop a multiple-action request on its first failure, retain earlier successful actions and leave the remaining targets untouched. Reject cross-Atom all-or-nothing rollback while retaining one-Atom safety, exact currentness/authorization and truthful effects/recording. Resume/retry and the older concurrent-publication design remain deferred; do not invent either mechanism.

Preserve established Summary/ID and current filenames for admitted same-identity semantic revisions, Version +1, actual offset timestamp and exact predecessor archives. A required Summary change follows replacement identity rules, not a same-ID repair. Deliver complete current/predecessor source pins and declared semantic deltas to CA-P-2248; the author does not accept their own packet. Historical receipts remain frozen and do not establish new-design readiness. This Task requires actual independent acceptance before Done; split a concrete overrun before execution.

### Completion checkpoint

Root authorized Done after actual independent RMEDO-only acceptance of the current rebuilt subset: 81 current sources, 120 exact archives, 67 intermediate pins and 29 declared Scope Units with the previous 27 unchanged. The independently checked [mechanical/source result](../../../../.caprmedio_tmp/connector-rmedo-check-gHaSHb/rmedo-mechanical-result.json) has SHA256 `d1f17f9c8b20ee259498fccf0298f92e13f0a7cec676007c9735e55433d09c92`. This closes only this delivered authoring packet; CA-P-2248's final expanded-Plan check remains pending. Missing operation-specific contracts under CA-P-2249/2250, subsequent FPF review, all implementation/fixtures, applicable Core alignment and deferred publication remain separate. No live capability follows.

### Definition of Done

The Plan is **not** Done if an affected contract retains conflicting assumptions, current/predecessor pins or exact history are missing, independent source acceptance is absent, one-Atom safeguards weaken, deferred policies are silently chosen, forbidden surfaces change, source authoring is reported as implementation/live capability, or own work exceeds 15 minutes without decomposition.
