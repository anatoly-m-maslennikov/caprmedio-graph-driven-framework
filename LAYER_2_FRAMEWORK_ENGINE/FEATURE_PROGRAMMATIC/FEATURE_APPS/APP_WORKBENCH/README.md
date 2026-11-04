# Workbench

Open `/caprmedio/workbench/<project_name>` (here, `/caprmedio/workbench/caprmedio`) on the Project MCP server. Run executes SQL once
and returns the first page and exact total counts. Previous and Next fetch
pages from that stable result; Check returns exact row and column counts.
The MCP endpoint is `/caprmedio/mcp`; health is `/caprmedio/health`.

MCP tools:

- `query_run(sql, page_size=100, cursor_position?)` returns a `query_id`, original column metadata,
  positional rows, total counts, offset and `has_more`.
- `query_page(query_id, offset, page_size=100)` reads the same result without
  re-executing SQL. The maximum page size is 1,000.
- `query_check(sql, cursor_position?)` returns validity and exact counts without transferring all rows.
- `query_schema()` returns table/column names and types for completion.
- `query_save(sql, cursor_position?)` saves SQL without executing it.
- `worksheet_save(sql)` saves a whole multi-query script.
- `query_load(reference)` opens a saved ID or full URL without executing it.
- `query_saved_list(limit=20)` lists the most recent saved queries and Worksheets.

Run and Check save before execution. Their answers, including SQL errors, return
`saved_query_id`, `saved_query_url`, `kind` and the selected `sql`. The saved ID is
separate from the materialized result's pagination `query_id`. Query saves are
immutable `.sql` files; Worksheet saves are `.json` files in
`.caprmedio_runtime/workbench/saved_queries`. A saved URL uses `?query=<id>`.

Each editor tab is a Worksheet. Run, Check and Save select the statement at the
cursor; Save Worksheet saves the whole script. Semicolons inside SQL literals or
comments do not split statements. MCP callers may pass `cursor_position` in
UTF-16 code units; without it, the submitted SQL is used unchanged.
Cmd+Enter runs and Shift+Cmd+Enter checks. The CodeMirror editor completes names
from the current schema. Local browser drafts autosave every five seconds and
restore after reload; unsaved tabs/windows ask before closing. Saved SQL opens
without execution. Light, Dark and System themes and text-only zoom cover all UI
text, including buttons, tabs and result cells.

The UI hides columns containing only NULL, empty strings or empty collections
across the whole result. Zero and false remain visible. `columns[].has_values`
is stable across pages; SQL rows and total column counts remain complete.

Web POST endpoints are `/caprmedio/workbench/<project_name>/run`, `/page`, `/check`,
`/schema`, `/save`, `/worksheet-save`, `/load` and `/saved-list`.
A mismatched Project name returns 404. Static assets stay under `/caprmedio/workbench/assets`.
A shared MCP server also requires `project_root`.

```sql
SELECT id, reference, role, status, "content.summary", relations FROM atoms LIMIT 20;
```

```sql
SELECT id, "relative path", filename, relations->'$.CONTAINS' AS contains
FROM atoms WHERE json_exists(relations, '$.CONTAINS');
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
`atoms` exposes a relative path plus filename, a stable `reference`, typed header
properties, the fixed union of declared `content.*` Markdown values, outgoing
`relations` JSON, and a hash. `scope_units` exposes its declaration properties,
outgoing `relations`, and a hash. It does not expose parser-only YAML, raw Markdown,
or raw edge JSON. Graph traversal remains available through `GRAPH_TABLE`.
The index stores parsed YAML, Markdown sections and derived relations in the rebuildable
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
