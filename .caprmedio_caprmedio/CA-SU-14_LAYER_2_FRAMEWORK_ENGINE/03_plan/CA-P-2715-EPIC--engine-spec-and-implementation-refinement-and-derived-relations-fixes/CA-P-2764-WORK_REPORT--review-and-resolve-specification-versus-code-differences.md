---
identity:
  id: CA-P-2764
  ref_id: CA-P-2764
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2729
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: CA-P-2764-WORK_REPORT--review-and-resolve-specification-versus-code-differences.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Review and resolve specification versus code differences

## Details

Disposition review accepted code fixes for canonical relations, schema modes, primitive admission and provenance. It retired redundant R2731 without replacing it or changing GRAPH_UI. Missing installer rebuilding and business/lifecycle reconciliation remain in the explicitly excluded perimeter. Generic Policy evaluators were not invented; source declarations and development guidance were separated from executable behavior.
