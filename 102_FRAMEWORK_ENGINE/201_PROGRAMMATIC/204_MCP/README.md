# CAPRMEDIO workflow MCP

Exposes caller-coordinated **RMED Atoms Base Revise** through
`rmed_atoms_base_revise`, plus discovery, context, status/results and notification helpers.
`workflow_orchestrator` enqueues explicitly authorized independent Runs through
a separately started DBOS worker and Codex CLI adapter.
The selected-workflow first cut contains implementations for Create Atom, Update
Atom, Replace Atom, Change Status Atom, Implementation Workflow, and Build
Applicable Methodology. They are admitted only when the source-bound route
manifest reopens with current pins.
It uses the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

## Run

For development from the repository source checkout, use only the project-local
uv environment; no system Python or `.env` file is required. This stdio command
does not activate a selected installed package:

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group rmed-workflow-mcp python \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py --project-root "$PWD"
```

The default transport is local **stdio**; the MCP host owns that process lifetime.
This does not register the server with Codex or any other host. The current
file-lock implementation supports macOS and Linux. The server is bound to one
Project root at startup, not a client-supplied root on each request. Project
Settings must register the shared Journal. An explicitly started, password-free
localhost HTTP transport is available only through the isolated Docker runtime;
it is documented in the [Docker runtime README](../203_APPS/WORKFLOW_ORCHESTRATOR/docker/README.md).

## Codex Project-folder hook (shared MCP only)

[`INSTALL_TOOLS/install.py runtime --harness=codex`](../201_TOOLS/INSTALL_TOOLS/README.md)
installs the thin `PreToolUse` command hook once per host. Its canonical source
is `201_TOOLS/INSTALL_TOOLS/codex_project_context_hook.py`. The hook matches
`^mcp__caprmedio__` and uses its isolated host Python environment with `-B`. It reads Codex's
JSON event and returns `updatedInput` with outer `project_root` set to the full
session `cwd`; all native arguments remain unchanged. It does not discover a
root, walk parents or derive context from the Skill's installation folder.

Invalid context or a conflicting explicit root denies only the affected call
and emits a sanitized WARNING on stderr. Unrelated tools/events are unchanged.
The shared server still owns Project admission and containment validation.
See the [Codex hook protocol](https://learn.chatgpt.com/docs/hooks).

Review/trust the hook in Codex before use, and activate it only with the shared
MCP contract that accepts outer `project_root`. The legacy one-Project server
does not accept this field. Installing this hook is not a shared-runtime
deployment or evidence of live activation. The configured Python environment
must remain available to every session using this host-side hook. The separate
`install.py project` command configures only a Project and its thin Skill.

## Same-port health page

The existing loopback HTTP listener serves `GET /health` on the same configured
host port as `/mcp`. Machine clients receive the unchanged JSON
`{"ready":true}` or `{"ready":false}` representation with its existing 200 or
503 status. A client that explicitly requests `Accept: text/html` receives a
read-only browser view at that same URL; use the configured loopback URL from the
Docker runtime documentation and replace `/mcp` with `/health`.

The page reports gateway task availability, the already-advertised Tool registry,
and bounded process-local Tool and Workflow observations. It separates scheduler
status from actual Workflow outcome/disposition and labels missing observations
as unknown. History is limited to 32 entries per kind and resets when the gateway
restarts. It performs no Tool, Workflow, DBOS, Docker, Journal, reload or other
live probe, and exposes no arguments, results, credentials, paths or provider
exception text. `Accept: application/json`, `*/*`, missing Accept, and an HTML
media range with `q=0` retain the machine JSON response.

For independent execution, also include `--group workflow-orchestrator` before
`python` in the runtime invocation. Start the worker explicitly using its
[README](../203_APPS/WORKFLOW_ORCHESTRATOR/README.md). The worker's lifetime is
independent of this stdio adapter. The MCP does not start it implicitly.

## Selected-workflow first cut

The six retained Workflow route implementations are Create Atom, Update Atom,
Replace Atom, Change Status Atom, Implementation Workflow, and Build Applicable
Methodology. Admission remains source-pinned and currentness-checked: a route is
not discoverable or executable unless its selected manifest reopens with the
existing identity, permission, status-model, and shared-Journal evidence
boundaries.
Public status is derived from the matching recorded Workflow terminal run, not
from scheduler completion or a nested Action result. W09 Implementation Workflow
coverage uses a golden mock Agent and does not establish a live-LLM result.

Scope mutations, Revert, graph builders, standalone advanced Artifact/Journal
queries, and formal Release/promotion remain outside this first cut. A transport,
manifest route, or completed scheduler call is not execution authority.

## Project releases run outside MCP

Local and Public releases use `PROJECT_TOOLS/release.py local` and `public` on
the host. They are repository commands, separate from MCP and selected Workflow
sessions. Use the locked invocations and draft format in
[Project release tools](../../../PROJECT_TOOLS/README.md).

The reusable `release_version` and `public.release` MCP bindings remain in code.
This Project disables them with `project_mcp.tool_blacklist`; blacklisted names
are absent from discovery and cannot be called through MCP. An omitted list
disables no tools. Restart/recreate the gateway to apply settings changes;
implementation-only reload keeps the gateway's selected settings. See the
Project release documentation for the settings snippet.

Run only on Operator instruction. The complete suite, including required
current-code Docker integrations, must pass before release effects. Public
release tests its prepared version and documentation before pushing `amm/dev`
and creating/updating a Draft PR to `main`; it never merges. These source changes
do not establish that an installed MCP has been refreshed.

## Hot reload

`server.py` is now a stable stdio gateway; `implementation_server.py` runs in a
separate local process per generation. Install this gateway with one initial MCP
reconnect. Afterward invoke `reload_mcp_implementation`:

```json
{"request":{"operation":"reload","request_id":"reload-001"}}
```

Use a new request ID for a new reload; repeating an ID returns its original receipt
within the gateway session. Call `get_mcp_reload_status` with `{"request":{}}`
to inspect the current generation and in-flight counts. It is a separate read-only
Tool and performs no reload or persistence. `reload_mcp_implementation` accepts
only `operation: reload` and is explicitly state-changing. No file watcher or
automatic reload runs. Annotations do not override Codex's permission policy;
reload may still need a client-side allow rule.

Candidate initialization/schema failure keeps the old implementation serving.
Already-admitted calls finish on their original process; no calls are replayed.
The gateway emits Tool-list-change notifications when the registry changes, but
reports Codex's cache refresh as unconfirmed. A client that does not refresh still
needs reconnecting. Changes to gateway code or its Python runtime also require
reconnect; installed dependencies are never changed by a reload.

Receipts live in `.caprmedio_install/mcp_hot_reload/`; they are not Atom authority.
The DBOS worker is independent and is not restarted by MCP reload.

Candidate startup is bounded to 90 seconds. Retired generations with calls still
running after 60 seconds are marked `drain_limit_reached`; they are not forcibly
killed or replayed. A generation's `process_available` reports observed lifecycle,
not successful completion of its calls. This first slice sends legacy negotiated
Tool-list-change notifications; modern subscription-based delivery is reported
unsupported rather than claimed available.

## Workflow calls

Every call has `{"request": {"operation": "…", …}}`. The advertised schema is
a discriminated union: unknown fields and invalid operations are rejected.

| Operation | Purpose |
|---|---|
| `describe` | Return the three short prompts and usage instructions; no writes |
| `start` | Record an Operator-authorized Run with its ID, request, Author, session, Scope Unit, and timezone |
| `gather` | Save the calling session's selected `{atom_id, path}` list, `criteria_paths`, exclusions, and blockers |
| `context` | Return one Atom, current bound criteria, and the `check` or `fix` prompt; use zero-based `ordinal` |
| `submit` | Save that Atom's check or fix report; fixes also supply `after_paths` |
| `status` | Return separate reported/checked/completed counts and recording blockers |
| `handoff` | Save remaining-work context under the same Run ID |
| `finish` | Record `completed`, `interrupted`, or `failed`; unfinished selections cannot be completed |
| `report` | Read the full Markdown report |
| `sync` | Retry report/Journal recording only; never replay checks or fixes |

The calling session gathers the scope and applicable criteria, runs agentic
checks, and performs authorized fixes. This server neither interprets the scope
request into a corpus selection nor decides or applies semantic corrections.
Run only on Operator instruction; the server's presence grants no execution
authority. Current completed checks cannot be submitted as a new recheck.

`start` needs an `author` accepted by the existing Journal partition convention
(GitHub username), `session: {app, uuid}`, and `scope`. Do not fabricate them.
Settings currently resolve through `.caprmedio_caprmedio/caprmedio_project_settings.toml`;
multi-Project settings discovery is not implemented in this first slice.

## Evidence

Full report: `tmp/RMED Atoms Base Revise/<run_id>.md`. Internal state and per-Atom
JSON reports live under `.caprmedio_tmp/rmed-base-revise/<run_id>/`. Execution
events go to the configured shared Project Journal. Current rules/source drift
blocks a new correction admission; old evidence is retained. For a stale input,
resolve the change and explicitly start a newly authorized Run; no automatic
recheck occurs. Handoffs continue a running Run; terminal Runs stay immutable.

An outcome of `fixed_not_rechecked` means the reported findings have dispositions,
not that a second semantic review passed. Recording failures retain work evidence
and appear as `recording_blockers`. Run mutations are serialized with a lock;
concurrent calls for the same Run may return busy and should retry the same call.
Report submission retries are idempotent; a duplicate `start` must use `status`
to recover the existing Run rather than overwrite it.

This local interface assumes a trusted calling session and cooperative filesystem
writers. It rejects traversal, secret-file paths, and symlinks. It is not a
multi-user authorization service. Stop writes to the same Atom by other agents
while an admitted fix is in progress.

## Tests

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group rmed-workflow-mcp python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests
```

The test client uses the real stdio MCP protocol and a temporary mock Project.
It exercises gathering, checks, fixes, shared-Journal writes, full reports, and
invalid-input rejection. It does not claim to validate an LLM's semantic judgment.
