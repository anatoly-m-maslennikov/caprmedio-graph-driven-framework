---
identity:
  atom_id: CA-A-1355
  ref_id: CA-A-1355
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:53:19.986433+00:00'
destination:
  file:
    name: CA-A-1355-FRAMEWORK_ENGINE-CODE_SYNOPSIS--ordinary-workbench-refresh-copies-the-full-inventory.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Ordinary Workbench refresh copies the full inventory

## Claim

### Prose Claim

CA-M-465@29 limits ordinary refresh work to changed sources and affected relations. CA-M-549@2 moves audits out of the lifecycle response path. `FEATURE_WORKBENCH_BACKEND/source_reader.py` still copies and sorts the inventory on ordinary deltas. `FEATURE_WORKBENCH_BACKEND/service.py` creates an `AuditSnapshot` from the full inventory under its refresh lock. Database writes and relation updates are targeted, and audit evaluation runs in its worker. Full snapshot preparation remains on the synchronous path. The review did not measure its share of elapsed time.
