---
atom_id: CA-D-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2724
  - CA-R-2728
  - CA-R-2729
carrier_destination:
  file:
    name: CA-D-673@1-WORKBENCH-ENG_DECISION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The shared SQL connector and its MCP Run and Check operations over the DuckDB Projection.

## Claim

### Prose Claim

MCP Run and Check must accept the same SQL input and use the same native SQL connector. The connector follows DuckDB SQL semantics; it does not add a second query language or a custom CFEL parser.

Each MCP or web Run/Check request invokes that connector directly and
synchronously. This delivery adds no planner, scheduler, workflow or
orchestrator job, queue, or second executor.

The connector registers the native table helper
`expand(seed, relations, seed_kind := NULL)`. `seed` is any reference string: a
bare Atom ID without `seed_kind` resolves to the Current Atom, while a Scope Unit
uses its name with `seed_kind` `'Scope Unit'`. `relations` is a SQL list of
registered Relation Type names. The only `seed_kind` literals are `'Atom'` and
`'Scope Unit'`; no encoded reference syntax or parser is added. The helper returns
exactly `kind VARCHAR` and `ref VARCHAR`, not fetched objects or relation records.
For an Atom result, join `kind = 'Atom'` and `ref = atoms.ref`; for a Scope Unit
result, join `kind = 'Scope Unit'` and `ref = scope_units.name`. It reads nested
direct typed facts with native DuckDB operations and adds no relation table or view.

Run must return the complete query result, column names and types, row count, and column count. Check must return whether the query is valid and, when valid, its exact row count and column count; an invalid query returns its error. Query errors are returned to the caller and are not converted to an empty successful result.

For a successful request, the shared connector result has these fields; MCP and the
web page map them directly rather than defining distinct result formats:

| Operation | Fields and values |
| --- | --- |
| Run | `columns`: ordered list of `{name: string, type: string}` from the executed DuckDB result; `rows`: all result rows in that column order; `row_count`: exact integer row count; `column_count`: exact integer column count. |
| Check | `valid`: `true`; `row_count`: exact integer row count; `column_count`: exact integer column count. |

`columns`, `rows`, and both counts come from the same Run execution. Check obtains
its counts by executing the exact SQL read-only, but does not return substituted rows.
An invalid Run or Check is a query error through the caller's existing error path,
not a success envelope with invented error, status, or partial-result fields.

Neither operation may silently add a limit or truncate rows. If a transport cannot carry the complete result, the response must report that limitation instead of claiming a complete result. Source-file errors remain a separate stderr channel with the source path, error, and available line or column; they are not fake result rows. Run and Check do not modify Atom sources or the Projection.

The connector delivers ordinary native SQL results, not custom result views or a renderer.

