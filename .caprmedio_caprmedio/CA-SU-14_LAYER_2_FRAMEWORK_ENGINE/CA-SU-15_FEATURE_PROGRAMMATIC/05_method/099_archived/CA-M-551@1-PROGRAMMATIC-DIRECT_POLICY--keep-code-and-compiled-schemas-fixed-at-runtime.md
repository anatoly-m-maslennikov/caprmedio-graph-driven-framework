---
identity:
  atom_id: CA-M-551
  ref_id: CA-M-551@1
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  tier: 2
state:
  status: archived
  version: 1
  updated_at: 2026-11-11 05:51:23 +0400
destination:
  file:
    name: CA-M-551@1-PROGRAMMATIC-DIRECT_POLICY--keep-code-and-compiled-schemas-fixed-at-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/099_archived
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-505
---

## Summary

Keep code and compiled schemas fixed at runtime

## Claim

### Prose Claim

Compile schemas, registries and other generated contracts at build time. Load those artifacts at startup and keep them fixed for the life of the process. Apply code or declaration changes by rebuilding and starting the new build. Do not hot reload code or recompile the contracts at runtime. Report missing or invalid build artifacts as errors. Normal source-data synchronization continues under the loaded contracts.
