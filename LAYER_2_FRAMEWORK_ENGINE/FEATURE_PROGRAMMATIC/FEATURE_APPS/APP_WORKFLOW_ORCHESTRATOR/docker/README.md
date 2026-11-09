# Project-scoped Docker runtime

The image runs MCP services. It does not include an
AI Agent, Codex CLI, Agent credentials, mock Agent, or Agent service.

MCP receives the selected Project bind mount at `/project`.
The image and dependencies remain immutable at `/workspace`. HTTP MCP publishes
only on `127.0.0.1`; the stdio MCP service publishes no port. Startup does not
enqueue a Workflow or release anything.

## Build and run

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group rmed-workflow-mcp python \
  LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/runtime.py build

UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group rmed-workflow-mcp python \
  LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/runtime.py mcp-http-start
```

`mcp-http-start` reports ready only after the loopback HTTP health check passes.

## MCP

Use `mcp` for stdio MCP and `mcp-http-start` for the Project HTTP endpoint.
The HTTP listener stays loopback-only. The MCP gateway and Workbench remain
independent of the retired AI Agent runtime.

## Persistent state

| State | Location |
| --- | --- |
| Workbench runtime | `.caprmedio_runtime/workbench/` |

Historical Run data is retained outside this runtime.
