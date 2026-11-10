---
identity:
  id: CA-C-717
  ref_id: CA-C-717
context:
  container:
    scope_unit: CA-SU-45
  role: Concern
  form: Problem
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 04:02:58 +0400
destination:
  file:
    name: CA-C-717-PROBLEM--valid-atom-filenames-are-rejected-before-header-parsing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
relations:
  concern_about:
  - CA-C-526
  - CA-C-527
  - CA-C-533
  - CA-C-283
---

## Summary

Valid Atom filenames are rejected before Header parsing

## Concern

The filename marker matcher greedily selects later words such as `runtime-draft` or a Plan ID mentioned in the slug as if they were the Atom Role. A valid Header then cannot qualify the source, because candidate selection requires the guessed filename Role to match first.

## Details

Current examples include C526, C527, C533 and C283. Source layouts should not be renamed merely to avoid ordinary slug words. P2859 owns the narrow reader correction; undeclared source directories remain a separate boundary.
