---
atom_id: CA-M-464
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 3
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2723
  - CA-R-2726
  - CA-R-2728
  - CA-R-2724
carrier_destination:
  file:
    name: CA-M-464@3-WORKBENCH-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 05:16:33 +0400
---

## Summary

Preserve governed Atom data and reuse native SQL.

## Claim scope

In-memory reading, schema Projection, and query semantics for Current and Draft Atom carriers excluding Archived carriers.

## Claim

### Prose Claim

The DuckDB Projection reader must read Current and Draft Atom carriers, excluding Archived carriers, into memory. Every Current status, including Done and Canceled, remains in that inventory. It parses YAML and Markdown according to in-memory schema Projections of the relevant current model Declarations. It must not use a generic CFEL evaluator or a prose interpreter.

The in-memory schema Projections identify admitted Header and Content Properties, their Markdown structure, and declared Relation Types. They remain in memory and do not create JSON files or a third public database table. Parent paths are derived from Property paths.

Only Current Scope Unit Declarations establish the current Scope Unit inventory. A Draft Declaration remains a queryable Atom but does not establish a current Scope Unit.

Source Atoms retain direct Relations only. Each indexed object row carries that object's outgoing direct and declared-derived Relations. For `Task IS_CONTAINED_BY Epic`, the Task row carries `IS_CONTAINED_BY` and the Epic row carries the derived `CONTAINS`. A source or relevant Declaration change refreshes every affected outgoing-relation row, graph mapping, and row hash, including rows for unchanged target sources. This does not edit those sources or increment their Versions. Each public row hash includes its materialized Relations. Each in-memory schema Projection row uses the same `hash` rule: hash its deterministic canonical row value with `hash` excluded.

Use DuckDB for SQL and the DuckPGQ community extension for SQL/PGQ graph queries. Register an in-memory property graph over the indexed objects and their materialized registered Relation facts. Reuse DuckPGQ for pattern matching and traversal instead of implementing a CAPRMEDIO traversal engine or requiring a custom `expand()` API.

Reachability queries must still satisfy the Relation-expansion requirement: resolve an unambiguous typed seed, follow the selected Relation Types and directions, include the seed and each reachable typed reference once, and terminate on cycles. Use native SQL and SQL/PGQ to produce that result; joins or subqueries fetch the selected objects. Querying a declared inverse uses its materialized fact and does not synthesize it again. The Projection does not add a SQL-like parser, evaluate Formal Claims, or adopt graph algorithms beyond the selected query requirements.
