---
identity:
  id: CA-C-727
  ref_id: CA-C-727
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
  updated_at: 2026-11-11 00:22:27 +0400
destination:
  file:
    name: CA-C-727-PROBLEM--implementation-prompt-frontier-has-no-current-workflow-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-R-1843
  - CA-R-1844
  - CA-M-329
  - CA-D-544
  - CA-D-545
---

## Summary

Implementation prompt frontier has no Current Workflow sources

## Concern

P2816 found that 18 of 21 staged shared-context source bindings have no identifiable Current source or explicit replacement, including Workflow O016 and its old Steps. Current D544 names O239, but O239 and the staged O230 are not Current. Six native and ten staged static tests pass while checking the obsolete frontier. R1843 requires affected prompts to remain unadmitted until the Current source graph is independently reviewed.

R1844/M329/D545 also require an all-active-Method projection, while the current implementation procedure selects applicable M Policy guidance and gathers non-Policy Methods separately. Reconcile those source contracts before changing prompt admission. Preserve frozen/native bindings; do not restore retired orchestration or refresh source pins just to pass tests.
