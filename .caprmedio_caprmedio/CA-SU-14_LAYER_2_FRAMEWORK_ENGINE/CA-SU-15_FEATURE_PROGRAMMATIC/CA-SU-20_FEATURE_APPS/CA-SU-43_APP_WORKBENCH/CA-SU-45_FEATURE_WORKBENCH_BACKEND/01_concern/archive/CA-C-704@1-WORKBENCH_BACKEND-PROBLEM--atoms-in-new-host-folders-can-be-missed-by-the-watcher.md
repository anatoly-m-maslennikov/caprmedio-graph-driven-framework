---
atom_id: CA-C-704
ref_id: CA-C-704@1
container:
  scope_unit: CA-SU-45
role: Concern
form: Problem
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  concern_about:
  - CA-M-465
  - CA-E-780
status: Archived
version: 1
updated_at: 2026-11-06 20:37:19 +0400
carrier_destination:
  file:
    name: CA-C-704@1-WORKBENCH_BACKEND-PROBLEM--atoms-in-new-host-folders-can-be-missed-by-the-watcher.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
# Summary

Atoms in new host folders can be missed by the watcher

## Concern

A Draft created inside a newly host-created nested folder did not become query-visible within 90 seconds in the historically reproduced running Workbench runtime. The technical change log recorded directory create/remove observations but no child-file event.

## Evidences

The CA-P-2710 Epic `watcher-latency-review.md` records the probe and its result. CA-E-780 is the linked watcher regression Evaluation.

## Blast radius

Queries can omit Atoms created in new host folders.
