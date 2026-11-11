---
identity:
  id: CA-P-2740
  ref_id: CA-P-2740@3
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2736
state:
  status: Archived
  version: 3
  updated_at: 2026-11-08 21:55:53 +0400
destination:
  file:
    name: CA-P-2740@3-WORK_REPORT--expose-missing-declared-content-through-query-run.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/archived
author: Anatoly Maslennikov
---

## Summary

Expose missing declared Content through query_run

## Details

Local release 0.4.4.36 installed the reviewed extractor fix; 153 scoped tests passed. The Operator deferred 78 content-unavailable Atoms: 64 PROGRAMMATIC, 12 APPS and O240/O241. No atom_document helper is planned. The approved cold-start mode uses observed YAML Headers and schema-declared Markdown; explicit schema-mode/build-asset verification remains. No full Content coverage or new deployment is claimed.
