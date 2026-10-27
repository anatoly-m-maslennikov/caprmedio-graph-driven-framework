---
atom_id: CA-P-1911@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 27
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 8
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-1872
  blocks:
  - CA-P-1912
tier: 3
---
# Summary

Apply the approved Core Subject migration

## Objective

Apply only the exact separately authorized Core Subject migration while preserving governing authority, source meaning and history.

## Details

### Actual Subjects-only migration and graph result — 2026-10-15

Local release `local-20261015-subject-batch-004` completed; its actual receipt is `.caprmedio_runtime/simple_local_release/reports/local-20261015-subject-batch-004.md`. The authorized sequence used pre-migration Git checkpoint `4fa3c461b` and committed all 611 edit drafts as `1d55642ea` before promotion.

One operation, `subjects-candidate4-20261015-001`, reached scheduler SUCCESS and a terminal completed batch: 611 completed, zero remaining, automatic retry false. Actual accepted/result evidence is `.caprmedio_install/workflow_orchestrator/runs/subjects-candidate4-20261015-001/accepted.json` and `subject_batch_progress.json` in that directory. No second confirmation, extra review/validation round, replay or batch rollback is claimed or required by this result checkpoint.

The actual migrated-source entity graph was rebuilt into `.caprmedio_caprmedio/_projection/core-subject-notation/after-current/`: `graph.json`, `indented.txt`, `provenance.json` and `manifest.json`. Its manifest records 906 owners, 4,491 occurrences, 782 nodes and 259 edges. Comparing its source hashes to `.caprmedio_tmp/stage2-migration-20261015/instructed-batch-source-refresh/source-pins.json` gives 611 changed and 295 unchanged owners (266 unchanged plus all 29 holds). The graph is the actual current mechanical Subjects projection, not full semantic/native graph admission. Ordinary content migration remains separate and unperformed.

Migration, required Journal effects and the actual graph output are committed as `6512a2e71`; these Plan result checkpoints are a separate change. This records successful authorized operation and actual graph output, not completion of unrelated deferred work. Keep this Plan Active while the Operator decides whether to move deferred branches to a Backlog Epic or retain them Active; no descendant is relocated or marked Done here, and no parent-status cascade is authorized.

### Operator-authorized minimum Subjects-only sequence — 2026-10-15

The Operator now authorizes this Candidate #4 Subjects-only sequence through the existing Workflows: commit current work → create the selected edit drafts → commit drafts → archive exact current predecessors and promote drafts → rebuild the entity graph from actual migrated sources. No additional confirmation, independent post-stage full preview, semantic review or extra review/validation round is required. This checkpoint supersedes conflicting earlier prerequisite, approval and Definition-of-Done clauses for this sequence; it does not remove normal operation checks or expand generic content-update authority.

Retain current target/draft checks and ordinary operation results, canonical ID and original Status restoration, Version +1, actual Project-time updated_at and byte-exact predecessor archives. Stop at the first failed or unknown result, preserve completed predecessors and the untouched remainder, and perform no automatic replay or batch rollback. Existing Git commits and predecessor archives remain recovery evidence, not permission for automatic reset. Preserve all 29 held owners unchanged and ordinary content migration separately under CA-P-1970. Record actual graph-rebuild output; candidate-only reproduction or a planned graph is not that output.

CA-P-1911@8 remains the single application owner. The latest authorization supersedes the earlier separate batch/target confirmation, fresh final-Atom preview/stage/approval and prior-Plan-Done gates as prerequisites to this sequence. Preserve normal current-rule/self-update and target/draft checks; do not replay a stale or failed operation or substitute an unrelated patch.

### Selected existing-tool application sequence — 2026-10-15

The Operator selected option 1 using the existing Tools: apply the 609 nongrammar Atoms first, then CA-E-383, and handle CA-R-1324 last through a fresh preview, fresh staging and exact approval after the preceding changes. The verified 611-owner/848-patch preview, seal `4c993644468c6beb348b56335b7053baa435dbc14d895e8dec96fff5334bc538`, remains preserved unchanged; only the intended application sequence changes. The final CA-R-1324 effect must bind its freshly reviewed intent and current grammar evidence, not reuse the old seal or intent as authorization.

This selects execution strategy only. It authorizes no current staging or live publication, changes no Tool, and waives no current-source, exact packet/target approval, pending batch-confirmation or semantic-report policy gate. Keep this Plan Active and preserve all earlier evidence and uncertain batches without replay; ordinary content migration remains deferred.

Estimated own work: 15 minutes. Assignee: AI Agent.

Readiness conditions: CA-P-2167's complete independent Tool receipt and CA-P-1910 are Done, and the Operator has explicitly authorized migration of its exact sealed preview, hash, file/patch list and pinned source frontier. The present request creates this Plan only. Candidate acceptance, Tool readiness, preview delivery, confidence or Plan creation grants no authority to write sources.

Inputs: the authorized preview, accepted graph and complete ledgers, current source pins, governing Subject/grammar and revision/history contracts, and the verification/recovery plan. Recheck every affected and preserved source pin, current authority, permission and safety condition before writes. Drift, unresolved authority or a changed patch requires a fresh preview and explicit authorization, not substitution of current files.

Write only the approved Subject changes, specifically authorized required grammar contracts and necessary revision/history maintenance. Preserve existing Summaries and YAML key names. Do not alter Claim meaning unless that exact semantic change is separately approved under its governing authority. Broad ontology changes, unapproved generalizations or unsupported Carrier serialization remain blocked and require separate RMED authority.

Use `/`, `.` and `:` only as admitted for the exact approved migration. `@` is filename punctuation only, not a graph/Subject Relation operator. Any additional Subject operator requires separate governed admission before use. Preserve source-backed Carrier bindings in their admitted source forms and the ledgers; a display mark is not a source declaration.

Output: the exact applied-change record, before/after source identities, revisions and hashes, preserved-history evidence and truthful failure/recovery disposition. Reconcile only approved source/history/grammar references and internal bindings named in the sealed preview. Record affected external MCP/runtime/release pins for their authorized owner, without refreshing manifests or claiming live admission. External admission remains separately pending and does not block CA-P-1912's local read-only reproduction check. Hand the exact changed snapshot to CA-P-1912.

Exclusive scope: the precise authorized source/grammar patch list and required revision/history effects only. Do not automatically delete marked nodes or history, overwrite old projections, rename serialization keys, modify unrelated sources or implementation, activate a runtime or claim a live MCP Run/Journal receipt. Full native MCP delivery remains separate and pending.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold. Split into bounded direct child Plans before execution if the ready work cannot fit 15 minutes. Creation of this Task does not start, authorize or complete this stage.

### Definition of Done

the Plan is **not** Done **if** ((CA-P-1910 is **not** Done **or** exact explicit migration authorization is missing, ambiguous **or** stale) **or** (a current source, authority, permission **or** safety check is failed **or** unverified) **or** (the applied patches differ from the authorized preview **or** required revision/history evidence is missing) **or** (a Summary, YAML key, Claim meaning, marked identity, history **or** unrelated source was changed without its separate authority) **or** (unsupported syntax **or** Carrier serialization was introduced) **or** (an approved source/history/grammar reference **or** internal binding named in the sealed preview remains unreconciled **or** a write/recovery effect remains uncertain) **or** (the exact changed snapshot, affected external-pin record **or** required handoff is missing) **or** (uncertainty below the confidence threshold was silently resolved **or** work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
