---
atom_id: CA-P-1912@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 28
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Projection
  depends_on:
  - Entity
  - Term
  - Atom
  - Property
  - Carrier
  - Plan
version: 5
updated_at: 2026-10-15 12:26:16 +0000
relations:
  is_decomposition_of:
  - CA-P-1872
  blocks:
  - CA-P-1969
---
# Summary

Verify the migrated Core graph reproduction

## Objective

Verify that the approved migrated Core Subjects reproduce the separately accepted graph without unexpected source or meaning changes.

## Details

### Actual Subjects-only migration and graph result — 2026-10-15

Local release `local-20261015-subject-batch-004` completed; its actual receipt is `.caprmedio_runtime/simple_local_release/reports/local-20261015-subject-batch-004.md`. The authorized sequence used pre-migration Git checkpoint `4fa3c461b` and committed all 611 edit drafts as `1d55642ea` before promotion.

One operation, `subjects-candidate4-20261015-001`, reached scheduler SUCCESS and a terminal completed batch: 611 completed, zero remaining, automatic retry false. Actual accepted/result evidence is `.caprmedio_install/workflow_orchestrator/runs/subjects-candidate4-20261015-001/accepted.json` and `subject_batch_progress.json` in that directory. No second confirmation, extra review/validation round, replay or batch rollback is claimed or required by this result checkpoint.

The actual migrated-source entity graph was rebuilt into `.caprmedio_caprmedio/_projection/core-subject-notation/after-current/`: `graph.json`, `indented.txt`, `provenance.json` and `manifest.json`. Its manifest records 906 owners, 4,491 occurrences, 782 nodes and 259 edges. Comparing its source hashes to `.caprmedio_tmp/stage2-migration-20261015/instructed-batch-source-refresh/source-pins.json` gives 611 changed and 295 unchanged owners (266 unchanged plus all 29 holds). The graph is the actual current mechanical Subjects projection, not full semantic/native graph admission. Ordinary content migration remains separate and unperformed.

Migration, required Journal effects and the actual graph output are committed as `6512a2e71`; these Plan result checkpoints are a separate change. This records successful authorized operation and actual graph output, not completion of unrelated deferred work. Keep this Plan Active while the Operator decides whether to move deferred branches to a Backlog Epic or retain them Active; no descendant is relocated or marked Done here, and no parent-status cascade is authorized.

### Operator-authorized minimum Subjects-only sequence — 2026-10-15

The Operator now authorizes this Candidate #4 Subjects-only sequence through the existing Workflows: commit current work → create the selected edit drafts → commit drafts → archive exact current predecessors and promote drafts → rebuild the entity graph from actual migrated sources. No additional confirmation, independent post-stage full preview, semantic review or extra review/validation round is required. This checkpoint supersedes conflicting earlier prerequisite, approval and Definition-of-Done clauses for this sequence; it does not remove normal operation checks or expand generic content-update authority.

Retain current target/draft checks and ordinary operation results, canonical ID and original Status restoration, Version +1, actual Project-time updated_at and byte-exact predecessor archives. Stop at the first failed or unknown result, preserve completed predecessors and the untouched remainder, and perform no automatic replay or batch rollback. Existing Git commits and predecessor archives remain recovery evidence, not permission for automatic reset. Preserve all 29 held owners unchanged and ordinary content migration separately under CA-P-1970. Record actual graph-rebuild output; candidate-only reproduction or a planned graph is not that output.

For this Task, retain the actual post-promotion entity-graph rebuild and its real output/result. The earlier independent full ledger/reproduction acceptance round is not an additional prerequisite or required validation round for this authorized sequence. Do not repair sources or infer graph success from old candidate-only evidence.

Estimated own work: 15 minutes. Assignee: AI Agent.

This Task owns the sole migration reproduction receipt consumed by CA-P-1969. Check the exact approved minimum grammar-body exception allow-list, preserved ordinary content/all unrelated frontmatter, and actual Version/time/status/history/recording effects. Use an independently authored expected ledger rather than the producer as its own oracle; fixture producer corruption must fail.

Readiness conditions: CA-P-2167's complete independent Tool receipt and CA-P-1911 are Done. Inputs: its exact changed source snapshot and applied-change record, the authorized preview and grammar contracts, CA-P-1909's separately accepted graph and hash, and the complete occurrence and node ledgers.

Read the migrated Core and rebuild into a new derived projection without changing authoritative sources, old outputs or history. Compare qualified nodes, graph-owned relations and directions, inherited constraints, allowed values, source references and all ledger dispositions with the accepted graph. Check source-backed Carrier bindings separately: `@` is filename punctuation only, not a graph/Subject Relation operator. Planned drop/consolidation/generalization marks are traceable decisions, not automatic node or historical deletion.

Verify the exact allowed before/after changes, required revisions and grammar checks, preserved excluded and unrelated files, and absence of unexpected Core meaning changes. Bind current source identities, versions and hashes. Explain every difference; an unresolved mismatch or unsupported region is not reproduction success. Report failures with the authorized recovery boundary instead of repairing or replaying migration.

Output: the new reproduced derived graph and its canonical hash, exact source/grammar pins, accepted-versus-reproduced comparison, complete ledger coverage and preservation report. Confirm that only the approved changes occurred and all required checks were actually performed.

Exclusive scope: read-only migrated sources and evidence, a new separate derived projection, and verification/handoff records only. No source, grammar, code, runtime, binding or history repairs; no old-output overwrite and no live MCP execution or Run/Journal claim. Full native MCP delivery and its actual admission, runtime and receipt gates remain separate and pending; local reproduction cannot complete the whole Epic.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold. Split into bounded direct child Plans before execution if the ready work cannot fit 15 minutes. Creation of this Task does not start, authorize or complete this stage.

### Definition of Done

the Plan is **not** Done **if** ((CA-P-1911 is **not** Done) **or** (the new separate projection, canonical hash, current source/grammar pins, comparison, complete ledgers **or** preservation report is missing) **or** (a required qualified node, relation, constraint, allowed value, source reference **or** Carrier binding fails to reproduce the accepted graph) **or** (an unexpected source/meaning change, lost historical reference, unapproved deletion **or** unsupported serialization is found) **or** (a required check is failed, stale, unresolved **or** unverified) **or** (verification changes an authoritative source, old output, code, runtime, binding **or** history) **or** (uncertainty below the confidence threshold was silently resolved **or** work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
