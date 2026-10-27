---
atom_id: CA-P-2656
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Relation
version: 1
updated_at: 2026-10-26 17:56:09 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align shared Relation Type contracts

## Objective

Apply the accepted shared Relation Type contract without introducing a Type Status, owning graph, forced exact-one defining R gate, or per-Type admission registry.

## Details

- Bound the source batch to the relation proposals in .caprmedio_tmp/subject-alignment-accepted/relations.json and their directly affected Current consumers, including R806, R1246, M120 and R1965.
- Keep each Relation Type's minimal canonical name and meaning in its governing R Claim(s); preserve any explicitly evidenced inverse, derivation or transitivity semantics only when relevant.
- Keep Relation Type identity shared at Project scope. Use applicable Graph Rules for graph-specific endpoint classes, contexts, cardinality, permissions and prohibitions; do not create graph-owned Type copies, a per-Type/per-graph admission gate, or default-allow/default-deny behavior.
- Keep Relation Type Status out of the contract and retain source traceability. Do not add a relation kind, registry authority, runtime implementation, code or Terms Graph work.
- Preserve existing Summaries, unrelated sources, Drafts and Archives; record bounded changed-source evidence for Root's later Draft/archive/promotion integration.

### Completion evidence

The accepted source correction is applied. Independent final verification passed.
Evidence: `.caprmedio_tmp/subject-alignment-accepted/verify.final.json`,
`verify.final.md`, both publication receipts, and
`graph-final/graph.subject-views.manifest.json`. The four Current-RMEDO views
contain 2,223 sources (792 Core, 405 Methodology, 1,026 Engine), with zero
unmapped Subjects. This is source/projection verification, not runtime execution.

## Definition of Done

- The bounded Relation Type definitions and registry consumers require only the accepted minimal defining-Claim contract.
- No touched source requires Relation Type Status, graph ownership, an exact-one defining R gate, or a universal per-Type admission process.
- Graph-specific constraints remain in Graph Rules and optional inverse/derivation/transitivity meaning remains source-evidenced.
- Actual source IDs, Versions and verification evidence are recorded without claiming code, runtime, full-suite, release or Git completion.
