---
atom_id: CA-R-2008
content_role: Requirement
type: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-21 20:13:53 +0000"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  depends_on: [CA-R-1096]
---
# Summary

Serve multiple Projects through one MCP runtime

## Scope

One running Docker container and one external HTTP MCP endpoint serving multiple
explicitly bound Projects through the shared PROGRAMMATIC runtime.

## Claim

The shared runtime **must** serve every operation under exactly one validated
Project binding without conflating Project identity, applicable source/tool
frontier, mutable state, or effects. The supported Codex path is
session → Project-local `ca` Skill → every Tool call carrying the outer
`project_root` together with the native request unchanged → the same MCP.
The shared service may publish the initial union of valid native Project Tool
contracts, but a Tool name with different input/output schemas is quarantined
for the affected Project and diagnosed; no Tool meaning is changed.

## Details

- Read host configuration from `XDG_CONFIG_HOME/caprmedio/runtime.toml`, falling
  back to `~/.config/caprmedio/runtime.toml`. Its configured host
  `projects_root` is mounted read/write outside every Project; this bind
  grants no additional cross-Project authority and is not an OS-security
  isolation claim.
- Accept a Project only when its requested root is an existing canonical
  non-symlink directory strictly below the configured host `projects_root`.
  Read the Project declarations for its authoritative prefix, control root and
  full opaque identity. Never infer a Project from a prefix, ambient process
  working directory, Git ancestor, or global `current_project`. When the host
  and container paths are the same absolute root, no translation is applied.
- Bind each call to the selected Project before provider dispatch. Preserve
  Project state, DBOS, Git, Journal and output ownership at their actual
  Project owners. A root-per-call context and a ProjectGateway child key the
  selected instance; a process-global Project selector is not introduced.
- Keep the loaded/active Project context pool bounded by
  `max_loaded_projects`, default `2`; accessible Project count is not a loaded
  count. Evict only idle contexts. Refuse a busy admission at the bound and do
  not automatically retry, replay, or switch the call to another Project.
- Eagerly discover a bounded candidate Project set at startup. Permit lazy
  discovery of a new or nested Project only for an already advertised,
  compatible Tool name. A new Tool name requires an explicit shared-service
  restart and client reconnect; no `tools/list_changed` assumption is made.
  A changed host configuration requires restart and never live-remaps a
  Project root.
- Per-Project disabled or inactive Tools refuse calls. The outer
  `project_root` is added only at the native input schema root while preserving
  `$defs`; the native request and result contract remain unchanged.
- Host-shared health is ready only when the shared service is initialized and
  its published frontier is available, not when every Project job or cache is
  loaded. Show known Project contexts with their prefixes and opaque identities
  separately; an unloaded or unknown Project remains unknown. Keep the existing
  default JSON `ready` boolean, `200/503` semantics, loopback boundary and
  HTML no-path/no-effect behavior. Startup and host-scope events have no
  invented Project prefix; request logs use the actual bound prefix.
- The legacy one-Project launcher remains a separate mode until explicitly
  adopted. Its selection records are not a global one-Project restriction on
  the shared per-request runtime.

This requirement changes no native Tool input/output meaning and authorizes no
deployment, production replacement, home-config write, or active-runtime claim.
