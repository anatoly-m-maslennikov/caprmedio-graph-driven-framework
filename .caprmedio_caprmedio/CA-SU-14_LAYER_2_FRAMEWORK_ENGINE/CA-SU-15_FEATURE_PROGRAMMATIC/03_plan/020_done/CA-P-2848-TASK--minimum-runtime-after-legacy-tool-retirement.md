---
identity:
  id: CA-P-2848
  ref_id: CA-P-2848
context:
  container:
    scope_unit: CA-SU-15
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 23:57:47 +0400
destination:
  file:
    name: CA-P-2848-TASK--minimum-runtime-after-legacy-tool-retirement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/020_done
author: Anatoly Maslennikov
---

## Summary

Minimum runtime after legacy Tool retirement

## Objective

Retire legacy Tool code and retain Workbench, standalone Subject/Topics builders, host local/public releases, and only the shared dependencies needed by those entry points.

## Definition of Done

Remove unused providers, mutation/query wrappers, selected execution, orchestration and worker paths with their exclusive tests and stale package copy. Preserve retained parsing, isolation, diagnostics, Journal append and release behavior; verify the changed boundaries with focused checks. Record the actual results and remaining gaps in the Work Report. Deployment and source Atom reconciliation are separate work.
