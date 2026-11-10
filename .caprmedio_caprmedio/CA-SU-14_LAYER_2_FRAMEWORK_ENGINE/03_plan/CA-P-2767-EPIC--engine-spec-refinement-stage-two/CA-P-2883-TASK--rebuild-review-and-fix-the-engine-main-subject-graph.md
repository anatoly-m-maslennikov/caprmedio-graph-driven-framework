---
identity:
  id: CA-P-2883
  ref_id: CA-P-2883
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 4
  updated_at: 2026-11-10 21:28:00 +0400
destination:
  file:
    name: CA-P-2883-TASK--rebuild-review-and-fix-the-engine-main-subject-graph.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two
relations:
  IS_BLOCKED_BY:
  - CA-P-2858
---

## Summary

Rebuild review and fix the Engine main-subject graph

## Objective

After the full review/fix cycle and source adoption, rebuild the scoped main-subject graph from the actual adopted Current sources. Review the graph against those sources and the latest Operator decisions. Fix findings, then rebuild and recheck until the graph passes. Do not start the implementation Epic before this gate and the current Epic are complete.

## Subtasks

- [x] Review the adopted source selection and confirm obsolete sources are archived. (ETA: up to 15–20 min.)
- [x] Rebuild the main-subject graph and record its exact source selection. (ETA: up to 15–20 min.)
- [x] Independently review the graph for missing, extra, stale, duplicate or wrongly placed topics and references. (ETA: up to 15–20 min.)
- [x] Fix findings in the affected source Drafts and repeat the affected review/adoption checks. (Repeat same-Scope batches, each up to 15–20 min.)
- [x] Rebuild and independently check again after the fixes. (ETA: up to 15–20 min.)
- [x] Record a small Work Report with the passing graph and remaining explicit exclusions.

## Definition of Done

The main-subject graph matches the adopted Current sources in scope, obsolete sources are excluded from current authority, and review findings are fixed and rechecked. Any later accepted source change repeats the affected review/adoption and graph checks before the implementation handoff. Unrelated scopes, existing Archives, benchmark fixtures and deferred plugin/old-Tool work remain preserved.

## Result

The actual Current graph contains 363 RMEDO Atoms and 75 exact main subjects. Independent census/render review passed. Exact admission and governing relation/Tier checks passed; C721/C722 are Resolved with source-only evidence. P2901 records the graph.
