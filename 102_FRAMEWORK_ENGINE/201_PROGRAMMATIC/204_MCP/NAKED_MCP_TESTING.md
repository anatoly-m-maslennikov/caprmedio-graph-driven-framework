# Naked MCP testing

This is a disposable local test path. It uses the existing MCP server and
selected Tool routes, without Docker, a live port, or Codex MCP configuration.

From the repository root, create a fresh disposable Project and exercise the
real MCP protocol in memory:

```bash
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
TMPDIR="$PWD/.caprmedio_tmp" \
uv run --project . --locked --no-sync --managed-python --python 3.14 \
  --no-env-file --all-groups python -B \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/naked_mcp_smoke.py \
  --project-root "$PWD/.caprmedio_tmp/naked-mcp-project"
```

`--project-root` is required and must name a new child of `.caprmedio_tmp`.
The harness refuses the repository or an existing path before creating any
fixture files.

To exercise the existing `server.py` stdio gateway through the SDK's real
`ClientSession` transport, use another fresh path:

```bash
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
TMPDIR="$PWD/.caprmedio_tmp" \
uv run --project . --locked --no-sync --managed-python --python 3.14 \
  --no-env-file --all-groups python -B \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/naked_mcp_smoke.py \
  --project-root "$PWD/.caprmedio_tmp/naked-mcp-stdio" \
  --transport stdio
```

This performs MCP initialization, tool listing, and the same workflow preview
over stdio. The gateway may take up to its bounded generation-startup window;
the harness allows 120 seconds for the SDK session while retaining that
server-side bound.

For a persistent naked stdio server against that already-created disposable
Project, use the existing server entrypoint directly:

```bash
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
TMPDIR="$PWD/.caprmedio_tmp" \
uv run --project . --locked --no-sync --managed-python --python 3.14 \
  --no-env-file --all-groups python -B \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py \
  --project-root "$PWD/.caprmedio_tmp/naked-mcp-project" \
  --transport stdio
```

This command waits for an MCP client on stdio and does not contact the live
Project or start a production listener.
