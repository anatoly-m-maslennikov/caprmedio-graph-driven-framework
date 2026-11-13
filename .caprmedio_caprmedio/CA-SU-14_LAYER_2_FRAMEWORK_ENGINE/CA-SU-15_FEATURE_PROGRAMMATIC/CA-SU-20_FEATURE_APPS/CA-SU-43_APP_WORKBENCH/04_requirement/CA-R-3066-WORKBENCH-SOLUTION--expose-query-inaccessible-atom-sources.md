---
identity:
  atom_id: CA-R-3066
  ref_id: CA-R-3066
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
  updated_at: '2026-11-12T01:42:07.020152+00:00'
destination:
  file:
    name: CA-R-3066-WORKBENCH-SOLUTION--expose-query-inaccessible-atom-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose query-inaccessible Atom sources

## Claim

### Prose Claim

Expose parse and current-schema issues for the selected Atom carriers, including loaded Archive files. Record unreadable or unparseable candidates in `atom_parse_issues` even when they have no `atoms` row. Record current-schema violations in `atom_schema_issues`. Keep parseable files visible in `atoms`, and report any discrepancy between declared content and its query projection. Include the Atom identity when available, the source path, the category and the diagnostic or available location. A diagnostic must leave the source file unchanged.
