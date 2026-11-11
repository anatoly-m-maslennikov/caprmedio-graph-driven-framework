---
atom_id: CA-M-505
ref_id: CA-M-505@1
container:
  scope_unit: CA-SU-15
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 2
status: Archived
version: 1
updated_at: 2026-11-07 04:34:07 +0400
carrier_destination:
  file:
    name: CA-M-505@1-PROGRAMMATIC-ENG_POLICY--disable-code-hot-reload-by-default.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archived
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Disable code hot reload by default

## Claim

### Prose Claim

Every code hot-reload mechanism must have an explicit off mode and start disabled by default, including runtime and development launch paths. Enable it only through explicit opt-in. Disabled mode applies code changes through a normal process/container restart and must not keep reload-only child processes or watchers. Source-data indexing is a separate capability; this Policy does not disable Workbench source synchronization.
