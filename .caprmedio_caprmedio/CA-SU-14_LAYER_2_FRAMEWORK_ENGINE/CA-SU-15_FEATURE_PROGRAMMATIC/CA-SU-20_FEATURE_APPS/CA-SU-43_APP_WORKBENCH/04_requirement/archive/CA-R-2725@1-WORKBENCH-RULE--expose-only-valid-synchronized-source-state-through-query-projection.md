---
atom_id: CA-R-2725
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
    name: CA-R-2725@1-WORKBENCH-RULE--expose-only-valid-synchronized-source-state-through-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Expose only valid synchronized source state through the query Projection

## Claim scope

The correspondence between governed Atom sources and their query Projection rows.

## Claim

### Prose Claim

The query Projection **must**:

- expose one committed state produced from completed source synchronization work.
- reconcile created, changed, moved, renamed, deleted, and repaired canonical carriers so their derived data reflects the latest valid source state.
- remove an invalid changed carrier's indexed data and owned derived data; an older valid version of that same current file **must not** remain queryable.
- exclude an unreadable carrier or a carrier that changes during stable capture with its owned derived data; the error does not prove that the source was deleted.
- restore a carrier's derived data only after a later actual file edit, move, or new observed source state is validly read.
- leave unrelated valid carriers queryable when one carrier is invalid, unreadable, or changes during capture.
- report source-file errors, with the source path and available location information, through stderr only; source-file errors **must not** appear as result rows.
- skip a source-file error and continue with other valid sources; it must not cause automatic resubmission of the same failed input.
- leave a failed synchronization transaction uncommitted, report failure through stderr and to its caller, and expose no partial or successful result.

