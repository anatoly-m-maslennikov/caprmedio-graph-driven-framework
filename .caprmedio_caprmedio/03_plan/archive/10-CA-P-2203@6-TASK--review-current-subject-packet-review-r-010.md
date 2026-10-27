---
atom_id: CA-P-2203@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 6
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2193
tier: 3
---
# Summary

Review current Subject packet review-r-010

## Objective

Freshly review every Subject occurrence in this exact whole-source packet.

## Details

This roll-up Task has zero own work. CA-P-2242 and CA-P-2243 freshly review disjoint ten-owner halves of the same 20-Requirement/132-occurrence [packet](../../../../../.caprmedio_tmp/stage2-migration-20261012/inventory/batches/review-r-010.json), SHA-256 `45374882ee2246153f0b236aa773058e07b5ef088b4f3787ff77d0249e107c37`; CA-P-2244 assembles/checks the separately accepted halves. Every child is bounded to 15 minutes for one AI Agent. All source/occurrence pins remain required; read preparation or a partial half does not complete this Task.

Required capture input: CA-P-2187 Done and [the current inventory](../../../../../.caprmedio_tmp/stage2-migration-20261012/inventory/current-subjects.inventory.json), SHA-256 `0b2f217e8ebf541cc84322d18be81073bfdbb54342f248cbf9928583678455c7`. Bind [Candidate #3](../../../../_projection/core-entity-review/presentation/operator.model.candidate-3.md), SHA-256 `ff34c4d75d64766543f397024b0d003e9f8c6e2293e97a8a51e56b8f737be7a2`, and [the latest Operator decision record](../../../../../.caprmedio_tmp/stage2-migration-20261012/model/operator-subject-decisions.md), SHA-256 `ce28c370232ae43829036714eb24957987d11453fd94a76c4794997b088ecfb5`. Historical byte equality, old Task completion and earlier reports do not supply fresh semantic acceptance.

Bind [the base decision record](../../../../../.caprmedio_tmp/stage2-migration-20261012/model/operator-subject-decisions.md) `ce28c370232ae43829036714eb24957987d11453fd94a76c4794997b088ecfb5`, [the scope-reference addendum](../../../../../.caprmedio_tmp/stage2-migration-20261012/model/scope-reference-decision.md) `df2303d0128ca9b882e2877f41ebc2f17f2c9fc2ce4a3a7ffefa394000d249c0`, and [the content-conflict addendum](../../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md) `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc` (SHA-256). Resolve overloaded old Subject names from each full body: the approved Atom.Owning Scope Unit and Atom.Target Scope Unit are references; Atom.Substance Scope is its exact applicability boundary. Combined lookup Atom Scope is a Selection, not a fourth scope. No storage-key/body change is permitted.

Confirmed whole-owner content conflicts may remain entirely unchanged and be explicitly queued for CA-P-1970 with exact evidence; all owners/occurrences still require fresh review and separate acceptance. Uncertainty is not that confirmation. This split adds no migration staging or content authority.

Apply the parent review contract: preserve exact source predicates/qualifiers and role-specific meaning; distinguish Object, Term and Selection. Named Selections are permitted, never Objects by that permission; owning-Atom and target-Atom subsets remain distinct. Preserve Owning Scope Unit, relational Target Scope Unit and exact governed Substance Scope; the legacy combined lookup Selection is not a fourth scope. Record supported change, supported unchanged or unresolved for every occurrence with current source evidence, prospective exact value and confidence. Below 90%, investigate then ask through Root before adoption/staging; do not infer new selector grammar or endpoint admission.

Own only this packet's derived review output under `.caprmedio_tmp/stage2-migration-20261012/reviews/`; preserve prior reports and other workers' outputs. Freeze the actual report path/hash and full-owner coverage for a separate independent reviewer. That reviewer must check current source/candidate/decision pins, semantic evidence and every prospective value, not only syntax/counts. No source/Tool/content edits, migration staging, accepted final graph, integration or publication is included.

### Decomposing Plans

- [CA-P-2242 — Review the first ten R010 owners](10-CA-P-2203@6-TASK--review-current-subject-packet-review-r-010/01-CA-P-2242-TASK--review-the-first-ten-r010-owners.md)
- [CA-P-2243 — Review the last ten R010 owners](10-CA-P-2203@6-TASK--review-current-subject-packet-review-r-010/02-CA-P-2243-TASK--review-the-last-ten-r010-owners.md)
- [CA-P-2244 — Assemble and check the R010 review](10-CA-P-2203@6-TASK--review-current-subject-packet-review-r-010/03-CA-P-2244-TASK--assemble-and-check-the-r010-review.md)

### Definition of Done

Not Done unless all three children have actual independently accepted outputs and complete 20-owner/132-occurrence coverage. Missing/stale pins or semantic receipts, unsupported meanings/qualifiers, adopted uncertainty, reused historical acceptance, unconfirmed exclusions or source effects keep this roll-up open.
