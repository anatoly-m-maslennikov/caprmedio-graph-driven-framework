---
identity:
  id: CA-P-2762
  ref_id: CA-P-2762
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Aspect/Engineering/Traceability
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2737
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: CA-P-2762-WORK_REPORT--map-adopted-atoms-to-implementation-modules.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes
author: Anatoly Maslennikov
---

## Summary

Map adopted Atoms to implementation modules

## Details

Mapped the selected PROGRAMMATIC, APPS, Workbench, backend, frontend and Codex Extension sources to actual modules, tests, process guidance or structural declarations. Current pins were reviewed rather than stamped blindly. Policies and called-only sources were removed from implementation headers. The missing older installer remains excluded and is recorded by I6; R2731 was retired as redundant. Static maps do not by themselves prove runtime behavior.
