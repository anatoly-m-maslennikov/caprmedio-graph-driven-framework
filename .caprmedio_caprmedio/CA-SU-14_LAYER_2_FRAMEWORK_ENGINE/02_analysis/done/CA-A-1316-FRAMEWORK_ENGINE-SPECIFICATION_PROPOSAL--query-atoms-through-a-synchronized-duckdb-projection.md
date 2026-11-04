---
atom_id: CA-A-1316
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
status: Done
version: 7
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
updated_at: 2026-11-04 07:39:08 +0400
carrier_destination:
  file:
    name: CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/done
---

## Summary

Query Atoms through a synchronized DuckDB Projection

## Proposal

Read governed source files directly, parse their complete YAML Header and Markdown Content with the Current model, and load the result into an in-memory DuckDB database. WORKBENCH provides synchronous native SQL and DuckPGQ graph queries through MCP and a simple web page.

```text
Current model parser ──┬─> atoms
                       ├─> scope_units (Current Scope Unit Declarations only)
                       └─> in-memory DuckDB + DuckPGQ ──> MCP / web
```

Files remain the source of truth. Keep exactly two public tables: `atoms` and `scope_units`. Store no database file, source bytes, raw frontmatter, generated schema artifact, snapshot, cache, or temporary spill file. Source bytes may exist only as transient parser input.

## Sources and model parsing

- Include Current Atoms and Drafts; exclude Archived Atoms. Current means every Current status, including Done and Canceled; Draft rows use their qualified `ID@Version-draft` reference.
- Select canonical Atom carriers from the existing Project inventory. Delivery copies, implementation documentation, and temporary files are not Atom inputs.
- Parse each source directly with the Current model. Do not create a second Declaration-derived schema artifact, generic CFEL evaluator, or prose evaluator. Current Scope Unit Declarations alone define `scope_units`; Draft Declarations are `atoms` rows and do not change Current Scope Unit structure.
- Parse complete YAML Headers and Markdown heading paths. Retain nested Header mappings and native distinctions between missing, null, empty, scalar, list, map, false, and zero. Reject duplicate YAML keys and ambiguous normalized sibling Property names.
- Retain the original Markdown body and complete mapped section occurrences. A `property_path` is a non-empty array of heading segments, not a dotted string. Preserve `heading`, `heading_level`, one-based occurrence `position`, `direct_markdown`, and complete `section_markdown`; the latter includes the heading and full subtree, while the former excludes child Properties. Skipped heading levels create no synthetic segments and fenced heading-like text creates no section. No separate parent-path field is stored.
- Keep direct values separate from descendant subtrees, including the RMED Claim container with Formal Claim and Prose Claim children. Applicable Current Declaration changes that govern scope or Relations refresh the actual indexed facts.

## Materialized relations and hashes

Store only direct Relations found in source files. Materialize declared derived Relations in memory from those direct facts and applicable Current Declarations. Do not infer relations from prose or invent undeclared transitivity.

Each indexed object row carries its outgoing direct and declared-derived Relations. A Task row carries `IS_CONTAINED_BY Epic`; the Epic row carries the derived `CONTAINS Task`. Refresh affected rows, unchanged counterpart objects, their hashes, and the DuckPGQ graph after source or applicable Declaration changes. Remove derived facts when their supporting source fact disappears. A declared inverse is not synthesized twice. Traversal reads materialized facts and does not create a second inverse. Refreshing derived rows does not edit source Atoms or increment their Versions.

Each `atoms` and `scope_units` row carries `hash`: SHA-256 of deterministic canonical row JSON with `hash` excluded, including the entire row after materialized Relation facts are present. Hashes are derived indexed data, not new source Properties. Do not automatically add a hash to arbitrary SQL result rows such as `SELECT COUNT(*)`.

## Queries and interfaces

Use native DuckDB SQL, including CTEs, subqueries, joins, aggregation, sorting, strings, regular expressions, and nested JSON operations. Use the image-bundled DuckPGQ extension for native SQL/PGQ graph queries with `GRAPH_TABLE` and `MATCH`. It queries an in-memory property graph over vertex and edge mappings derived from the two public tables. Do not build a CAPRMEDIO traversal engine or require a custom `expand()` API.

Reachability queries retain the existing requirement: include the unambiguous seed and each reachable typed reference once, follow selected registered Relation Types and directions, and terminate cycles. SQL retrieves objects through joins or subqueries. Current Atoms use base ID references; Drafts use `ID@Version-draft`; Scope Units use names. Preserve both kind and reference in graph identity.

