---
identity:
  atom_id: CA-R-970308650
  ref_id: CA-R-970308650
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 00:34:40 +0400
destination:
  file:
    name: CA-R-970308650-WORKBENCH-SOLUTION--expose-physical-carrier-mismatches.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose physical carrier mismatches

## Claim

### Prose Claim

For every selected Current or Draft Atom source that exists at scan time, compare its actual filename and location with the declared `file.name` and `file.path`. Expose each mismatch as one query-visible audit row with the Atom identity, the actual source path, the declared values, issue category `physical_carrier_mismatch`, and the observed and expected values. If a source disappears, remove its previous issue row on the next scan; do not claim an actual path for a file that no longer exists. Do not repair, move or rename files.

