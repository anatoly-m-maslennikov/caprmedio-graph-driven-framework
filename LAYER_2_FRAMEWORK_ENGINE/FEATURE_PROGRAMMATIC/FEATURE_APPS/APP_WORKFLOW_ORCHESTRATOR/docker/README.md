# Project-scoped Docker runtime

The image runs the durable DBOS worker and MCP services. It does not include an
AI Agent, Codex CLI, Agent credentials, mock Agent, or Agent service.

The worker and MCP receive the selected Project bind mount at `/project`.
The image and dependencies remain immutable at `/workspace`. HTTP MCP publishes
only on `127.0.0.1`; the stdio MCP service publishes no port. Startup does not
enqueue a Workflow or release anything.

## Build and run

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group workflow-orchestrator python \
  LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/runtime.py build

UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group workflow-orchestrator python \
  LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/runtime.py start
```

`start` creates the Docker worker routing marker only after Compose reports the
worker ready. `stop` retains queue and Run state. There is no native fallback if
that marker remains after Docker is stopped.

## MCP

Use `mcp` for stdio MCP and `mcp-http-start` for the Project HTTP endpoint.
The HTTP listener stays loopback-only. The MCP gateway and Workbench remain
independent of the retired AI Agent runtime.

## Persistent state

| State | Location |
| --- | --- |
| Docker queue, dispatches, readiness, routing | `.caprmedio_install/workflow_orchestrator/docker/` |
| Native queue/dispatches | `.caprmedio_install/workflow_orchestrator/` |
| Workbench runtime | `.caprmedio_runtime/workbench/` |

Historical Run data is retained. A request for a retired Agentic operation must
be rejected before queue admission; it is never routed to a mock replacement.
