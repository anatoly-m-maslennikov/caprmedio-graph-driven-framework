# Workbench

Open `/caprmedio/workbench/<project_name>` (here, `/caprmedio/workbench/caprmedio`) on the Project MCP server. Run executes SQL once
and returns the first page and exact total counts. Previous and Next fetch
pages from that stable result; Check returns exact row and column counts.
The MCP endpoint is `/caprmedio/mcp`; health is `/caprmedio/health`.

MCP tools:

- `query_run(sql, page_size=100, cursor_position?, save=false, preview?, name?)` returns selected `sql`, a `query_id`, original column metadata,
  positional rows, total counts, offset and `has_more`.
- `query_page(query_id, offset, page_size=100)` reads the same result without
  re-executing SQL. The maximum page size is 1,000.
- `query_check(sql, cursor_position?)` returns selected `sql`, validity and exact counts without transferring all rows.
- `query_schema()` returns table/column names and types for completion.
- `view_save(sql, name?)` saves a whole multi-query script with an optional name.
- `query_load(reference)` opens a saved ID or full URL without executing it.
- `query_saved_list(limit=20)` lists the most recent saved queries and Views.
- `workbench_restart()` restarts only this Project's Workbench index and query owner.
- `workbench_reread()` discards the derived DuckDB database and rebuilds it from source, including changed table schemas.

`preview=N` returns at most N rows while preserving an existing SQL LIMIT;
omitting it adds no limit. `save=true` saves the exact original selected SQL
only after a successful Run. Preview never changes saved SQL. An optional `name`
requires `save=true`. If saving fails after Run succeeds, the normal response
keeps its rows and query ID and includes `outcome: "partial"` and `save_error`,
without a new saved ID. MCP returns a normal result and HTTP returns 200.

Single-project MCP tools accept an optional top-level `project_root` matching
their bound host or container Project root. Shared MCP requires this field.
The gateway validates and removes it before native dispatch; it cannot switch
the Project of a single-project service.

`workbench_restart()` is available through MCP and the fixed health-page
`Restart Workbench` form. It has no Workbench frontend control and accepts no
generic service, shell or Docker command. It closes the existing Workbench
owner, rebuilds its index, and returns
`{service: "workbench", status: "ready"}` only when the replacement is ready.
Old query-result IDs become unavailable; saved query and View IDs remain
loadable. MCP and other services continue running. A Scope Unit Declaration
that remains invalid causes an explicit unavailable error; correct it and call
`workbench_restart()` again. Restart does not retry automatically, control Docker,
run shell commands, or write a Business Journal event.

The native health form posts only to `/caprmedio/health/workbench-restart`.
On a shared host it requires exactly one `project_root` Project folder; a
single-project host accepts an empty form only. It uses the same MCP tool
boundary as direct callers. The ordinary health GET and JSON readiness response
remain read-only.

The health-page `Full reread` button posts to
`/caprmedio/health/workbench-reread` through the same MCP operation. It closes
Workbench, removes only its derived database, WAL and temporary files, then
creates a fresh database and reads Current and Draft sources. Old tables,
columns and query-result IDs do not survive. Source files, saved queries,
Views and their Journal remain unchanged. Failure reports unavailable;
there is no automatic retry or fallback to the old database.

Ordinary Run and Check do not create permanent saved-item IDs. Every actual Run records SQL, success/fail, error and row/column counts in the separate runtime query log; Check does not. Log records expire after seven days on use and contain no result rows. Saved Views do not expire. Run & Save and Save View
create immutable entries in the configured Project Journal, in date-partitioned
`workbench-saved-items-…-part-N.ndjson` files. Each entry has a canonical UUIDv7,
kind, exact SQL, optional name and save timestamp. Parts hold about 1,000 entries
under concurrent appends. Existing runtime `q_….sql` and `w_….json` files remain
read-only compatibility sources; their IDs and URLs keep working.
A saved URL uses `?query=<id>`. Saved entries are not renamed.

