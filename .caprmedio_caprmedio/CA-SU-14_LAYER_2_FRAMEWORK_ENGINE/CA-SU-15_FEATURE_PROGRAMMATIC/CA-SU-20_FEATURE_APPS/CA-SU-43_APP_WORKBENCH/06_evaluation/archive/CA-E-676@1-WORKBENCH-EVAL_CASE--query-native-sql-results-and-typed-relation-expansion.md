---
atom_id: CA-E-676
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 1
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-676@1-WORKBENCH-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for:
  - CA-R-2728
  - CA-R-2724
  - CA-R-2729
  - CA-M-464
  - CA-D-673
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Query native SQL results and typed Relation expansion

## Claim scope

The SQL connector and its small `expand` helper over indexed Projection rows.

## Claim

### Prose Claim

The connector passes when accepted SQL follows native DuckDB semantics for
selection, joins, CTEs, aggregation, sorting, string functions, and regular
expressions. A valid query returns its exact column names, types, row count,
column count, and complete rows without an implicit limit. An invalid query
returns a SQL error rather than an empty successful result. `expand` resolves an
unambiguous seed and follows only the selected registered Relation Types and
directions over indexed links. It includes the seed and each reachable reference
once, terminates on cycles, and returns references rather than fetched object
copies. Its native SQL shape is `expand(seed, relations, seed_kind := NULL)`,
where `relations` is a SQL list of registered relation names and its two result
columns are `kind` and `ref`. A CTE or ordinary SQL join can fetch the referenced
Atom rows. Prose and unregistered links do not become graph edges.

## Details

### Fixtures and expected outcomes

| Fixture | Expected outcome |
| --- | --- |
| Valid `SELECT`, CTE, aggregation, grouping, ordering, string, and regex queries | Results use native DuckDB behavior and report exact columns, types, counts, and all rows. |
| Invalid SQL, including a malformed expression or unresolved table | The caller receives a query error; it is not converted to an empty successful result and does not mutate the Projection. |
| A cyclic relation graph with one or more selected typed Relation Types | `expand` returns the seed and each reachable reference once, follows the selected directions, and terminates without looping. |
| Multiple typed Relation Types from the same seed | Only links of the requested types participate; direct indexed facts remain distinguishable and are not inferred from prose. |
| Expansion references joined through a CTE to `atoms` or `scope_units` | The query returns fetched object data through SQL while the expansion result itself remains references, not embedded object copies. |
| A seed name that is ambiguous without kind or context | Expansion fails with an ambiguity error rather than choosing an arbitrary Atom. |

### Concrete helper SQL

The helper accepts a Scope Unit name and a SQL list; it exposes only typed references:

```sql
SELECT kind, ref
FROM expand('FRAMEWORK_ENGINE', ['CONTAINS'], 'Scope Unit');
```

For a cyclic set of selected direct facts and declared inverses, this result contains
the seed `(kind, ref)` once and every reachable `(kind, ref)` once. It does not
fetch a Scope Unit object and it terminates.

The result is joinable to the documented `scope_units` Projection table without a
second graph representation:

```sql
WITH expanded AS (
  SELECT kind, ref
  FROM expand('FRAMEWORK_ENGINE', ['CONTAINS'], 'Scope Unit')
)
SELECT scope_units.*
FROM expanded
JOIN scope_units ON expanded.kind = 'Scope Unit'
                AND expanded.ref = scope_units.name
ORDER BY expanded.kind, expanded.ref;
```

An Atom seed may use its bare Atom ID with the Current default, while an explicit
kind is limited to the two documented literals; no encoded reference syntax is
accepted:

```sql
SELECT kind, ref
FROM expand('CA-R-2724', ['DEPENDS_ON'], 'Atom');
```
