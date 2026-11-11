---
atom_id: CA-A-1316
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
status: Archived
version: 6
author: Anatoly Maslennikov
role: Analysis & Advisory
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  depends_on:
  - CA-R-2719
  - CA-R-2498
  - CA-R-2500
  - CA-R-2721
  - CA-R-2722
  - CA-R-2547
  - CA-D-663
updated_at: 2026-11-04 05:16:33 +0400
carrier_destination:
  file:
    name: CA-A-1316@6-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/archive
---

## Summary

Query Atoms through a synchronized DuckDB Projection

## Proposal

Read source files, parse their YAML Header and Markdown Content according to the Current model, and load the result into an in-memory DuckDB database. WORKBENCH provides synchronous SQL and DuckPGQ SQL/PGQ graph queries through MCP and a simple web page.

```text
Current Declarations → in-memory reader schema projections
                                   ↓
Current Atom and Draft files → model-based reader → in-memory DuckDB + DuckPGQ → MCP / web
```

Files remain the source of truth. Keep exactly two public tables: `atoms` and `scope_units`. Store no database file, raw source bytes, raw frontmatter, generated schema files, snapshots, caches or temporary spill files. Read source bytes only as transient parser input.

## Sources and model parsing

- Include Current Atoms and Drafts; exclude Archived Atoms. Current includes Done, Canceled and other Current statuses.
- Select canonical Atom carriers from the existing Project inventory. Delivery copies, implementation documentation and temporary files are not Atom inputs.
- Derive the reader's required schema mappings from relevant Current Declarations as in-memory projections. Their rows carry hashes. They do not create another governing configuration, intermediate file or public table.
- Parse both YAML and Markdown according to that model: Header keys, Content heading paths, nested Properties and declared formats. Use declared mappings rather than interpreting prose or executing arbitrary CFEL.
- Retain the complete parsed Header, original Markdown body and mapped nested Content Properties. Preserve absence, null, empty values, scalar/list shape, false and zero. Reject duplicate YAML keys and ambiguous normalized sibling Property names.
- Keep direct Markdown values separate from complete sections and descendants. Derive parent paths from Property path segments; do not store a second parent-path value.
- Build `scope_units` only from Current Scope Unit Declarations. A Draft Declaration is queryable in `atoms` without changing Current structure or parser authority.

## Materialized relations and hashes

Store only direct Relations in source files. Materialize the declared derived Relations in memory from the indexed direct facts and the applicable Current Declarations. This includes declared inverse counterparts. Do not infer relations from prose or invent undeclared transitivity.

Each indexed object row carries its outgoing direct and declared-derived Relations. A Task row carries `IS_CONTAINED_BY Epic`; the Epic row carries the derived `CONTAINS Task`. Refresh affected rows, including unchanged counterpart objects, their hashes, and the DuckPGQ graph after source or Declaration changes. Remove derived facts when their source support disappears. Traversal reads materialized facts; it does not create a second inverse. Refreshing derived rows does not edit source Atoms or increment their Versions.

Each `atoms`, `scope_units` and internal schema-projection row includes `hash`: SHA-256 of its deterministic canonical row data with the `hash` field excluded. Include materialized relation values carried by that row. Hashes are derived data, not new source Properties.

Native SQL returns only the requested result columns. It does not automatically add a hash to an arbitrary result such as `SELECT COUNT(*)`.

## Queries and interfaces

Use native DuckDB SQL, including CTEs, subqueries, joins, aggregation, sorting, strings, regular expressions and nested JSON operations. Use the DuckPGQ community extension for SQL/PGQ graph queries with `GRAPH_TABLE` and `MATCH`. It queries an in-memory property graph over internal vertex and edge mappings derived from the two public tables. Do not build a CAPRMEDIO traversal engine or require a custom `expand()` API.

Reachability queries retain the existing requirement: include the unambiguous seed and each reachable typed reference once, follow selected registered Relation Types and directions, and terminate cycles. SQL retrieves objects through joins or subqueries. Current Atoms use base ID references; Drafts use `ID@Version-draft`; Scope Units use names. Preserve both kind and reference in graph identity.

Run and Check execute synchronously in the originating MCP or web request. No query jobs, tickets, queues, planner, scheduler, orchestrator or Workflow/Step wrappers are needed.

- Run returns complete rows, ordered column names/types and exact row/column counts.
- Check executes the read-only query and returns validity and exact counts, or the query error.
- Do not add an implicit LIMIT or silently truncate a result. Return an explicit delivery error if the transport cannot carry the full result.
- The web page has a SQL text area, Run and Check, counts, ordinary rows and errors. It uses the same connector as MCP.

Public queries are read-only and cannot access unrelated files or networks. Use DuckDB's native statement parsing and supported configuration for that boundary; do not add a homemade SQL parser. Native SELECT classification alone is not sufficient with side-effecting extension functions: public SQL must not create or drop graphs or mutate graph caches. Keep graph management in trusted startup and indexing, and test that public mutation attempts fail. The in-memory implementation does not use file-based read-only/read-write connection switching.

## Runtime and refresh

