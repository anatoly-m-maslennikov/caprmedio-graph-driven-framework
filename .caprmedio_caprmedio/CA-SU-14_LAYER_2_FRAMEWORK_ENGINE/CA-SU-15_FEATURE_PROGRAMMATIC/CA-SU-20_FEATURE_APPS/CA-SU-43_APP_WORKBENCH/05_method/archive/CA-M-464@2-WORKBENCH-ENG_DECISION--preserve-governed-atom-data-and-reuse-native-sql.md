---
atom_id: CA-M-464
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 2
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
    name: CA-M-464@2-WORKBENCH-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 00:38:14 +0400
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

Source Atoms retain direct Relations only. The Projection materializes declared derived Relations in memory and rebuilds the affected materialized rows after a source or relevant Declaration changes. Each public row hash includes its materialized Relations. Each in-memory schema Projection row uses the same `hash` rule: hash its deterministic canonical row value with `hash` excluded.

Use DuckDB as the SQL engine and reuse its native SQL behavior. The only CAPRMEDIO graph extension is the minimal `expand` helper over indexed registered Relation Types: it resolves an unambiguous seed, follows selected directions, includes each reachable reference once, terminates cycles, and returns references rather than embedded objects. The Projection does not add a SQL-like parser or evaluate Formal Claims.
