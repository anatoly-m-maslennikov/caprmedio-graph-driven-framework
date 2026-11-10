---
identity:
  id: CA-P-2901
  ref_id: CA-P-2901
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-10 21:28:00 +0400
destination:
  file:
    name: CA-P-2901-WORK_REPORT--rebuild-and-check-current-engine-main-subjects.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2883
author: Anatoly Maslennikov
---

## Summary

Rebuild and check Current Engine main subjects

## Details

The actual Current-source graph has 363 RMEDO Atoms and 75 exact main subjects. Independent rendering/census review passed with zero missing, unexpected, duplicate or parse failures. Exact Scope/Role/Form admission passed for all 363 sources; 375 governing relations passed Tier/ancestry and cycle checks.

The source manifest pins paths and hashes. Exclusions are explicit: 593 old-Tool RMEDO files, 18 native-plugin sources, the 501-source benchmark, three held old-Tool declarations and mixed native E684, whose shared clause is Current E819. No Draft, Archive, Definition prose or runtime query proof is presented.
