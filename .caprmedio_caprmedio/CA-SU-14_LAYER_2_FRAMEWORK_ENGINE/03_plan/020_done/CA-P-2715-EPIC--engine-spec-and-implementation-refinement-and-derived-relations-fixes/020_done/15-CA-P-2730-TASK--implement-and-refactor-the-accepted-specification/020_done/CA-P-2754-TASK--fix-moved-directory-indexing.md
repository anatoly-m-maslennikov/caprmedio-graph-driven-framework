---
identity:
  id: CA-P-2754
  ref_id: CA-P-2754
context:
  container:
    atom: CA-P-2730
  role: Plan
  form: Task
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 2
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: CA-P-2754-TASK--fix-moved-directory-indexing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/15-CA-P-2730-TASK--implement-and-refactor-the-accepted-specification/020_done
author: Anatoly Maslennikov
relations: {}
---

## Summary

Fix moved-directory indexing

## Details

1. Reproduce the large-move failure (15 min).
2. Correct affected-subtree handling and add its regression (20 min).
3. Review and fix boundary handling (10 min).
4. Verify the performance gate and release (20 min).
