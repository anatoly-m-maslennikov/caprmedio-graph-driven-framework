---
atom_id: CA-P-2660
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-26 17:56:09 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Verify accepted alignment and regenerate four Subject views

## Objective

After P2656–P2659 integration, verify the actual Current frontier, staged Draft/archive effects, accepted decisions and four stable Subject views; do not claim completion before the pending evidence files exist and pass.

## Details

- Run only after the four source batches and Root's Draft-first integration are actually available. Re-read changed Current sources, predecessor/history records, direct consumers and the final Epic append; a proposal, Draft or prior view is not applied evidence.
- Reconcile the expected counts against actual staging: phase 1 is 53 updates plus R1513 retirement; phase 2 is 27 updates plus six retirements (33 plan rows), including the second O127 update. Report any count or source-set divergence instead of silently widening scope.
- Check the shared Relation Type contract, Step/ON_RESULT retirement, Plan containment/cascade, syntax/Type guidance, and preservation of unrelated obligations. Verify parent terminal behavior exactly: all selected contained children terminal, mixed Done/Canceled allowed, already-terminal children preserved, unfinished children canceled, and parent own work/DoD only for Done.
- Regenerate the four prescribed stable-ID Subject views from Current RMEDO sources only, preserving the accepted three-section form and excluding Drafts, Archives, delivery mirrors and derived copies. Do not change generator or runtime code.
- Use verification evidence paths .caprmedio_tmp/subject-alignment-accepted/verify.final.json, .caprmedio_tmp/subject-alignment-accepted/verify.final.md and .caprmedio_tmp/subject-alignment-accepted/graph-final/graph.subject-views.manifest.json (or the final manifest path recorded by the run). Missing paths mean verification is pending, not passed.
- Keep Terms Graph implementation, code, tools, runtime, full-suite testing, deployment, release, commit and push outside this Task.

### Completion evidence

The accepted source correction is applied. Independent final verification passed.
Evidence: `.caprmedio_tmp/subject-alignment-accepted/verify.final.json`,
`verify.final.md`, both publication receipts, and
`graph-final/graph.subject-views.manifest.json`. The four Current-RMEDO views
contain 2,223 sources (792 Core, 405 Methodology, 1,026 Engine), with zero
unmapped Subjects. This is source/projection verification, not runtime execution.

## Definition of Done

- All five child Task effects are checked against actual Current sources and bounded direct consumers; unresolved evidence remains explicit.
- The expected phase counts and O127 second update reconcile with actual staging, or a concrete discrepancy is recorded.
- Four stable-ID Current-RMEDO views and the accepted three-section output are regenerated only after source integration, with source pins and manifest evidence.
- verify.final.json, verify.final.md and the graph-final manifest exist and support the reported checks; no completion claim is made before they do.
- No unapproved taxonomy, Terms Graph implementation, runtime/code change, full-suite, release or Git claim is included.
