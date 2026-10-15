---
atom_id: CA-P-1969
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 10
updated_at: "2026-10-15 12:26:16 +0000"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1970, CA-P-1974]
---
# Summary

Verify Subjects before content updates

## Objective

Prove Step 1 is complete before allowing any ordinary Atom content rewrite.

## Details

### Actual Subjects-only migration and graph result — 2026-10-15

Local release `local-20261015-subject-batch-004` completed; its actual receipt is `.caprmedio_runtime/simple_local_release/reports/local-20261015-subject-batch-004.md`. The authorized sequence used pre-migration Git checkpoint `4fa3c461b` and committed all 611 edit drafts as `1d55642ea` before promotion.

One operation, `subjects-candidate4-20261015-001`, reached scheduler SUCCESS and a terminal completed batch: 611 completed, zero remaining, automatic retry false. Actual accepted/result evidence is `.caprmedio_install/workflow_orchestrator/runs/subjects-candidate4-20261015-001/accepted.json` and `subject_batch_progress.json` in that directory. No second confirmation, extra review/validation round, replay or batch rollback is claimed or required by this result checkpoint.

The actual migrated-source entity graph was rebuilt into `.caprmedio_caprmedio/_projection/core-subject-notation/after-current/`: `graph.json`, `indented.txt`, `provenance.json` and `manifest.json`. Its manifest records 906 owners, 4,491 occurrences, 782 nodes and 259 edges. Comparing its source hashes to `.caprmedio_tmp/stage2-migration-20261015/instructed-batch-source-refresh/source-pins.json` gives 611 changed and 295 unchanged owners (266 unchanged plus all 29 holds). The graph is the actual current mechanical Subjects projection, not full semantic/native graph admission. Ordinary content migration remains separate and unperformed.

Migration, required Journal effects and the actual graph output are committed as `6512a2e71`; these Plan result checkpoints are a separate change. This records successful authorized operation and actual graph output, not completion of unrelated deferred work. Keep this Plan Active while the Operator decides whether to move deferred branches to a Backlog Epic or retain them Active; no descendant is relocated or marked Done here, and no parent-status cascade is authorized.

### Operator-authorized minimum Subjects-only sequence — 2026-10-15

The Operator now authorizes this Candidate #4 Subjects-only sequence through the existing Workflows: commit current work → create the selected edit drafts → commit drafts → archive exact current predecessors and promote drafts → rebuild the entity graph from actual migrated sources. No additional confirmation, independent post-stage full preview, semantic review or extra review/validation round is required. This checkpoint supersedes conflicting earlier prerequisite, approval and Definition-of-Done clauses for this sequence; it does not remove normal operation checks or expand generic content-update authority.

Retain current target/draft checks and ordinary operation results, canonical ID and original Status restoration, Version +1, actual Project-time updated_at and byte-exact predecessor archives. Stop at the first failed or unknown result, preserve completed predecessors and the untouched remainder, and perform no automatic replay or batch rollback. Existing Git commits and predecessor archives remain recovery evidence, not permission for automatic reset. Preserve all 29 held owners unchanged and ordinary content migration separately under CA-P-1970. Record actual graph-rebuild output; candidate-only reproduction or a planned graph is not that output.

For this Task, record the actual sequence outcome and graph output, including the 611 selected change owners, 266 unchanged owners and 29 held owners as applicable to actual results. Do not add the earlier independent full migration-acceptance/revalidation round as a gate. Partial/failed execution is not complete migration, and this checkpoint does not authorize the separate content Epic.

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-2167's complete independent Tool receipt, CA-P-1966's completed current mapping-disposition and independent current-source-rebinding evidence, CA-P-1968 and the actual CA-P-1911/1912 completion evidence. CA-P-1912 owns the sole migrated-graph verification receipt; consume and check that receipt here, do not create a competing migration acceptance. Fixture Tool verification does not replace actual migration reproduction.

Independently inventory the migrated current authoring Core and compare every changed and unchanged source against the approved packet. Verify the independently rebound current source hashes and [Candidate #4](../../_projection/core-entity-review/presentation/operator.model.candidate-4.md), SHA-256 `a23019a1ee6cd3586640d6c3d9e211091f3683ac5f136058d745650570e78ca7` version/reference, Subject grammar, field direction, unique current identities, ordinary Version increments, preserved intended status, actual history/Journal effects and preservation of ordinary bodies. A type-change discovery must be reported/routed to Step 2, not treated as an ordinary same-ID effect. Consume CA-P-1966's completed current mapping-disposition and independent current-source-rebinding evidence under CA-P-1959's latest Subjects-only override. Its current checkpoint supersedes old deep re-review/adaptation/re-pin prerequisites for this slice. Historical analytical PASS remains bound to its original bytes; no full FPF rerun, Core adoption or migration is implied.

Rebuild the subject-driven entity graph with the pinned implementation. Verify expected qualified nodes and typed relation direction, all occurrence evidence, preserved distinctions and unresolved/excluded cases. Reuse CA-P-1912's verification responsibilities and record one receipt, not a competing success claim.

A partial batch, unresolved executable mapping, failed validation, stale pin or changed ordinary body prevents a pass. The Step-1 receipt identifies exact source/implementation/graph hashes and limitations. Only a complete current pass unblocks CA-P-1970.

Validate all preserved body/frontmatter bytes. The only body exceptions are the exact approved minimum grammar patches; compare them to their allow-list rather than rejecting the approved cutover. Check actual ID/Version/status/time and Journal/history effects against the materialized packet. Step 1 verifies origins and the subject-driven graph, not already-rewritten Step-2 body content; accepted deferred body issues stay visible.

No content repair, authority edits, runtime activation or native MCP delivery occurs in this verification Task.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if Step 1 lacks a complete current pass, approved effects are missing or divergent, ordinary bodies changed, graph reproduction fails, or partial evidence is treated as the content-update gate; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
