---
identity:
  id: CA-P-2858
  ref_id: CA-P-2858@3
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
  status: Archived
  version: 3
  updated_at: 2026-11-10 06:12:11 +0400
destination:
  file:
    name: CA-P-2858@3-TASK--adopt-reviewed-additions-and-hand-off-implementation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2857
---

## Summary

Adopt reviewed additions and hand off implementation

## Objective

Adopt only accepted specification corrections from the full Engine review cycle using the active lifecycle rules. Check successor identities, IS_REPLACEMENT_FOR lineage, incoming references, preserved coverage and source locations. Promote accepted Drafts, archive exact predecessors and obsolete merged/replaced Atoms, and repair affected Current references. Hand the adopted baseline to P2883 for the main-subject graph gate; runtime implementation remains separate.

## Subtasks

- [ ] Review the next accepted same-Scope batch and its reference plan. (ETA: up to 15–20 min.)
- [ ] Promote or replace the accepted sources through the authorized source workflow. Split before 20 minutes.
- [ ] Archive obsolete sources after verifying survivor coverage and replacement/reference treatment. (ETA: up to 15–20 min.)
- [ ] Verify actual source identities, versions, content and references. (ETA: up to 15–20 min.)
- [ ] Use query readback where available and record reader/runtime limits separately from normative source correctness.
- [ ] Record a small Work Report and hand the exact baseline to P2883. (ETA: up to 15 min.)

## Definition of Done

Accepted Drafts are promoted and obsolete merged/replaced Atoms are archived, with verified lineage, survivor coverage and reference treatment. Unresolved sources stay explicitly recorded. Existing Archives remain unchanged apart from authorized new predecessor archives. No runtime readiness, implementation or release is claimed.
