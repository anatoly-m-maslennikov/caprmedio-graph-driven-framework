# In-memory Workbench MVP — adopted refinement

[CA-A-1316](../../done/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md) is Done, version 5. The 22 indexed Workbench RMEDO Atoms are Current at version 2; their version-1 predecessors are archived.

- Read Current Atom and Draft files; exclude Archived sources. All Current statuses remain included.
- Parse frontmatter and Markdown according to the Current model using in-memory projections of relevant Current Declarations.
- Use only the public `atoms` and `scope_units` tables in in-memory DuckDB. No database file, raw source-byte column, raw-frontmatter column, generated schema file, cache, snapshot or temporary spill file.
- Materialize declared derived Relations in memory. Source files retain direct facts only. Traversal uses materialized facts once, with no repeated inverse synthesis.
- Hash each public data row and internal schema-projection row from its canonical value, excluding `hash` itself and including materialized relation values carried by the row. SQL keeps the requested result columns.
- Keep direct Markdown and complete sections distinct. Derive parent paths from Property path segments.
- Keep synchronous MCP/web Run and Check, separate technical indexing, stderr errors and no automatic retry. No query orchestration or hot-reload owner replacement.

## Verification

Two independent document checks passed after aligning parent-path wording, hash semantics and query no-spill acceptance. The published source check passed for all 23 changed Atoms, their 23 archives, all 28 index links, exact two-table schema, both hash columns and the materialized-relation flag.

MCP appended the 23 actual source-update observations to `Codex-2026-11-04-part-1.ndjson`, lines 1–23. No baseline records or Workflow Runs were invented.

## Runtime work remains

No runtime feature code, dependency or Docker image was changed. Implementation must still demonstrate the native SQL statement guard, model/schema extraction, relation refresh, row hashing and disabled spilling.

Technical reference: [DuckDB Python API](https://duckdb.org/docs/2.0/clients/python/reference/) and [configuration](https://duckdb.org/docs/2.0/configuration/overview). Native statement parsing supports the selected guard; in-memory mode still requires disabling temporary spill files. These document checks are not runtime tests.
