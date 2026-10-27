---
atom_id: CA-P-2246@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Scope Unit
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Configuration
  - Revision
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 8
updated_at: 2026-10-24 08:06:50 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Align logical connector Evaluation and Delivery

## Objective

The affected Tool Evaluation and Delivery contracts define independently checkable outcomes for the approved logical connector and Workflow behavior.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Use CA-P-2167's prospective rebuild decisions and the approved CONNECTOR_TOOLS/TOOL_WORKFLOWS FEATURE authority roots. Exclusive source scope: the Root-assigned Evaluation/Delivery packet, including new CA-E-625–628, CA-D-622–625 and the CA-D-425 revision. Other workers own Requirements/Methods and Operations. Serialize overlapping existing carriers; Root alone declares the two approved FEATURE Scope Units; do not create other Scope Units, code, database storage, CORE_META_MODEL/migration changes or projections.

The Operator approved the two FEATURE siblings CONNECTOR_TOOLS and TOOL_WORKFLOWS under PROGRAMMATIC (Level 3, navigation 5/6), with flat role folders and shared Core policies inside each. Root alone updates Project Structure; only rebuilt RMEDO moves to `305_FEATURE_CONNECTOR_TOOLS`/`306_FEATURE_TOOL_WORKFLOWS`. Their future `305_CONNECTOR_TOOLS`/`306_TOOL_WORKFLOWS` delivery roots remain unmaterialized; existing TOOLS, unrelated legacy authority, existing delivery bindings and code paths stay unchanged. This approval supersedes the prior prospective no-new-Scope-Unit restriction for exactly this split.

Connector Core CA-R-1936/CA-M-376/CA-E-628/CA-D-625 must supply a coherent broad logical API across ALL connector Tools: common input/result/precondition/error/effect contracts, not a new transport, database or retry design. Workflow Core policies remain separate. Actual code work must explicitly address hardcoded authority paths, release/admission bindings, selected-execution refresh/seals/pins and the graph generator's incorrect delivery derivation, with legacy Core/content alignment and independent runtime/admission/fixture gates retained. New source ownership or a matching receipt does not make existing code compatible, and successful source authoring grants no live readiness.

Connector Core CA-E-628/CA-D-625 must make the common logical input/result/precondition/error/effect contract independently checkable across ALL connector Tools, with coherent operation-specific refinements and shared Workflow Core policies in TOOL_WORKFLOWS. Broad API here does not mean a new transport, database or retry design.

Specify storage-neutral logical request/result boundaries without exposing private file/database implementation. Cover independent Find/Read/Modify, createAtom/createSU, archive-only removal, and independent findWorkflow/modifyWorkflow. Check any Summary change refuses same-ID property modification and uses fresh replacement identity plus archival. Replacement results distinguish target/created/archived IDs without silently retargeting references.

Make shared section add/replace/remove/title-rename/order, one property-list item by VALUE or full-set replacement including add/remove, and Subject field/scope/exact-prefix-suffix-contains matching independently checkable. Bind the shared TOML connector's Project Structure and Project Settings Workflows to distinct config schema checks.

Evaluate multiple actions by actual per-Atom outcomes: stop at the first failure, retain earlier successes and prove later targets untouched. Do not require cross-Atom rollback. Retain one-Atom authorization, currentness, preservation, required history and truthful recording. Resume/retry is deferred, and the existing concurrent-publication guard remains deferred; no unknown policy may become an implicit implementation requirement or capability claim.

For each admitted same-identity semantic source revision preserve Summary/ID/current filename, increment Version exactly once, use actual offset time and retain exact prior bytes. Deliver current/predecessor source pins, semantic deltas and explicit positive/refusal expectations to CA-P-2248. Independent source review is not execution of new Tool fixtures. Keep historical receipt pins/results unchanged; this Task remains Active until actual independent acceptance. Split a concrete overrun before execution.

### Completion checkpoint

Root authorized Done after actual independent RMEDO-only acceptance of the current rebuilt subset: 81 current sources, 120 exact archives, 67 intermediate pins and 29 declared Scope Units with the previous 27 unchanged. The independently checked [mechanical/source result](../../../../.caprmedio_tmp/connector-rmedo-check-gHaSHb/rmedo-mechanical-result.json) has SHA256 `d1f17f9c8b20ee259498fccf0298f92e13f0a7cec676007c9735e55433d09c92`. This closes only this delivered authoring packet; CA-P-2248's final expanded-Plan check remains pending. Missing operation-specific contracts under CA-P-2249/2250, subsequent FPF review, all implementation/fixtures, applicable Core alignment and deferred publication remain separate. No live capability follows.

### Definition of Done

The Plan is **not** Done if outcomes or refusal checks are ambiguous, stale indexed-list/cross-Atom transaction assumptions survive, schema/result/identity distinctions are missing, exact predecessor/current pins or independent acceptance are absent, one-Atom safeguards weaken, deferred choices are inferred, forbidden effects occur, source authoring substitutes for implementation/live verification, or own work exceeds 15 minutes without decomposition.