The Trusted SQL MVP admits exactly one native `SELECT` and executes it inside a native `BEGIN TRANSACTION READ ONLY` boundary. External access is disabled and the relevant configuration is locked for public requests. The implementation must not spill to disk and does not use a file-based read-only connection switch. Native statement parsing admits the request; no homemade SQL parser, generic permission layer, or capability-sandbox promise is added.

DuckPGQ internal management calls are unsupported for public requests. An unsupported call may invalidate the connection even under the read-only transaction. Return an explicit engine error stating that restart is required; do not automatically retry the query. An ordinary SQL error leaves the connection usable for the next request.

Run and Check execute synchronously in the originating MCP or web request. MCP Run and Check return complete, untruncated result rows, ordered column names/types, exact row and column counts, and query errors. If the MCP transport cannot carry complete data, return an explicit transport failure rather than silently truncating. The web page has a SQL text area, Run and Check, counts, ordinary result rows, and query errors through the same connector; this proposal does not require all web rows to be materialized or displayed at once and does not define a UI truncation or pagination policy.

## Runtime and refresh

Bundle DuckDB `2.0.0` and the image-bundled DuckPGQ extension in the WORKBENCH Docker image. Trusted startup loads the pair, enables its native SQL/PGQ grammar, builds the in-memory graph, and accepts public queries only after a committed state exists. It does not download dependencies at runtime. Use the existing application, one in-memory database owner per Project, and one technical indexer; Run and Check remain synchronous and need no query jobs, tickets, queues, planner, scheduler, orchestrator, or Workflow/Step wrappers.

Load the selected Current/Draft inventory on startup and reconcile it as the actual inventory changes. Publish source rows, materialized outgoing Relations, row hashes, and graph mappings together so queries cannot see mismatched table and graph state. Cover creates, edits, moves, renames, confirmed removals, and applicable Current Declaration changes. Ordinary internal cache updates are runtime maintenance, not logical Projection mutations.

If a file is invalid, unreadable, or unstable during capture, exclude its indexed values, report the path and error to stderr, and continue with valid inputs. Do not keep stale values, repair the file, or queue an automatic retry. A later actual source change is new input. Source files remain unchanged.

A database or graph update failure publishes no partial state or successful result. Report it to stderr and its caller. Query errors return to the requesting MCP or web caller. Technical query/index activity uses Docker stdout/stderr; this MVP creates no Business Journal record.

## Dependency admission

The minimal Delivery dependency admission is the existing PyYAML parser, `markdown-it-py==4.2.0` for CommonMark heading parsing from the official PyPI packages on Python `>=3.10`, and DuckDB `2.0.0` with image-bundled DuckPGQ. Pin package versions without file hashes. Do not add generic schema-validation or permission-layer dependencies.

## Acceptance and limits

The focused Evaluation Atoms cover Current/Draft membership, complete YAML and Markdown heading-path parsing, native value distinctions, Current Scope Unit Declaration structure, direct and materialized Relation refresh, per-row hashes, synchronous MCP/web behavior, one native SELECT in a read-only transaction, locked external access, no intermediate files or spilling, ordinary versus connection-invalidating engine errors, atomic indexing, and stderr/no-retry source failures.

No runtime implementation or release is claimed by this proposal. Interactive editing, custom result views, renderer behavior, arbitrary CFEL evaluation, generic prose evaluation, and query orchestration remain future work.

## Sources

- [DuckDB graph queries and SQL/PGQ](https://duckdb.org/docs/2.0/guides/sql_features/graph_queries)
- [DuckPGQ extension and supported versions](https://duckdb.org/community_extensions/extensions/duckpgq)
- [PyYAML on PyPI](https://pypi.org/project/PyYAML/)
- [markdown-it-py 4.2.0 on PyPI](https://pypi.org/project/markdown-it-py/4.2.0/)

DuckPGQ is a community extension under active development. These sources establish the selected mechanisms and package publication, not acceptance evidence for this implementation. The selected runtime pair still needs its graph-refresh, trusted-query, connection-error, and no-spill checks.

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

Implementation remains a happy-path MVP: native query and indexing transactions finish normally with COMMIT; no application rollback, candidate database, retained-state restoration, automatic query replay, or connection recovery is introduced. Failed indexing/invalidated engine state is reported to stderr and requires an explicit restart. Technical diagnostics reserve stdio MCP stdout for protocol traffic.
