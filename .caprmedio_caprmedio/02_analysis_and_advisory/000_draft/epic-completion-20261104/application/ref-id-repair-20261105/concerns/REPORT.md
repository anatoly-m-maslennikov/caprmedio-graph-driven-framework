# Concern Status evidence review

Read-only review of the live bytes referenced by the pinned adoption plan. No source files were changed.

- Plan: `.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/application/property-order-20261105/ref-id-data/adoption-plan.json` (SHA-256 `2526f37b5d1e243083516bfbf369a2e10046aa593fa7d3b55644c832977c09f6`)
- Census baseline: `.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/property-audit/final-header-check.json` (SHA-256 `4a6afd881059657202fd3f042b3f1b27ce088399869bc9a164eba5f722d99740`)
- Current Concern records missing Status: **127**
- Explicit `Active` candidates: **49**; unknown: **78**, including five records whose Draft-repair decision is explicitly resolved but whose Current Atom.Status mapping is not established.
- The requested “old177” does not match the current pinned plan: it contains 206 holds overall, with 127 Concern missing-Status records. The census also records 127. The report does not fabricate the extra 50.
- One batched history search over all 127 paths found **zero** historical Status edits. Current Status authorities impose required Status but do not provide a missing-value default.

## Candidate boundaries

`Active` candidates have direct deferred, pending, unresolved, or still-open language in an operative Disposition/Resolution. CA-C-109 and CA-C-110 are supported by explicit current problem/conflict statements. CA-C-268–272 explicitly say the Draft repair decision is resolved, but no Current `Status` mapping is established; their lifecycle value remains unknown. Current `Status` authority allows Draft/Active/Archived and requires one value, without defining a legacy Concern default. The remaining rows are `unknown`; no age, filename, folder, question form, or link was used to infer state.

Machine-readable per-record evidence, exact line numbers, and live source SHA-256 values are in [status-review.json](status-review.json).
