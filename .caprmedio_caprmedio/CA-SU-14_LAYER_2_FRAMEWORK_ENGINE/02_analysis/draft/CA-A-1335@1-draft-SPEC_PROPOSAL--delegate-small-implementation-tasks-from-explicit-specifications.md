---
identity:
  atom_id: CA-A-1335
  ref_id: CA-A-1335@1-draft
context:
  container:
    scope_unit: CA-SU-14
  role: Analysis & Advisory
  form: Spec Proposal
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-10 13:47:32 +0400
destination:
  file:
    name: CA-A-1335@1-draft-SPEC_PROPOSAL--delegate-small-implementation-tasks-from-explicit-specifications.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/draft
author: Anatoly Maslennikov
---

## Summary

Delegate small implementation tasks from explicit specifications

## Proposal

Give each worker one small outcome, one owned Scope Unit and exclusive paths. Aim to finish in one context without compaction. Split a task before dispatch when its specifications, code and expected output are too large. Keep the existing 15–20 minute subtask target; size the context separately.

Resolve the applicable sources once. Reuse a compact policy prompt with source IDs and Versions. Give the worker only the selected sources and code context, without the full chat or project inventory.

## Task shape

```text
Outcome: <one result or explicit slice>
Implement: <R IDs and Versions>
Use Solutions: <M IDs and Versions>
Apply MED from topics: <Aspect branches>
Selected policies/decisions: <IDs and Versions>
Acceptance: <E IDs and Versions; selected checks>
Delivery: <D IDs and Versions, when needed>
Scope Unit: <one>
Own paths: <exclusive files>
Policy prompt: <compiled prompt and source pins>
Check: <commands and observable result>
```

Select MED by applicability, Scope and topic. Topic membership alone does not make a Decision applicable. A slice does not establish implementation of the whole Atom.

## Subtasks

- Tests: implement the selected Es using test Methods; own test paths.
- Implementation: implement the R slice using M Solutions and D contracts; own implementation paths.
- Parent: resolve shared ownership and verify the combined result.

Use separate test and implementation workers when useful. Prepare acceptance tests first. A small change may use one worker. Report a flawed test rather than weaken it.

For example, take only command-palette keyboard navigation from R2727, use Solution M466 and the relevant Frontend MED. The test subtask owns the selected E683 checks for opening the palette, moving its selection and choosing a command; the implementation subtask owns that control. Both target WORKBENCH_FRONTEND. Passing this slice does not establish all of R2727 or E683. Before dispatch, pin the adopted Versions, exact paths and checks.

Return changed paths, source IDs implemented, checks run and remaining issues. If a task cannot finish in context, leave a small checkpoint.

## Related Atoms

- CA-R-2727
- CA-M-327
- CA-M-328
- CA-M-395
- CA-M-466
- CA-M-513
- CA-M-526
- CA-E-683
