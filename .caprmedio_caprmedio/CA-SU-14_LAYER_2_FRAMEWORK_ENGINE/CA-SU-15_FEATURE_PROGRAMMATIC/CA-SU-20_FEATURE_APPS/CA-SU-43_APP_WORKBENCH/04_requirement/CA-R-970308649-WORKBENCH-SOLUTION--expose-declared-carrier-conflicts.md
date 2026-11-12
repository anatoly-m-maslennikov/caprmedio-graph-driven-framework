---
identity:
  atom_id: CA-R-970308649
  ref_id: CA-R-970308649
context:
  container:
    scope_unit: CA-SU-43
  role: requirement
  form: solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: active
  version: 2
  updated_at: '2026-11-12T01:42:12.539601+00:00'
destination:
  file:
    name: CA-R-970308649-WORKBENCH-SOLUTION--expose-declared-carrier-conflicts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose declared carrier conflicts

## Claim

### Prose Claim

For every readable selected Atom, including loaded Archives, compare its declared `file.name` and `file.path` with the other declared properties that identify its carrier. Derive expected values only from the existing canonical declared carrier rules. Expose each conflict as one query-visible audit row with the Atom identity, source path, issue category `declared_carrier_inconsistency`, observed and expected or related values, and the diagnostic location when available. If no applicable canonical rule exists, report `missing_carrier_rule` instead of guessing a filename grammar. Do not infer a replacement value, change the source file, or emit a row when no conflict exists.

