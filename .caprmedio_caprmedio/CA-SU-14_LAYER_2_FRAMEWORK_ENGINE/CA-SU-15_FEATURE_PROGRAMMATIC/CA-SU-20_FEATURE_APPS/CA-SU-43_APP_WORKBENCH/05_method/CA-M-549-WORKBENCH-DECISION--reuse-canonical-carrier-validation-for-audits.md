---
identity:
  atom_id: CA-M-549
  ref_id: CA-M-549
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-970308648
  - CA-R-970308649
  - CA-R-970308650
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 00:34:40 +0400
destination:
  file:
    name: CA-M-549-WORKBENCH-DECISION--reuse-canonical-carrier-validation-for-audits.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Reuse canonical carrier validation for audits

## Claim

### Prose Claim

Reuse the existing source reader, locator and canonical carrier validation for all three Workbench audit tables. Generate the audit rows from the same selected Current and Draft source scan and the same canonical identity and path values. Reuse existing invalid and unreadable-source diagnostics. Do not add a second reader, a separate consistency Action or source mutation. Keep the tables query-visible and side-effect-free.

