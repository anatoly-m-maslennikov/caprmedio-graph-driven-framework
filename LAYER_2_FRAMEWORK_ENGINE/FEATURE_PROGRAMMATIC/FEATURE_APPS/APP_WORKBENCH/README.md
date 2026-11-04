# Workbench

Open `/workbench` on the Project MCP server. Run returns all rows; Check returns
the row and column counts. The MCP tools are `query_run` and `query_check`, with
one `sql` argument. A shared MCP server also requires `project_root`.

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
It keeps parsed YAML, Markdown sections and derived relations in memory.
`watchfiles` watches only the selected repository's CAPRMEDIO source folder,
even when a larger parent folder is mounted.
Invalid or ambiguous sources are excluded and reported to stderr.

SQL is trusted Operator input. The runtime accepts one native read query inside
a read-only transaction. Unsupported DuckPGQ management functions can invalidate
the connection; restart Workbench after such an error.

The Docker build installs DuckPGQ. Native tests need the host extension too:

```sh
uv sync --group rmed-workflow-mcp
.venv/bin/python -c "import duckdb; c=duckdb.connect(config={'extension_directory':'.caprmedio_tmp/workbench/extensions'}); c.execute('INSTALL duckpgq FROM community'); c.close()"
```

Run the repository's full test suite to build one disposable image and run the
host and Docker tests. The tests do not replace the running Project MCP.
