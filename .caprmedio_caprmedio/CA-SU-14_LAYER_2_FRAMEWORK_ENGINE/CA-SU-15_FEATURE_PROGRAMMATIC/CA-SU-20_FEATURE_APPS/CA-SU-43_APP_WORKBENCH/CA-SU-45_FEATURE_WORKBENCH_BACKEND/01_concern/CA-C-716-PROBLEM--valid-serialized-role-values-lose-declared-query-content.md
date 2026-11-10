---
identity:
  id: CA-C-716
  ref_id: CA-C-716
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
    name: CA-C-716-PROBLEM--valid-serialized-role-values-lose-declared-query-content.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
relations:
  concern_about:
  - CA-M-514
  - CA-M-515
---

## Summary

Valid serialized Role values lose declared query content

## Concern

The content reader compares Role/Form strings exactly against business-spelled Declaration filters. Current M514/M515 use the admitted lower_snake_case carrier values `method` and `direct_policy`, so their correct Prose Claims are not exposed by the compiled content schema. The newly prepared normalized Drafts hit the same boundary.

## Details

Preserve the valid source serialization. Verify and fix the common reader/schema adaptation before promotion; do not rewrite source values to conceal the mismatch. The local reader reproduced the gap. No deployed-service failure or code fix is claimed.
