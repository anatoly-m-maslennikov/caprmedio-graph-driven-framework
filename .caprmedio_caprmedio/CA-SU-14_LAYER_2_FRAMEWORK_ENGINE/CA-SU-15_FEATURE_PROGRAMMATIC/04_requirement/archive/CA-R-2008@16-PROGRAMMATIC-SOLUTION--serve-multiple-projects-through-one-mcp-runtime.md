---
identity:
  atom_id: CA-R-2008
  ref_id: CA-R-2008@16
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  tier: 4
relations:
  depends_on:
  - CA-R-1096
  IS_REPLACEMENT_FOR:
  - CA-D-640
  - CA-M-401
state:
  status: Archived
  version: 16
  updated_at: 2026-11-09 21:15:45 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-2008@16-PROGRAMMATIC-SOLUTION--serve-multiple-projects-through-one-mcp-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
---

## Summary

Serve multiple Projects through one MCP runtime

## Claim

### Prose Claim

The shared runtime **must** serve every operation under exactly one validated
Project binding without conflating Project identity, applicable source/tool
frontier, mutable state, or effects. The supported Codex path is
session → Project-local `ca` Skill → every Tool call carrying the outer
`project_root` together with the native request unchanged → the same MCP.
The shared service may publish the initial union of valid native Project Tool
contracts, but a Tool name with different input/output schemas is quarantined
for the affected Project and diagnosed; no Tool meaning is changed.

## Details

### Scope

One running Docker container and one external HTTP MCP endpoint serving multiple
explicitly bound Projects through the shared PROGRAMMATIC runtime.

- Read host configuration from `XDG_CONFIG_HOME/caprmedio/runtime.toml`, falling
  back to `~/.config/caprmedio/runtime.toml`. Its configured host
  `projects_root` is mounted read/write outside every Project; this bind
  grants no additional cross-Project authority and is not an OS-security
  isolation claim.
- The canonical installation boundary is one CLI at
  `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/INSTALL_TOOLS/install.py`
  with separate `runtime` and `project` commands. `runtime` owns the
  global Docker parameters `projects_root`, `http_port` and
  `max_loaded_projects` in the host TOML outside all Projects. Both
  commands are dry-runs unless `--apply` is supplied.
- `runtime --harness=codex` may copy the standard-library hook script and
  create its isolated host environment under
  `XDG_DATA_HOME/caprmedio/runtime`, outside `projects_root`, then
  register one global hook and the loopback HTTP MCP connection while
  preserving unrelated host configuration. It does not grant trust or claim
  runtime activation. An existing conflicting CAPRMEDIO connection refuses
  before effects. An optional immutable `sha256:<64 lowercase hex>` image
  with `--apply` delegates start/readiness to the existing shared launcher;
  without an image the command configures only and reports no running
  container.
- `project` targets only the selected directory. A fresh Project requires an
  explicit prefix and seeds only minimal settings, control-root and empty
  structure; an existing prefix, configuration and structure remain
  authoritative. It installs the canonical thin Skill bundled in the release
  and performs no Docker, global MCP, global hook, Git initialization or
  copied Tool installation. Missing, ambiguous, unsafe and conflicting
  preconditions refuse before effects; own writes roll back without
  overwriting concurrent edits.
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

### Retained delivery support

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

The canonical installer is one CLI at
`LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/INSTALL_TOOLS/install.py`
with separate `runtime` and `project` commands. Both are dry-runs unless
`--apply` is supplied. `runtime` writes only the global Docker parameters
`projects_root`, `http_port` and `max_loaded_projects` to the host
TOML; `--harness=codex` copies the standard-library hook and creates the
isolated host environment under `XDG_DATA_HOME/caprmedio/runtime`, outside
all Projects, then registers the global hook and HTTP MCP connection while
preserving unrelated configuration and granting no trust. A conflicting
CAPRMEDIO connection refuses before effects. An optional immutable
`sha256:<64 lowercase hex>` image with `--apply` delegates start/readiness
to the existing shared launcher; without an image delivery is configuration
only and makes no running-service claim. `project` targets only the selected
directory, requires an explicit prefix for a fresh Project, seeds minimal
settings/control/empty structure, preserves existing Project carriers, and
installs the canonical bundled thin Skill without Docker, global MCP/hooks,
Git initialization or copied Tools. Unsafe, ambiguous, missing or conflicting
inputs refuse before effects, with exact-own-write rollback preserving
concurrent edits.

#### Details

##### Scope

Host configuration, shared Docker/MCP package carriers, Project binding
records, bounded pool state and attributable operational diagnostics.

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

##### Delivery evidence

A delivery manifest must bind the schema revision, configured host path/port,
container target port, package entrypoints, Project-binding fields and
reproducible two-Project fixture/evidence references. Missing or uncertain
runtime evidence remains unresolved; a source file, projection, local commit or
configuration text alone is not deployment proof.

### Retained binding procedure

Obtain the caller's explicit `project_root` through the supported client
contract, resolve it against the admitted host configuration and Project
declarations, then freeze one validated Project identity for the complete
operation. Carry that binding through Tool execution, asynchronous continuations,
nested calls, receipts and result attribution while preserving the native
request and each Project's actual state owners.

#### Details

##### Scope

Request binding, shared Project discovery, bounded loading and all dependent
work in the shared HTTP MCP runtime.

##### Procedure

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

##### Outcome

Every shared-MCP operation is attributable to exactly one validated Project
frontier and retains the Project's real state ownership, while one container and
one external HTTP endpoint can serve multiple Projects.

##### Failure or stop

Stop the affected call on an invalid host config, outside/symlink/ambiguous
root, missing declaration, stale mapping, unavailable/busy pool admission or
conflicting Tool contract. Refuse without selecting another Project, changing a
native Tool contract, retrying or replaying uncertain work.
