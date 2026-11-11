---
identity:
  id: CA-P-2740
  ref_id: CA-P-2740@2
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
  version: 2
  updated_at: 2026-11-08 19:50:47 +0400
destination:
  file:
    name: CA-P-2740@2-WORK_REPORT--expose-missing-declared-content-through-query-run.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/archived
author: Anatoly Maslennikov
---

## Summary

Expose missing declared Content through query_run

## Details

Local release 0.4.4.36 installed the reviewed extractor fix. Its 153 scoped tests passed with no failures or skips. Live query_run verified content.operation, root Scope Unit CA-SU-00, header_context_container JSON and IS_WORK_REPORT_FOR. Full source fetching is still incomplete: 64 local PROGRAMMATIC candidates have no exposed Content, and O240/O241 still expose no Operation. The Operator decision about cache-only atom_document(reference) access is pending. No bulk rewrite or full Content coverage is claimed. Release cleanup retained one unproven old image; deployment itself succeeded.
