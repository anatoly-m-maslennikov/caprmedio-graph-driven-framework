---
identity:
  id: CA-P-2996
  ref_id: CA-P-2996
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
  status: Done
  version: 1
  updated_at: 2026-11-11 19:40:40 +0400
destination:
  file:
    name: CA-P-2996-WORK_REPORT--verify-declaration-driven-lifecycle-placement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2934
author: Anatoly Maslennikov
---

## Summary

Verify declaration-driven lifecycle placement

## Details

In a disposable Project, query_run selected all five native placement Claims by Main Subject and Delivery Role. Their source hashes matched the released image. The public MCP calls moved an Epic to Done, canceled its open Task in the Epic directory, and archived both in the owning Scope Unit’s shared Plan archive.

The build compiler now derives Status folder names from the formal Status Order Numbers and Delivery path templates. All 102 lifecycle tests passed, including changed source IDs and folder numbers. The native compile matched all 16 source hashes. The four remaining authoring tools still require the admission rules tracked in CA-C-730.
