---
identity:
  id: CA-P-2756
  ref_id: CA-P-2756
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
  - CA-P-2719
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 00:18:04 +0400
destination:
  file:
    name: CA-P-2756-WORK_REPORT--fix-relation-materialization-with-the-generated-registry.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Fix relation materialization with the generated registry

## Details

Canonical direct facts and derived inverse facts share one registry. Native GRAPH_TABLE checks verified both directions for the APPS, PROGRAMMATIC and Workbench containment chain. Header Container supplies direct ownership facts. Ambiguous case-colliding names are warned about and omitted.
