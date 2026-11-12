---
identity:
  id: CA-P-2982
  ref_id: CA-P-2982
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 15:42:58 +0400
destination:
  file:
    name: CA-P-2982-WORK_REPORT--implement-the-new-atom-lifecycle-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Implement the new Atom Lifecycle Tools

## Details

The Engine reads stable receiving Scope Unit IDs in formal Role/Form permissions. The native read returned 84 pairs across 12 Delegations. Lifecycle checks the exact pair for Solution, Direct Policy and Approach Policy. New Analysis and Advisory Carriers use `analysis_and_advisory`. Draft and Archived Carriers use their owning Scope Unit's shared Role folders.

The staged MCP gateway passed all six Tools, including nested Plan closure, refusal to reactivate a child inside a terminal Plan, and child-first Workflow archival. Terminal Plan descendants kept their Status, Version and Updated At. Moving a parent refreshed Current descendant destinations and preserved attached assets and existing shared archives.

Public registration remains pending broader local admission and folder-backed Update handling. The tested terminal cascade covers closure. Reopening a terminal Plan tree remains unsupported when the child-first order conflicts with the terminal-parent invariant. The Workbench registry build selected an installed CA-R-1498@17 copy instead of native CA-R-1498@18, so that asset did not include `RECURSIVELY_CONTAINS`.
