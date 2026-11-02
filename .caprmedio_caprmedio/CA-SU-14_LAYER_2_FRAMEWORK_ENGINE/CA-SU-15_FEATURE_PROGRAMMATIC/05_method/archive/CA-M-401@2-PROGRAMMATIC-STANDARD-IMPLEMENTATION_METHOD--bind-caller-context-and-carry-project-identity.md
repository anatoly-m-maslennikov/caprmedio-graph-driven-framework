---
atom_id: CA-M-401@2
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Project Identity Binding
  depends_on: []
relations:
  method_for: [CA-R-2008]
---
# Summary

Bind caller context and carry Project identity

## Scope

Request binding, shared Project discovery, bounded loading and all dependent
work in the shared HTTP MCP runtime.

## Claim

Obtain the caller's explicit `project_root` through the supported client
contract, resolve it against the admitted host configuration and Project
declarations, then freeze one validated Project identity for the complete
operation. Carry that binding through Tool execution, asynchronous continuations,
nested calls, receipts and result attribution while preserving the native
request and each Project's actual state owners.

## Procedure

1. Load and validate the host TOML at
   `XDG_CONFIG_HOME/caprmedio/runtime.toml`, or
   `~/.config/caprmedio/runtime.toml` when the environment variable is absent.
   Require `schema_version = 1` and a `[shared_mcp]` section with
   `projects_root`, `http_port`, and optional `max_loaded_projects` (default
   `2`). Treat a host-config change as a restart boundary.
2. Eagerly enumerate a bounded candidate set below the configured canonical
   non-symlink `projects_root`. Admit only existing canonical Project roots
   whose declarations provide an authoritative prefix, control-root and full
   opaque identity. Reject outside, missing, symlink-substituted, ambiguous or
   undeclared roots without sibling/parent/global-cwd fallback.
3. Carry the outer `project_root` plus the native request unchanged to the
   shared MCP. Resolve the same absolute host/container root without
   translation; otherwise retain the admitted mapping revision. Set the
   root-per-call context and construct a child ProjectGateway keyed by the
   validated identity. Do not set a global `current_project`.
4. Load or reuse only that Project's applicable sources, settings, model
   generation, native Tool frontier, DBOS/Git/Journal state, locks, caches and
   result paths. Derive keys from the opaque full identity, not prefix text
   alone. A context at `max_loaded_projects` may evict only an idle entry;
   refuse a busy admission and never retry or replay it.
5. Build the initial public frontier as the union of valid native Tool
   contracts from admitted Projects. A same-name Tool is shared only when its
   input and output schemas are identical. Quarantine and diagnose the
   affected Project Tool on a conflict. Add the outer `project_root` only at
   the native input schema root while preserving `$defs`; disabled/inactive
   Project Tools refuse calls and native Tool meaning remains unchanged.
6. Discover new or nested Projects lazily only for already advertised,
   compatible Tool names. Require explicit shared restart and client reconnect
   before publishing a new Tool name; do not rely on
   `tools/list_changed`. Carry the frozen binding through nested and
   asynchronous work and recheck it at existing freshness/effect boundaries;
   never silently switch mappings.
7. Keep health and diagnostics read-only. Report host readiness from initialized
   published frontier state, and show known Project contexts (prefix and opaque
   identity) separately from unloaded/unknown contexts. Host startup/log events
   are unbound; request logs use the real bound prefix. Health GETs do not
   dispatch, poll, reload, mutate or replay work.

## Outcome

Every shared-MCP operation is attributable to exactly one validated Project
frontier and retains the Project's real state ownership, while one container and
one external HTTP endpoint can serve multiple Projects.

## Failure or stop

Stop the affected call on an invalid host config, outside/symlink/ambiguous
root, missing declaration, stale mapping, unavailable/busy pool admission or
conflicting Tool contract. Refuse without selecting another Project, changing a
native Tool contract, retrying or replaying uncertain work.
