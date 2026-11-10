---
identity:
  atom_id: CA-M-505
  ref_id: CA-M-505
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control <+ Code Hot Reload
  tier: 2
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-505-PROGRAMMATIC-DIRECT_POLICY--disable-code-hot-reload-by-default.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Disable code hot reload by default

## Claim



### Prose Claim
Every code hot-reload mechanism must have an explicit off mode and start disabled by default, including runtime and development launch paths. Enable it only through explicit opt-in. Disabled mode applies code changes through a normal process/container restart and must not keep reload-only child processes or watchers. Source-data indexing is a separate capability; this Policy does not disable Workbench source synchronization.
