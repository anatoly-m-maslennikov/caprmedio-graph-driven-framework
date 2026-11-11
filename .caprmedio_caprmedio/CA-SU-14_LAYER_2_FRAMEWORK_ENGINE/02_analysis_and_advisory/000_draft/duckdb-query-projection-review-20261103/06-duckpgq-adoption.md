# DuckPGQ specification update — 4 November 2026

Adopted DuckDB + DuckPGQ for native SQL/PGQ graph queries through the existing synchronous MCP/web connector. Removed the requirement for a custom `expand()` API. R2723–R2729 retain the required behavior. No runtime code or Docker image changed.

Applied the Operator's outgoing-Relation ownership decision: Task owns the direct `IS_CONTAINED_BY` fact; Epic carries derived `CONTAINS`. Both affected indexed rows and hashes refresh without modifying the unchanged counterpart source.

| Atom ID | Previous version | Current version | Status |
| --- | --- | --- | --- |
| CA-M-462 | 2 | 3 | Applied |
| CA-M-464 | 2 | 3 | Applied |
| CA-M-465 | 2 | 3 | Applied |
| CA-E-674 | 2 | 3 | Applied |
| CA-E-676 | 2 | 3 | Applied |
| CA-E-677 | 2 | 3 | Applied |
| CA-D-672 | 2 | 3 | Applied |
| CA-D-673 | 2 | 3 | Applied |
| CA-D-675 | 2 | 3 | Applied |
| CA-O-240 | 2 | 3 | Applied |
| CA-O-241 | 2 | 3 | Applied |
| CA-A-1316 | 5 | 6 | Applied |

Checks: independent coherence review and mechanical preflight passed. After adoption, all12 Current hashes/headers and predecessor archives passed; the proposal's28 ID-only index links resolve. Both public tables retain `hash` and now carry their own outgoing `relation_edges_json`.

Actual source updates were appended once through MCP to `.caprmedio_caprmedio/_journal/Codex-2026-11-04-part-1.ndjson`, lines24–35. No baseline or Workflow Run was invented.

Runtime remains untested: the selected DuckDB/DuckPGQ versions, native graph parsing, mutation rejection (including SELECT-side graph/cache functions), atomic graph/table refresh, and no-spill behavior still require implementation checks. Native SELECT classification alone is not a complete read-only boundary.

This update also corrects E677's Current-Declaration authority wording and adds source/counterpart invalidation acceptance cases. It does not resolve the separate SQL-result cell-encoding proposal or claim that the full FPF findings queue is closed.

Sources: [DuckDB graph queries](https://duckdb.org/docs/2.0/guides/sql_features/graph_queries); [DuckPGQ supported versions](https://duckdb.org/community_extensions/extensions/duckpgq).
