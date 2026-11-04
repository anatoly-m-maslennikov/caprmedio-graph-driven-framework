---
atom_id: CA-R-2727
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2727@1-WORKBENCH-RULE--provide-a-simple-web-query-interface-over-the-shared-query-capability.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Provide a simple web query interface over the shared query capability

## Claim scope

The local web interface for queries over the query Projection.

## Claim

### Prose Claim

The web interface **must**:

- provide a SQL text area and Run and Check actions.
- show ordinary result rows, row and column counts, and query errors.
- use the same query capability as the public query interface.
- remain within the existing local application boundary.
- avoid custom TABLE, DOC, or TREE result modes.

