---
identity:
  id: CA-P-2987
  ref_id: CA-P-2987
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: canceled
  version: 1
  updated_at: 2026-11-11 17:17:22 +0400
destination:
  file:
    name: CA-P-2987-WORK_REPORT--implement-the-new-atom-lifecycle-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/040_canceled
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Implement the new Atom Lifecycle Tools

## Details

Deployed the retained-history fix. Disposable MCP HTTP calls closed a parent Plan, canceled its active child, and archived the resulting tree. Both moves preserved an older Archived revision byte-for-byte. The older revision was never a Status target.

The Model projection CLI rendered 71 distinct Aspect memberships from the five pinned Formal Claim previews, preserving full paths without Main Subject fallback. The 164 graph tests and 81 lifecycle tests passed. CA-C-730 still tracks formal authoring admission, reopening terminal trees and folder-backed Update.
