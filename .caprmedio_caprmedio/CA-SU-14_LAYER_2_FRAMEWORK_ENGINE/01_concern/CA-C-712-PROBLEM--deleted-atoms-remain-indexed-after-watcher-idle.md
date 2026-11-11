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
  status: Resolved
  version: 2
  updated_at: 2026-11-11 03:05:37 +0400
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


## Resolution

Verified on the running 0.4.4.40 image (c6e5cfb3e431) on 11 November 2026. The retained real-project mixed canary updates ten Current Atoms and removes two Current Methods and their two numbered Drafts. All ten updated rows were visible and all four deleted rows absent while syncing=false, without reread, in 0.284 s from the start of mutation. Owned source and index cleanup passed.

The current delta implementation unions old/new carrier keys, deletes the previous rows and inserts surviving replacements in one transaction. Existing direct and polling-watcher integration tests cover the mixed shape; the live image adds native-watcher acceptance. No additional runtime patch was needed to pass this reproduction; the original older runtime's internal cause remains unproven. This resolves the observed stale-row behavior, not unrelated model admission or general performance acceptance.

Evidence: .caprmedio_tmp/CA-P-2791/CA-P-2813/live-mixed-canary/mixed-latest.json and mixed-live-corrected-timings.log. Retained test: test_workbench_live_mixed_canary.py.
