---
identity:
  atom_id: CA-R-2725
  ref_id: CA-R-2725@6
context:
  container:
    scope_unit: CA-SU-43
  role: requirement
  form: direct_policy
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: archived
  version: 6
  updated_at: '2026-11-12T01:42:02.762501+00:00'
destination:
  file:
    name: CA-R-2725@6-WORKBENCH-DIRECT_POLICY--expose-only-valid-synchronized-source-state-through-the-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/099_archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
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
- exclude an ordinary source that cannot be parsed or read stably and remove any older query row for that file. Keep parseable files queryable and report violations of the current declared schema separately.
- leave unrelated valid sources queryable when another source is excluded.
- report source-file errors with path and available location information through stderr and the queryable issue tables. Publish audits asynchronously after source rows commit. Expose audit progress and the elapsed time of the most recent audit so users can identify pending diagnostics.
- skip an excluded source without automatic retry; a later actual source change may be considered on a later refresh.
- remain distinct from source deletion: a source-file error is not proof that the source was deleted.

An invalid Current Scope Unit Declaration must not produce valid or partial projected structure.

Report duplicate Atom IDs and Versions among selected Current and Archived rows. Drafts and Backlog rows are outside that duplicate check. Archive duplicate coverage is limited to the loaded folders and any exact archived files included in `atoms`.
