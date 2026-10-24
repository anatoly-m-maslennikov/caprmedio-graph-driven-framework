---
atom_id: CA-P-2247@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 3
updated_at: "2026-10-13 00:21:20 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Align logical connector Operations Workflows

## Objective

The affected Operations define independent logical connector Actions and Workflows with the approved target, edit and configuration boundaries.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Use CA-P-2167's prospective decisions and the approved CONNECTOR_TOOLS/TOOL_WORKFLOWS FEATURE authority roots. Exclusive source scope: the Root-assigned Operations packet, including CA-O-201 Find targets Workflow, CA-O-202 Modify explicitly selected targets Workflow, CA-O-203 Create Scope Unit Action, CA-O-204 TOML patch Action, CA-O-205 Project Structure Workflow and CA-O-206 Project Settings Workflow, the required Steps CA-O-207–210, plus affected existing Operations. Reuse CA-O-047's existing read Action, reopening its actual current contract; do not create another read Action; Root alone declares the two approved FEATURE Scope Units, and no other structural unit is created by this packet.

The Operator approved the two FEATURE siblings CONNECTOR_TOOLS and TOOL_WORKFLOWS under PROGRAMMATIC (Level 3, navigation 5/6), with flat role folders and shared Core policies inside each. Root alone updates Project Structure; only rebuilt RMEDO moves to `305_FEATURE_CONNECTOR_TOOLS`/`306_FEATURE_TOOL_WORKFLOWS`. Their future `305_CONNECTOR_TOOLS`/`306_TOOL_WORKFLOWS` delivery roots remain unmaterialized; existing TOOLS, unrelated legacy authority, existing delivery bindings and code paths stay unchanged. This approval supersedes the prior prospective no-new-Scope-Unit restriction for exactly this split.

Connector Core CA-R-1936/CA-M-376/CA-E-628/CA-D-625 must supply a coherent broad logical API across ALL connector Tools: common input/result/precondition/error/effect contracts, not a new transport, database or retry design. Workflow Core policies remain separate. Actual code work must explicitly address hardcoded authority paths, release/admission bindings, selected-execution refresh/seals/pins and the graph generator's incorrect delivery derivation, with legacy Core/content alignment and independent runtime/admission/fixture gates retained. New source ownership or a matching receipt does not make existing code compatible, and successful source authoring grants no live readiness.

Bind every connector Operation to the common Connector Core CA-R-1936/CA-M-376/CA-E-628/CA-D-625 logical input/result/precondition/error/effect interface. Keep shared Workflow policies Core within TOOL_WORKFLOWS and operation-specific refinements coherent; do not create a new transport or retry/resume mechanism.

Keep logical storage-neutral connector boundaries; file/database details are private. Find, Read and Modify are independent generally; findWorkflow/modifyWorkflow need no compulsory chaining. Preserve distinct createAtom/createSU and archive-only Atom removal. A property Tool rejects a same-ID Summary change; replacement creates a fresh ID, archives the predecessor and reports target/created/archived identities without automatic reference retargeting.

Use the shared section-edit family for add/replace/remove/title-rename/order and property lists by VALUE or full-set replacement including add/remove, never indexed items. The shared TOML Action serves two distinct config Workflows with their corresponding schema checks. Subject search keeps governs/depends_on, scope and exact/prefix/suffix/contains modes explicit.

Every requested Atom action is independent. Stop on first failure, retain actual earlier successes and leave remaining targets untouched; no cross-Atom all-or-nothing orchestration. Keep one-Atom safety, approval/currentness and truthful effect/recording boundaries. Resume/retry and the old concurrent-publication safety choice are deferred; do not implement or imply automatic continuation/replay or a publication mechanism.

Other workers own Requirements/Methods and Evaluation/Delivery. Serialize shared carriers and preserve fixed Summary/ID/current filename, Version +1, actual offset timestamp and exact predecessors for same-identity semantic revisions; a Summary change follows fresh-ID replacement. Deliver actual current/predecessor pins, Workflow/Action bindings and stop/result distinctions to CA-P-2248. No code, database build, CORE_META_MODEL content/Subject migration, live Tool publication or runtime activation is included. Keep historical receipts frozen and this Task Active until actual independent acceptance; split a concrete overrun before execution.

### Completion checkpoint

Root authorized Done after actual independent RMEDO-only acceptance of the current rebuilt subset: 81 current sources, 120 exact archives, 67 intermediate pins and 29 declared Scope Units with the previous 27 unchanged. The independently checked [mechanical/source result](../../../../../.caprmedio_tmp/connector-rmedo-check-gHaSHb/rmedo-mechanical-result.json) has SHA256 `d1f17f9c8b20ee259498fccf0298f92e13f0a7cec676007c9735e55433d09c92`. This closes only this delivered authoring packet; CA-P-2248's final expanded-Plan check remains pending. Missing operation-specific contracts under CA-P-2249/2250, subsequent FPF review, all implementation/fixtures, applicable Core alignment and deferred publication remain separate. No live capability follows.

### Definition of Done

The Plan is **not** Done if Operation bindings are missing/ambiguous, private storage details become public logical requirements, independent operations are forced into an unnecessary chain, config schemas or target/result identities are confused, stale indexed-list/cross-Atom rollback behavior persists, current/predecessor evidence or independent acceptance is absent, one-Atom safeguards weaken, a deferred policy is chosen, forbidden effects occur, or own work exceeds 15 minutes without decomposition.
