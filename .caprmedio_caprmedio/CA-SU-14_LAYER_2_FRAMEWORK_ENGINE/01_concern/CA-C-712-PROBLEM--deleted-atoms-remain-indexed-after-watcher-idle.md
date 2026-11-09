---
identity:
  id: CA-C-712
  ref_id: CA-C-712
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Problem
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-09 14:24:58 +0400
destination:
  file:
    name: CA-C-712-PROBLEM--deleted-atoms-remain-indexed-after-watcher-idle.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-M-465
  - CA-D-672
  - CA-E-677
---

## Summary

Deleted Atoms remain indexed after watcher idle

## Concern

After the C707 batch updated ten Current Atoms and removed two Current Method carriers and their owned Drafts, query_run still returned M417/M426 as Current although their source paths were absent and workbench_status reported syncing=false. A full Workbench reread removed both rows.

## Details

Reproduce the mixed update/delete batch and correct the incremental indexing path. Do not infer the internal cause from this observation. Preserve actual deletion semantics and add coverage through the existing watcher Evaluation E677. Source retirement was independently verified after the reread; this Problem remains Active until the code fix and acceptance are verified.
