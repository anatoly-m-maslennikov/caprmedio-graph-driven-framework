---
identity:
  id: CA-P-2867
  ref_id: CA-P-2867@1
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 04:02:58 +0400
destination:
  file:
    name: CA-P-2867@1-TASK--repair-readability-and-admit-all-eligible-engine-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2854
---

## Summary

Repair readability and admit all eligible Engine Atoms

## Objective

Admit all Current and Draft ENGINE Atoms to the review inventory, including files absent from query_run and files whose declared content is not exposed. Remove the prior 69-MED hold. Keep older non-Workbench Tools and Codex plugin work deferred; preserve benchmark fixtures and existing Archives.

## Subtasks

- [x] Fix the 69 formerly held MED layouts in place without changing frontmatter, wording, Versions or timestamps. (ETA per same-Scope batch: up to 15–20 min.)
- [x] Verify their declared Claims with the real source reader. (ETA: up to 15 min.)
- [x] Repair other unambiguous eligible Current/Draft layouts mechanically. Split before 20 minutes.
- [ ] Reconcile every eligible file with query visibility and declared-content coverage. Split per Scope Unit and before 20 minutes.
- [ ] Classify source-layout, reader-admission, schema and invalid-data gaps separately; record exact follow-up work. (ETA per batch: up to 15 min.)
- [ ] Add every admitted source to the next refinement batches. (ETA per Scope Unit: up to 15 min.)

## Definition of Done

Every eligible Current/Draft source is accounted for and has a readable or explicitly diagnosed disposition. Mechanical changes preserve values and history. Missing runtime or schema support is not presented as a successful deployed query_run test.
