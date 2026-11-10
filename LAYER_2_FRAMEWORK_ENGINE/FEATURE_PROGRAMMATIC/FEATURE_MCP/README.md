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

`tool_providers.json` is the editable installed Provider inventory. It has
`schema_version`, `mcp_blacklist`, and `providers`; each Provider declares its
`provider_id`, Python `module`, `factory`, and `descriptor_factory`. Generate
the required checked-in `tool_registry.json` with:

```sh
uv run --project . --locked --no-sync --all-groups python -B \
  LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/generate_tool_registry.py \
  --package-root .
```

The generated registry pins the inventory digest and descriptor models. MCP
refuses startup when either asset is missing, malformed, stale, or does not
match installed Provider code. Adding a Provider or Tool requires an installed
implementation, one inventory entry, and regeneration; gateway routing stays
generic.

`factory(project_root, gateway)` is invoked lazily to create a Provider with
`call(name, arguments)` and `close()` methods. `descriptor_factory()` returns the corresponding
`mcp.types.Tool` models. The generated registry records `inventory_sha256`,
`mcp_blacklist`, Provider fields and descriptors, and `public_tools`.
The runtime validates each registered input schema before calling its Provider
and its output schema before returning the Provider result. A Provider may
optionally implement `prepare_arguments(name, arguments, context)` and
`present_result(name, value, context)` for its own transport shaping; the
gateway never applies Workbench-specific URL behavior to other Providers.

`mcp_blacklist` denies exact public Tool names globally. Project
`project_mcp.tool_blacklist` is unioned with it, so a Project cannot re-enable
a global denial. Both lists affect advertisement and direct invocation.

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
[Docker runtime README](docker/README.md).

## Health and restart

The configured loopback listener serves JSON readiness at `GET /health`.
Explicit `Accept: text/html` requests receive a browser health page with
Workbench restart and reread controls. Restart the MCP process or container
after changing gateway code; implementation reload is retired. Workbench source
synchronization and its restart/reread tools remain independent.
