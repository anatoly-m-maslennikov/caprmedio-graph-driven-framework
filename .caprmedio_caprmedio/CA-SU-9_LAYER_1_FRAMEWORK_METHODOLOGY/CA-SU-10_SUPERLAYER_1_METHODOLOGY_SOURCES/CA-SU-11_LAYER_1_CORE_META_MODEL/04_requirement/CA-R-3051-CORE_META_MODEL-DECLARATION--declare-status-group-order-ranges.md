---
identity:
  id: CA-R-3051
  ref_id: CA-R-3051
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group
  tier: 3
state:
  status: active
  version: 1
  updated_at: '2026-11-11T19:51:32+04:00'
destination:
  file:
    name: CA-R-3051-CORE_META_MODEL-DECLARATION--declare-status-group-order-ranges.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Status Group order ranges

## Claim

### Prose Claim

Each numbered Status uses the order range of its Status Group or subgroup. Each Current Status belongs to exactly one of its three subgroups.

| Status Group | Subgroup | Statuses | Status Order Number |
| --- | --- | --- | --- |
| Draft | | Draft | 000 |
| Backlog | | Backlog and related Plan Statuses | 001–019 |
| Current | Active | Active | |
| Current | Done | Done, Resolved, and other completion Statuses | 020–039 |
| Current | Canceled | Canceled and other cancellation Statuses | 040–059 |
| Archived | | Archived | 099 |