Each editor tab is a View. Run, Check and Run & Save select the statement at the
cursor; Save View saves the whole script. Semicolons inside SQL literals or
comments do not split statements. MCP callers may pass `cursor_position` in
UTF-16 code units; without it, the submitted SQL is used unchanged.
Cmd+Enter runs and Shift+Cmd+Enter checks. Cmd+P opens the searchable command
palette for every current UI action. Arrow Up/Ctrl+P and Arrow Down/Ctrl+N move
the selection; Enter chooses and Escape closes. Settings contains Theme and Zoom.
The standalone Workbench chat is disabled; use native Codex chat.
The next utility tab lists saved queries and Views. Open Saved is available only in the command palette: Cmd+P, choose Open Saved,
paste an ID or URL, then Enter.

The CodeMirror editor completes names from the current schema and values in
status equality literals, such as `status = 'Act`. Schema metadata provides
observed status values; typing does not run or save SQL.
Local browser drafts and optional current View names autosave every five seconds and
restore after reload; unsaved tabs/windows ask before closing. Saved SQL opens
without execution. Light, Dark and System themes and text-only zoom cover all UI
text, including buttons, tabs and result cells.

Rename current Views; bound Workspaces share those names with MCP. Save View copies that optional name;
Run & Save can take a query name and saves only after successful execution.

The UI hides columns containing only NULL, empty strings or empty collections
across the whole result. Zero and false remain visible. `columns[].has_values`
is stable across pages; SQL rows and total column counts remain complete.

A Codex plugin package is in `FEATURE_CODEX_EXTENSION/plugin`. It uses a native
SessionStart session ID and the existing CAPRMEDIO MCP connection; it adds no
standalone chat or second server. Local packaging does not install or trust it
in Codex automatically.

`workspace_open(session_id)` initializes or resumes one Workspace for that native
chat and Project. Open its `workspace_url` in Codex's native browser beside the
chat. The URL uses `?workspace=<session_id>`. Existing unbound browser drafts stay
separate. `workspace_list` and `workspace_get` inspect known state.

Use `view_create` (first/last), `view_list`, `view_get`, `view_update`, `view_run`,
`view_check`, `view_fetch`, `view_focus`, `view_rename`, `view_remove` and `view_save`
with explicit Workspace/View IDs. SQL updates require the View's revision;
stale updates fail without discarding the browser draft. The last View cannot be
removed. `view_run` returns metadata, not rows; fetch result pages only when
needed. The browser uses the same state, so an Agent can create, update, run and
focus a View without reading the result rows. `query_log_list` and `query_log_get`
read retained run records.

The shared HTTP representation is POST `/interface` under the Project Workbench
URL, with `{operation, arguments}` and the existing outer Project binding.

Web POST endpoints are `/caprmedio/workbench/<project_name>/run`, `/page`, `/check`,
`/schema`, `/view-save`, `/load` and `/saved-list`. Run & Save uses `/run`
with `save=true`; there is no separate `/save` or MCP `query_save` operation.
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


Browser E2E tests use Playwright with Chromium against the same owned container
as the MCP/HTTP tests. They use the production frontend and real backend, with
no Vite server, mock backend or retries. Tests assert visible results and user
flows; duplicate constructor/call-order unit checks are removed. Focused unit
tests remain where the E2E flows do not cover the behavior.

Install the development browser once from `FEATURE_WORKBENCH_FRONTEND`:

```sh
npm ci
PLAYWRIGHT_BROWSERS_PATH="$(git rev-parse --show-toplevel)/.caprmedio_tmp/workbench/playwright-browsers" npx playwright install chromium
```

The Docker E2E test sets the browser URL and uses that cache automatically.
A standalone browser run requires an explicit `WORKBENCH_E2E_URL` and the same
`PLAYWRIGHT_BROWSERS_PATH`, then `npm run test:e2e`. It creates saved-item Journal
entries in the selected test Project. No live-server URL is assumed.

Browser test artifacts are written to `.caprmedio_tmp/workbench/browser-results`, outside application/image inputs.

Result table headers show column names on their own line, with SQL types below in smaller muted text.
