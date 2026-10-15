---
atom_id: CA-P-2247
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
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 1
updated_at: "2026-10-12 23:10:03 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Align logical connector Operations Workflows

## Objective

The affected Operations define independent logical connector Actions and Workflows with the approved target, edit and configuration boundaries.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Use CA-P-2167's prospective decisions and actual existing declared Engine authority roots. Exclusive source scope: the Root-assigned Operations packet, including CA-O-201 Find targets Workflow, CA-O-202 Modify explicitly selected targets Workflow, CA-O-203 Create Scope Unit Action, CA-O-204 TOML patch Action, CA-O-205 Project Structure Workflow and CA-O-206 Project Settings Workflow, the required Steps CA-O-207–210, plus affected existing Operations. Reuse CA-O-047's existing read Action, reopening its actual current contract; do not create another read Action or a new Scope Unit.

Keep logical storage-neutral connector boundaries; file/database details are private. Find, Read and Modify are independent generally; findWorkflow/modifyWorkflow need no compulsory chaining. Preserve distinct createAtom/createSU and archive-only Atom removal. A property Tool rejects a same-ID Summary change; replacement creates a fresh ID, archives the predecessor and reports target/created/archived identities without automatic reference retargeting.

Use the shared section-edit family for add/replace/remove/title-rename/order and property lists by VALUE or full-set replacement including add/remove, never indexed items. The shared TOML Action serves two distinct config Workflows with their corresponding schema checks. Subject search keeps governs/depends_on, scope and exact/prefix/suffix/contains modes explicit.

Every requested Atom action is independent. Stop on first failure, retain actual earlier successes and leave remaining targets untouched; no cross-Atom all-or-nothing orchestration. Keep one-Atom safety, approval/currentness and truthful effect/recording boundaries. Resume/retry and the old concurrent-publication safety choice are deferred; do not implement or imply automatic continuation/replay or a publication mechanism.

Other workers own Requirements/Methods and Evaluation/Delivery. Serialize shared carriers and preserve fixed Summary/ID/current filename, Version +1, actual offset timestamp and exact predecessors for same-identity semantic revisions; a Summary change follows fresh-ID replacement. Deliver actual current/predecessor pins, Workflow/Action bindings and stop/result distinctions to CA-P-2248. No code, database build, Core/migration/source publication or runtime activation is included. Keep historical receipts frozen and this Task Active until actual independent acceptance; split a concrete overrun before execution.

### Definition of Done

The Plan is **not** Done if Operation bindings are missing/ambiguous, private storage details become public logical requirements, independent operations are forced into an unnecessary chain, config schemas or target/result identities are confused, stale indexed-list/cross-Atom rollback behavior persists, current/predecessor evidence or independent acceptance is absent, one-Atom safeguards weaken, a deferred policy is chosen, forbidden effects occur, or own work exceeds 15 minutes without decomposition.
