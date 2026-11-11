---
identity:
  id: CA-P-2866
  ref_id: CA-P-2866@3
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: Archived
  version: 3
  updated_at: 2026-11-11 02:31:44 +0400
destination:
  file:
    name: CA-P-2866@3-TASK--verify-content-extraction-for-admitted-engine-carriers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2811
  - CA-P-2858
---

## Summary

Verify content extraction for admitted Engine carriers

## Objective

Implement and test the adopted content-reader corrections using valid Current/Draft carrier examples, including Engine M514/M515 and the newly reviewed source layouts. Keep source authoring conventions separate from reader bugs. Gather applicable Method Policies and the exact adopted RMEDO before changing code.

## Subtasks

- [ ] Review the admitted reader specification and source examples. (ETA: up to 15 min.)
- [ ] Verify grouped and legacy-compatible Headers and admitted named Role/Form spellings. (ETA: up to 15 min.)
- [ ] Implement the smallest common reader correction and real-interface Evaluation. Split before 20 minutes.
- [ ] Implement the adopted C718 schema/model changes and verify all applicable CAPRMEDO Role/Form content through E675. Split before 20 minutes.
- [ ] Record results and remaining coverage limits. (ETA: up to 15 min.)

## Definition of Done

Valid admitted sources expose their declared content through query_run. Invalid sources and undeclared folders retain their governed handling. Existing fixtures and a real-project canary cover the correction. No mass Atom rewrite substitutes for a reader fix.

## C718 input update

Implement Current R2726 using M500 and M464; deliver D672 and verify E675. Gather the applicable Method Policies before implementation. Check the regenerated Role/Form model and Content schema at image build, then verify the actual query interfaces with valid Current/Draft carriers. The adopted RMEDO holds the specification. Report runtime results separately from this source decision.

## Live acceptance gap

C729 records a live schema failure: no declared Content columns and no compiled Relation registry because the Framework model is outside the Current Project Scope tree. Confirm the authoritative model input, fix the shared compilation boundary and prove it through live query_run; fixture-only parser passes do not close this task. Preserve the Workflow-engine and SQL UPDATE deferrals.
