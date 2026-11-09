# CAPRMEDIO Workbench MCP

The native MCP frontier contains the 28 Workbench tools for SQL queries,
Workspaces, Views, query history, the MCP App bridge, and Workbench service
control. Subject and Topic projection builders remain local tools; they do not
need MCP registration. Local and Public release remain host commands documented
in [Project release tools](../FEATURE_PROJECT_TOOLS/README.md).

Legacy Artifact search, specialized RMED revision, selected Workflow execution,
orchestration, capability discovery, Atom mutation, Revert, and graph Workflow
routes have been retired from this MCP frontier. Methodology/source Atoms,
including RMED contracts, have not yet been reconciled with this code retirement.

## Registration

Workbench tools are registered directly by the gateway. No provider inventory,
selected Workflow manifest, capability-discovery service, or generated Tool
registry is needed to start MCP.

`project_mcp.tool_blacklist` removes exact tool names from the advertised and
callable frontier. An omitted list disables no tools. Restart the gateway after
changing settings.

## Project context

Single-project calls accept an optional top-level `project_root` assertion. It
must match the trusted Project's canonical host root or declared container
mapping. The gateway validates and removes this outer field before dispatch.
Shared MCP requires `project_root`; protocol operations such as initialization
and listing do not.

## Run

Use the project-local environment from the source checkout:

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group rmed-workflow-mcp python \
  LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/server.py --project-root "$PWD"
```

The default transport is local stdio, and the host owns its process lifetime.
This command does not register MCP with a host or refresh an installed runtime.
For runtime installation and the isolated Docker HTTP transport, use
[Project release tools](../FEATURE_PROJECT_TOOLS/README.md) and the
[Docker runtime README](../FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/README.md).

## Health and restart

The configured loopback listener serves JSON readiness at `GET /health`.
Explicit `Accept: text/html` requests receive a browser health page with
Workbench restart and reread controls. Restart the MCP process or container
after changing gateway code; implementation reload is retired. Workbench source
synchronization and its restart/reread tools remain independent.
