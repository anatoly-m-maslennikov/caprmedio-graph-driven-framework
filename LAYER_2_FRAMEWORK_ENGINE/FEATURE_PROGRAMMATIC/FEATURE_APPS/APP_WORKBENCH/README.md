# Workbench

Open `/caprmedio/workbench` on the Project MCP server. Run executes SQL once
and returns the first page and exact total counts. Previous and Next fetch
pages from that stable result; Check returns exact row and column counts.
The MCP endpoint is `/caprmedio/mcp`; health is `/caprmedio/health`.

MCP tools:

- `query_run(sql, page_size=100)` returns a `query_id`, original column metadata,
  positional rows, total counts, offset and `has_more`.
- `query_page(query_id, offset, page_size=100)` reads the same result without
  re-executing SQL. The maximum page size is 1,000.
- `query_check(sql)` returns validity and exact counts without transferring all rows.

Web POST endpoints are `/caprmedio/workbench/run`, `/page` and `/check`.
A shared MCP server also requires `project_root`.

```sql
SELECT id, role, status, hash FROM atoms LIMIT 20;
```

```sql
SELECT name, parent_name FROM scope_units ORDER BY name;
```

```sql
FROM GRAPH_TABLE (
    caprmedio MATCH (parent:Reference)-[edge:CONTAINS]->(child:Reference)
    COLUMNS (parent.ref AS parent, child.ref AS child, edge.derived AS derived)
);
```

The index reads Current and Draft Atom files and Current Scope Unit Declarations.
It stores parsed YAML, Markdown sections and derived relations in the rebuildable
`.caprmedio_runtime/workbench/projection.duckdb` database. Query results stay
stable across source refresh and are discarded at restart. Spill files remain
in the same owned runtime directory; source files stay authoritative.
`watchfiles` watches only the selected repository's CAPRMEDIO source folder,
even when a larger parent folder is mounted.
Invalid or ambiguous sources are excluded and reported to stderr.

SQL is trusted Operator input. The runtime admits one native read query and
materializes it through a trusted internal cache write. Public SQL cannot edit
source files or source tables. Unsupported DuckPGQ management functions can
invalidate the connection; restart Workbench after such an error.

`FEATURE_WORKBENCH_BACKEND` owns indexing and queries.
`FEATURE_WORKBENCH_FRONTEND` owns the Svelte + TypeScript + Vite UI and shared
component palette. Python serves the production assets; no frontend server is needed.
Build the frontend with `npm ci && npm run build` in its directory.
Split source files above 300 lines where practical; splitting above 500 is mandatory.

The Docker build installs DuckPGQ. Native tests need the host extension too:

```sh
uv sync --group rmed-workflow-mcp
.venv/bin/python -c "import duckdb; c=duckdb.connect(config={'extension_directory':'.caprmedio_tmp/workbench/extensions'}); c.execute('INSTALL duckpgq FROM community'); c.close()"
```

Run the repository's full test suite to build one disposable image and run the
host and Docker tests. The tests do not replace the running Project MCP.
