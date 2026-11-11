---
identity:
  id: CA-P-2841
  ref_id: CA-P-2841
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 5
  updated_at: 2026-11-09 21:20:12 +0400
destination:
  file:
    name: CA-P-2841-WORK_REPORT--2840.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2767-EPIC--engine-spec-refinement-stage-two/020_done
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2840
---

## Summary

Merge scoped Atoms by Summary

## Details

Reviewed the full captured Current RMEDO source frontier. Repaired 44 legacy R/O layouts without rewriting their words; corrected 27 topic sets and retained 17 before merge review. Independent same-Scope reviews and final preservation/reference checks preceded adoption.

Applied 33 Summary-merge groups in two verified batches: 48 predecessor contracts retired, 81 Current records adopted, including the new M513 merge Method, new R3013 registry Requirement and resolved C713. The final batch contains 66 adopted records, 42 retirements and 107 predecessor archives. Existing Summaries and Roles stayed unchanged; R3013 uses a new identity for its changed Summary. C713 permitted only references in D366/D512/E525 outside the Epic scope; exact body/metadata checks verify that boundary.

Fresh query readback after full reread verified every adopted ID, Version, path, Status and declared Claim/Operation; all retired IDs are absent from Current and no live nonreplacement relation points at them. All 48 Scope Units, the 500 benchmark Atoms, 69 held MED and 69,409 original protected Draft/Archive files are preserved. Six merge groups remain explicitly held because their 20 direct Evaluation consumers are deferred; R1076 and M153 stay separate as outcome and supporting procedure. Thin summary-merges.tsv records each disposition.

C712 remains an implementation defect: full reread is recovery, not an incremental-delete fix. I7–I9 and existing module pins remain factual code observations pending P2791. Concurrently adopted M514/M515 are preserved; live query confirms their lowercase Header values but missing Claim extraction. P2791 must handle that consumer issue before policy compilation. No runtime code, implementation test, release, commit or push was performed in this specification pass.
