---
identity:
  atom_id: CA-M-464
  ref_id: CA-M-464@8
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Eng Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2723
  - CA-R-2726
  - CA-R-2728
  - CA-R-2724
state:
  status: Archived
  version: 8
  updated_at: 2026-11-06 20:37:19 +0400
destination:
  file:
    name: CA-M-464@8-WORKBENCH_BACKEND-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archived
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---


## Summary

Preserve governed Atom data and reuse native SQL.

## Claim scope

Direct file reading and native query semantics for Current and Draft Atom carriers excluding Archived carriers.

## Claim

### Prose Claim

The DuckDB Projection reader must read Current and Draft Atom carriers, excluding Archived carriers, into the derived DuckDB database. Every Current status, including Done and Canceled, remains in that inventory. Parse YAML and Markdown directly using the existing safe YAML reader and CommonMark headings. Generate the Content schema from Current model Declarations. Compile declared Content paths and their applicability; do not evaluate arbitrary CFEL formulas or interpret prose as schema.

Preserve all parsed raw Header properties, the original Markdown body, and real heading paths without a fixed heading list or Form validation. Parent paths are derived from Property path segments. The reader creates no intermediate source-data files or third public source table. Its schema is a rebuildable derived asset under `.caprmedio_runtime/workbench`, with one flattened SQL column for every observed raw Header Property path and Content columns from model-declared Properties.

Only Current Scope Unit Declarations establish the current Scope Unit inventory. A Draft Declaration remains a queryable Atom but does not establish a current Scope Unit.

Source Atoms retain direct Relations only. Each indexed object row carries that object's outgoing direct and declared-derived Relations. For `Task IS_CONTAINED_BY Epic`, the Task row carries `IS_CONTAINED_BY` and the Epic row carries the derived `CONTAINS`. A source or relevant Declaration change refreshes every affected outgoing-relation row, graph mapping, and row hash, including rows for unchanged target sources. This does not edit those sources or increment their Versions. Each public row hash includes its materialized Relations.

Use DuckDB for SQL and the DuckPGQ community extension for SQL/PGQ graph queries. Register a property graph over the indexed objects and their materialized registered Relation facts. Reuse DuckPGQ for pattern matching and traversal instead of implementing a CAPRMEDIO traversal engine or requiring a custom `expand()` API.

Reachability queries must still satisfy the Relation-expansion requirement: resolve an unambiguous typed seed, follow the selected Relation Types and directions, include the seed and each reachable typed reference once, and terminate on cycles. Use native SQL and SQL/PGQ to produce that result; joins or subqueries fetch the selected objects. Querying a declared inverse uses its materialized fact and does not synthesize it again. The Projection does not add a SQL-like parser, evaluate Formal Claims, or adopt graph algorithms beyond the selected query requirements.

Register Relation names from Current Requirement Declarations. Read only their explicit, unqualified literal `HAS_INVERSE` bindings (or the declared written alias/counterpart) to materialize inverse facts. This does not evaluate conditional formulas or treat arbitrary source Claims as graph facts. Direct graph facts come from authored Header Relations and declared Scope Unit/Atom ownership references.

Include `pytz`, required by DuckDB for fetching timezone-aware timestamps into Python. Keep those values timezone-aware until the shared result encoder returns ISO strings; do not cast source columns to work around a missing runtime dependency.
