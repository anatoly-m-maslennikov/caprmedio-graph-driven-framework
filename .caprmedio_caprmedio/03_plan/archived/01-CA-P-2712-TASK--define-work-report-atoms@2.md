---
atom_id: CA-P-2712
ref_id: CA-P-2712
container:
  atom: CA-P-2711
role: Plan
form: Plan
label: Task
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 4
status: Active
version: 2
updated_at: "2026-11-08 19:02:01 +0400"
carrier_destination:
  file:
    name: 01-CA-P-2712-TASK--define-work-report-atoms.md
    path: .caprmedio_caprmedio/03_plan/CA-P-2711-EPIC--adopt-the-medo-role-and-form-model
---

## Summary

Define Work Report Atoms

## Objective

Define and adopt Work Report as a Plan Form for recording a Task’s execution in a separate file, updated throughout the work.

## Settled inputs

- A Task states the work to perform and its acceptance criteria.
- A Work Report belongs to P. It records changes made, checks performed, results and remaining gaps.
- The report is updated during execution; it is not a one-shot completion document.
- A completed Task goes to Done.
- The Work Report has its own ID, the same Summary and the same Container as its Task.
- IS_WORK_REPORT_FOR is the direct report-to-Task Relation; its target is the Task’s base Atom ID.

## Work

1. Settle the Form name, content structure and Task/report association.
2. Define report identity, cardinality and lifecycle. Keep Atom identity separate from visual grouping.
3. Define grouping and navigation between the Task and its report.
4. Create model Drafts; review, repair, promote and check them.
5. Identify affected authoring, reader and projection contracts for their implementation owners.

## Definition of Done

- Reviewed Current model Atoms define the P Work Report and its boundary with Task, I, A and C.
- The report has a declared identity, Task binding and lifecycle.
- A worked example shows updates during execution and the Task reaching Done.
- Source checks and required consumer handoffs are recorded separately from runtime verification.
