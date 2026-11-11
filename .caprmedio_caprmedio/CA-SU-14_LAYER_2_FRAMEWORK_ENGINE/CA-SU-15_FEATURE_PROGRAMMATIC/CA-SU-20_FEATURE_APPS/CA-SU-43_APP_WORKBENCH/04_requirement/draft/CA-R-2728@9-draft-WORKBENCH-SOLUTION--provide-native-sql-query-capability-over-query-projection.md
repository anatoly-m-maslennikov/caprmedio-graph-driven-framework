---
identity:
  atom_id: CA-R-2728
  ref_id: CA-R-2728@9-draft
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Draft
  version: 9
  updated_at: 2026-11-11 01:59:26 +0400
destination:
  file:
    name: CA-R-2728@9-draft-WORKBENCH-SOLUTION--provide-native-sql-query-capability-over-query-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/draft
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Provide native SQL query capability over query projection

## Claim scope

Queries over the synchronized Atom query Projection.

## Claim

### Prose Claim

A Workspace contains Tabs; each Tab holds one SQL script with semicolon-separated statements. Run executes the whole script or explicitly selected statements in order. Stop at the first failure, retain completed results and effects, and report the failed statement and completed outcomes; do not retry, roll back or recover automatically. Check validates the requested statements without applying changes. Invalid SQL and source-file failures are distinct errors.

SELECT reads the synchronized DuckDB query Projection. Supported SQL UPDATE writes Atom YAML and Markdown through the shared source adapter, never directly to the Projection; DuckDB is a rebuildable cache, not source authority. UPDATE requires an explicit `draft` or `in_place` mode. Draft creates or edits Drafts and leaves Current unchanged; promotion is separate. Editing an existing Draft or using in-place preserves Version and UpdatedAt. Initial metadata for a new Draft is set once by its lifecycle. Declared source properties and Markdown content may be updated; computed columns are read-only. Reject unsupported operations, invalid changes and source write failures explicitly.

A source-writing request explicitly selects the operation `preview` or `apply`; a query-row preview limit is separate. Preview evaluates a mixed script sequentially in a private working copy without source writes, so later statements see earlier proposed changes, and describes every proposed source path, field, old and new value and resulting change. Apply executes one statement at a time, starting the next only after the preceding statement and its source writes complete successfully, and returns complete per-change results and errors. In both modes, later statements observe preceding successful writes through synchronized Projection state or an equivalent source-backed per-run state, never the stale pre-write cache. In Draft mode, reuse one evolving Draft per target within the Run, so a later SELECT or UPDATE sees its preceding Draft changes; do not replace that state with Current. Current remains unchanged, including for queries outside the Run, and promotion remains separate. If synchronization or equivalent state preparation fails, stop and report the error while retaining completed source writes and results; no retry or rollback is performed. No universal additional confirmation is required; caller authorization may persist. Find and replace can propose the same changes through the same source adapter and modes.

Queryable issue tables expose each issue with source path, issue category, available location and diagnostic, and the observed and expected values when applicable. The shared pipeline exposes findings under the predicate owners CA-R-970308648, CA-R-970308649 and CA-R-970308650. They also identify inaccessible or unparseable source files by source path even without an Atom row. SELECT discovers issues; find and replace or SQL UPDATE supplies corrections; preview, apply and refresh complete the flow. These tables do not require a separate AuditConsistency Action.

Expose parsed Header/Content without flattening distinctions. Read-only `query_schema({})` returns all exposed tables and their actual columns, including issue tables, `atoms` (including declared `content.*` and Mode-2 Header Status columns with optional distinct non-null values), and `scope_units`; fetching it neither runs SQL nor reads/writes saved Journal. Status completion can properly escape an actual value from that metadata.

Persistent saving, loading and saved-item listing are separate contracts; unsaved Run, Check and Page have no saved-item side effect.