Bundle a compatible DuckDB/DuckPGQ pair in the WORKBENCH Docker image. Trusted startup loads the extension and enables its version-specific SQL/PGQ grammar before accepting public queries; it does not download dependencies at runtime. Use the existing application, one in-memory database owner per Project and one technical background indexer. Coordinate indexing and queries so each query sees a committed state. Restart WORKBENCH after code changes; hot-reload owner handoff is outside this MVP.

Load the selected inventory on startup and reconcile it periodically. Publish affected table rows, counterpart Relations, row hashes, and the registered graph together; queries must not see mismatched graph and table state. A graph refresh failure is reported rather than serving that mismatched state. Cover creates, edits, moves, renames, confirmed removals and Declaration changes as inventory changes; no separate event-processing workflows or prescribed fingerprint algorithm are required.

If a file is invalid, unreadable or unstable during capture, exclude its indexed values, report the path/error and available location to stderr, and continue with valid inputs. Do not keep its stale values, repair it or queue an automatic retry. A later actual source change is new input.

A database update failure publishes no partial state or successful result. Report it to stderr and its caller. Query errors return to the requesting MCP/web caller. Technical query/index activity uses Docker stdout/stderr rather than business-Journal records.

## Acceptance and limits

The indexed Evaluation Atoms cover Current/Draft membership, model-based nested parsing, Declaration changes, row hashes, materialized relation refresh, synchronous complete results, read-only SQL, no external access, no intermediate files or spilling, atomic indexing and stderr/no-retry errors.

No runtime implementation or release is claimed by this proposal. Interactive editing, custom result views, renderer, arbitrary CFEL evaluation and query orchestration remain future work.

## Sources

- [DuckDB graph queries and SQL/PGQ](https://duckdb.org/docs/2.0/guides/sql_features/graph_queries)
- [DuckPGQ extension and supported versions](https://duckdb.org/community_extensions/extensions/duckpgq)

DuckPGQ is a community extension under active development. These sources establish the selected mechanism, not acceptance evidence for this implementation. The selected runtime pair still needs its graph refresh, read-only, and no-spill checks.

## RMEDO index

- [CA-R-1525](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1525-CORE_META_MODEL-RULE--bind-workflow-runs-to-exact-definition-revisions.md)
- [CA-R-1649](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1649-CORE_META_MODEL-RULE--journal-projection-rebuild-events.md)
- [CA-R-1728](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1728-CORE_META_MODEL--record-every-projection-rebuild-in-a-journal.md)
- [CA-R-2723](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2723-WORKBENCH-RULE--derive-query-projection-only-from-governed-atom-sources.md)
- [CA-R-2724](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2724-WORKBENCH-RULE--expand-indexed-relation-references-with-complete-cycle-safe-results.md)
- [CA-R-2725](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2725-WORKBENCH-RULE--expose-only-valid-synchronized-source-state-through-query-projection.md)
- [CA-R-2726](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2726-WORKBENCH-RULE--preserve-atom-header-and-markdown-content-faithfully-in-query-projection.md)
- [CA-R-2727](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2727-WORKBENCH-RULE--provide-a-simple-web-query-interface-over-the-shared-query-capability.md)
- [CA-R-2728](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2728-WORKBENCH-RULE--provide-native-sql-query-capability-over-query-projection.md)
- [CA-R-2729](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2729-WORKBENCH-RULE--return-complete-consistent-results-for-query-run-and-check.md)
- [CA-M-462](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/CA-M-462-WORKBENCH-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md)
- [CA-M-463](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/CA-M-463-WORKBENCH-ENG_DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md)
- [CA-M-464](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/CA-M-464-WORKBENCH-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md)
- [CA-M-465](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/CA-M-465-WORKBENCH-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md)
- [CA-E-673](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/CA-E-673-WORKBENCH-EVAL_CASE--align-mcp-run-check-and-web-results.md)
- [CA-E-674](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/CA-E-674-WORKBENCH-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md)
- [CA-E-675](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/CA-E-675-WORKBENCH-EVAL_CASE--preserve-nested-header-and-markdown-property-distinction.md)
- [CA-E-676](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/CA-E-676-WORKBENCH-EVAL_CASE--query-native-sql-results-and-typed-relation-expansion.md)
- [CA-E-677](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/CA-E-677-WORKBENCH-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md)
- [CA-D-378](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-378-CORE_META_MODEL-ENG_DECISION--serialize-assigned-atom-identities.md)
- [CA-D-650](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-650-CORE_META_MODEL-ENG_DECISION-CORE_META_MODEL--serialize-numbered-version-qualified-draft-atom-filenames.md)
- [CA-D-672](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/CA-D-672-WORKBENCH-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md)
- [CA-D-673](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/CA-D-673-WORKBENCH-ENG_DECISION--deliver-shared-query-run-and-check-results.md)
- [CA-D-674](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/CA-D-674-WORKBENCH-ENG_DECISION--deliver-simple-sql-query-page.md)
- [CA-D-675](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/CA-D-675-WORKBENCH-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md)
- [CA-O-240](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/09_operations/CA-O-240-WORKBENCH-ACTION--execute-one-read-only-duckdb-query.md)
- [CA-O-241](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/09_operations/CA-O-241-WORKBENCH-ACTION--reconcile-the-duckdb-query-projection.md)
- [CA-R-2730](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/CA-R-2730-APPS-DEFINES_SCOPE_FOR-WORKBENCH--declare-workbench.md)
