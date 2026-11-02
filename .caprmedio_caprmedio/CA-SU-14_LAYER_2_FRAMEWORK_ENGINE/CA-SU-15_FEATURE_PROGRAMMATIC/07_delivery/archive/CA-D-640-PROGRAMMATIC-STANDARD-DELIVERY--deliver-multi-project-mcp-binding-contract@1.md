---
atom_id: CA-D-640
content_role: Delivery
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-21 20:13:53 +0000"
subjects:
  governs: Entity/Carrier
  depends_on: []
relations:
  delivery_for: [CA-R-2008]
---
# Summary

Deliver the multi-Project MCP binding contract

## Scope

Host configuration, shared Docker/MCP package carriers, Project binding
records, bounded pool state and attributable operational diagnostics.

## Claim

Deliver one Docker container and one external HTTP MCP endpoint with a
restart-bound host configuration and a per-call Project binding contract.
Deliver the following exact host configuration schema outside every Project:

```toml
schema_version = 1

[shared_mcp]
projects_root = "/Users/am/Documents/My_Repos"
http_port = 8092
max_loaded_projects = 2
```

`max_loaded_projects` is optional and defaults to `2`; `projects_root` is a
configured canonical host directory, not a Project Settings source. The
`http_port` value is the configurable host-published port. The container image
listens on port `8092`; do not hard-code the historical host port `56317`.
The default config path is
`$XDG_CONFIG_HOME/caprmedio/runtime.toml`, falling back to
`~/.config/caprmedio/runtime.toml`. A changed host config requires an explicit
restart and never remaps a live Project root.

## Details

- Carry the outer `project_root`, authoritative prefix, control-root and full
  opaque Project identity with the native request and retain the binding
  revision through Tool calls, nested/asynchronous work, results, receipts and
  diagnostics. The native request, input/output schemas, `$defs` and Tool
  meaning remain unchanged.
- Deliver the host-side read/write `My_Repos` bind and the shared MCP package
  carriers at their canonical implementation places:
  `201_TOOLS/host_runtime_config.py`,
  `204_MCP/shared_gateway.py`,
  `204_MCP/shared_project_catalog.py`,
  `204_MCP/shared_project_pool.py`,
  `204_MCP/shared_http_server.py`,
  `docker/shared-mcp.compose.yaml`,
  `docker/shared_mcp_launcher.py`, and the canonical Agentic
  `205_SKILLS/ca` Project-local Skill path. These are delivery boundaries, not
  new source authority or a claim of activation.
- Include bounded union-frontier publication, per-Project disabled/inactive
  refusal and conflict diagnostics. New Tool names are published only after
  explicit shared restart/client reconnect; compatible advertised names may
  resolve a lazy Project.
- Keep Project state, DBOS, Git, Journal, caches, locks and output records at
  their actual owners. Host startup/unbound events carry no invented prefix;
  request logs identify the real bound prefix. Health displays known context
  prefixes and opaque identities separately and reports unloaded/unknown
  contexts as unknown.
- Deliver health on the same configured loopback listener with its existing
  default JSON `ready` boolean and `200/503` semantics plus escaped HTML.
  The view has no controls/effects and contains no raw payloads, credentials,
  provider exception text or absolute paths. Mounting all repositories provides
  application-level routing, not OS-level hostile-workload isolation.
- Preserve the legacy one-Project launcher as a separate mode until an
  independently authorized adoption; this delivery does not claim production
  replacement, home-config mutation, deployment or active acceptance.

## Delivery evidence

A delivery manifest must bind the schema revision, configured host path/port,
container target port, package entrypoints, Project-binding fields and
reproducible two-Project fixture/evidence references. Missing or uncertain
runtime evidence remains unresolved; a source file, projection, local commit or
configuration text alone is not deployment proof.
