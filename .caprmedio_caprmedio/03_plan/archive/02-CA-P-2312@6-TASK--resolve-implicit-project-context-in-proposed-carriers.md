---
atom_id: CA-P-2312@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Project Configuration
  - Subject/Engineering/Validation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-24 08:16:43 +0400
relations:
  is_decomposition_of:
  - CA-P-2307
tier: 3
---
# Summary

Resolve implicit Project context in proposed carriers

## Objective

Bind the actual selected Project identity and control root from existing Settings/selection context. Resolve Project-owned and Project-targeted carriers without a synthetic Scope Unit row. Preserve unknown/ambiguous identity, external placement, declared scope, relational and source-currentness safeguards.

## Details

Estimated own work: up to 15 minutes; decompose further before exceeding that bound. The Operator approved fixing the two existing validator gaps before TOMLKit implementation. Fix current-contract conformance only; any missing policy needs a separate decision. Root owns Plans and Git; parallel workers own disjoint production and independent test files. No legacy Atom rewrite, dependency change, live source publication, Core migration or installed activation.

### Definition of Done

The bounded change has an actual failing-before/passing-after regression, relevant refusal tests, current source/implementation pins and independent review. Remaining legitimate source defects or unsupported context are named, not silently accepted. No full source or runtime acceptance follows from focused tests.

### Result

Bounded fix and independent review passed. Evidence and exact pins: `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/proposed-carrier-admission-review.md`. Fourteen independent regressions and thirty lifecycle tests pass; broader pre-existing failures are recorded separately. Full new-carrier admission remains blocked by an existing non-Atom evidence document and unresolved requested-source metadata. This Task does not accept those inputs or close the parent implementation gates.
