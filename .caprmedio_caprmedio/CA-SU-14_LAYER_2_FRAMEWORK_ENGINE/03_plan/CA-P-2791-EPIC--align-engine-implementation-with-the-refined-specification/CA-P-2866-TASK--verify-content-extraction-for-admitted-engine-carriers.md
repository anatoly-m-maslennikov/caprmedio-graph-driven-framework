---
identity:
  id: CA-P-2866
  ref_id: CA-P-2866
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
  status: Done
  version: 8
  updated_at: 2026-11-11 07:39:42 +0400
destination:
  file:
    name: CA-P-2866-TASK--verify-content-extraction-for-admitted-engine-carriers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
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

- [x] Review the admitted reader specification and source examples. (ETA: up to 15 min.)
- [x] Verify grouped and legacy-compatible Headers and admitted named Role/Form spellings. (ETA: up to 15 min.)
- [x] Implement the smallest common reader correction and real-interface Evaluation. Split before 20 minutes.
- [x] Implement the adopted C718 schema/model changes and verify all applicable CAPRMEDO Role/Form content through E675. Split before 20 minutes.
- [x] Verify inherited dependent properties and constraints across arbitrary declared specialization chains. (ETA: up to 15 min.)
- [x] Record results and remaining coverage limits. (ETA: up to 15 min.)

## Definition of Done

Valid admitted sources expose their declared content through query_run. Invalid sources and undeclared folders retain their governed handling. Existing fixtures and a real-project canary cover the correction. No mass Atom rewrite substitutes for a reader fix.

## C718 input update

Implement Current R2726 using M500 and M464; deliver D672 and verify E675. Gather the applicable Method Policies before implementation. Check the regenerated Role/Form model and Content schema at image build, then verify the actual query interfaces with valid Current/Draft carriers. The adopted RMEDO holds the specification. Report runtime results separately from this source decision.

## Live acceptance gap

C729 records a live schema failure: no declared Content columns and no compiled Relation registry because the Framework model is outside the Current Project Scope tree. Confirm the authoritative model input, fix the shared compilation boundary and prove it through live query_run; fixture-only parser passes do not close this task. Preserve the Workflow-engine and SQL UPDATE deferrals.


## Approved discovery correction

The Operator selected all Atoms in `.caprmedio_<project name>`, rather than a hard-coded Core path. M464 and E677 now record the Current/Draft discovery boundary and acceptance. Implement and verify discovery, select Declarations through query_run, then verify schema and relation generation from their Formal Claims on every image build. Current Scope structure remains a separate Declaration-derived result. C729 stays Active until live image/query acceptance proves the correction.


## Declaration review handoff

The real all-root capture generated 2,292 Content columns from broad wildcard declarations, including old presentation headings. The isolated replacement image exceeded the cold-schema query deadline and was removed; the healthy serving image was preserved. The Operator assigned declaration issues to CA #5. That handoff includes generic inheritance through arbitrary specialization chains and dependent/nested properties. The attempted compiler-only restriction was withdrawn; projection creation must follow the effective declared model. Continue independent fixture and insertion checks while source interpretation is reviewed. C729 remains Active.


## Formal-input acceptance

Implement the Operator-approved formal-only generation boundary under M500/M509 and E675. Cover schema and Relation generators, then check image-build outputs. Do not infer model facts from Header Topics, prose or comments; retain factual Header Mode 2 independently. Keep declaration correction and general inheritance review with CA #5.

## Build-only schema follow-up

- [x] Load the generated schema and canonical Relation registry from the image. Remove the runtime compiler paths. (ETA: split into up to 20 min subtasks.)
- [x] Test live Declaration edits and full reread against the same image; verify the change takes effect after an image rebuild. Check ordinary data refresh separately. (ETA: up to 20 min.)
- [x] Audit MCP and PROGRAMMATIC for remaining opt-in reload paths and obsolete RMED; fix verified conflicts under CA-M-551. Keep Workflow-engine work deferred. (ETA: up to 20 min.)

## Verified acceptance

P2949 and P2952 record the real Project candidate and two-image Mode 1/2 checks. Both query interfaces exercised the built asset. The real-Project candidate exposes M514, M515 and Draft Formal Claims. C729 remains open for the installed-service check in P2818.
