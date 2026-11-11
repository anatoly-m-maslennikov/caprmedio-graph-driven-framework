---
atom_id: CA-P-2312
ref_id: CA-P-2312
container:
  atom: CA-P-2307
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Engineering/Validation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2307
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2312-TASK--resolve-implicit-project-context-in-proposed-carriers.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/done/2-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
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
