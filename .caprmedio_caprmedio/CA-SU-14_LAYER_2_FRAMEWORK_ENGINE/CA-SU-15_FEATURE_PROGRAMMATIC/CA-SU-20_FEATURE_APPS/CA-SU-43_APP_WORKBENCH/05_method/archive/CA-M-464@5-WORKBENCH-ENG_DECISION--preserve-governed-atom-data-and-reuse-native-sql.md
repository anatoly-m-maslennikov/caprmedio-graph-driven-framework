---
atom_id: CA-M-464
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 5
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
    name: CA-M-464@5-WORKBENCH-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 16:59:55 +0400
---

## Summary

Preserve governed Atom data and reuse native SQL.

## Claim scope

Direct file reading and native query semantics for Current and Draft Atom carriers excluding Archived carriers.

## Claim

### Prose Claim

The DuckDB Projection reader must read Current and Draft Atom carriers, excluding Archived carriers, into the derived DuckDB database. Every Current status, including Done and Canceled, remains in that inventory. Parse YAML and Markdown directly using the existing safe YAML reader and CommonMark headings. Do not compile model Declarations into a reader schema, evaluate generic CFEL, or interpret prose.

Preserve all parsed Header properties, the original Markdown body, and real heading paths without a fixed heading list or Form validation. Parent paths are derived from Property path segments. The reader creates no intermediate schema, JSON file, or third public database table.

Only Current Scope Unit Declarations establish the current Scope Unit inventory. A Draft Declaration remains a queryable Atom but does not establish a current Scope Unit.

Source Atoms retain direct Relations only. Each indexed object row carries that object's outgoing direct and declared-derived Relations. For `Task IS_CONTAINED_BY Epic`, the Task row carries `IS_CONTAINED_BY` and the Epic row carries the derived `CONTAINS`. A source or relevant Declaration change refreshes every affected outgoing-relation row, graph mapping, and row hash, including rows for unchanged target sources. This does not edit those sources or increment their Versions. Each public row hash includes its materialized Relations.

Use DuckDB for SQL and the DuckPGQ community extension for SQL/PGQ graph queries. Register a property graph over the indexed objects and their materialized registered Relation facts. Reuse DuckPGQ for pattern matching and traversal instead of implementing a CAPRMEDIO traversal engine or requiring a custom `expand()` API.

Reachability queries must still satisfy the Relation-expansion requirement: resolve an unambiguous typed seed, follow the selected Relation Types and directions, include the seed and each reachable typed reference once, and terminate on cycles. Use native SQL and SQL/PGQ to produce that result; joins or subqueries fetch the selected objects. Querying a declared inverse uses its materialized fact and does not synthesize it again. The Projection does not add a SQL-like parser, evaluate Formal Claims, or adopt graph algorithms beyond the selected query requirements.

Register Relation names from Current Requirement Declarations. Read only their explicit, unqualified literal `HAS_INVERSE` bindings (or the declared written alias/counterpart) to materialize inverse facts. This does not evaluate conditional formulas or treat arbitrary source Claims as graph facts. Direct graph facts come from authored Header Relations and declared Scope Unit/Atom ownership references.
