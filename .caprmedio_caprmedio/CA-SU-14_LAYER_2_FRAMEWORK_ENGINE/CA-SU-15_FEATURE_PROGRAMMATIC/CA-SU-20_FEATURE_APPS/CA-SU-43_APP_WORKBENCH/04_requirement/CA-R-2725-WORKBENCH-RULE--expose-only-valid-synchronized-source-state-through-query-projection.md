---
atom_id: CA-R-2725
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2725-WORKBENCH-RULE--expose-only-valid-synchronized-source-state-through-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
updated_at: 2026-11-05 05:54:01 +0400
---
## Summary

Expose only valid synchronized source state through the query Projection

## Claim scope

The correspondence between selected governed Atom sources and their query Projection rows.

## Claim

### Prose Claim

The query Projection **must**:

- expose a complete committed state from valid selected sources.
- make valid selected sources available without exposing a partial update.
- exclude an invalid, unreadable, or unstable ordinary Atom source and its derived data; an older state of that source **must not** remain queryable as current.
- leave unrelated valid sources queryable when another source is excluded.
- report a source-file error, with its path and available location information, through stderr rather than as a result row.
- skip an excluded source without automatic retry; a later actual source change may be considered on a later refresh.
- remain distinct from source deletion: a source-file error is not proof that the source was deleted.

An invalid Current Scope Unit Declaration must not produce valid or partial projected structure.
