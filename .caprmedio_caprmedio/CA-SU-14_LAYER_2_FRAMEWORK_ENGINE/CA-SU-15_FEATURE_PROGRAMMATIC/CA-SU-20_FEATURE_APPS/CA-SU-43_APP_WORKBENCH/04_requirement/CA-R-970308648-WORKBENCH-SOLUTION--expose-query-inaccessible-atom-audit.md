---
identity:
  atom_id: CA-R-970308648
  ref_id: CA-R-970308648
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
    name: CA-R-970308648-WORKBENCH-SOLUTION--expose-query-inaccessible-atom-audit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose query-inaccessible Atom sources

## Claim

### Prose Claim

The Workbench query Projection must expose a query-visible audit table for every selected Current or Draft Atom source whose declared content cannot be read through `query_run`.

Each row must include the Atom identity when available, the source path, the issue category `query_inaccessible_atom`, and the reader diagnostic or location. A source with no readable Atom row must still be reportable by its path. The table must not expose stale indexed data or repair the source. Readable Atoms remain in the normal query tables.

