# Project-scoped Docker runtime

One image supports separate MCP, durable DBOS worker, and Codex Agent services.
`project-mcp` starts or reuses only the selected Project's HTTP MCP container.
Nothing starts automatically or enqueues a Workflow during startup.

The worker and MCP receive one Project bind mount at `/project`, allowing atomic
publication from `.caprmedio_tmp/` into admitted authority and execution-state
destinations. Git metadata and the Engine mirror under that mount are read-only;
executable code and dependencies stay in the immutable image at `/workspace`.
The Agent receives no Project mount. The worker's broader Project filesystem
access is a trusted local boundary, not a per-file operating-system sandbox;
the executor still restricts edits to the explicitly admitted selection.

The worker alone applies authorized Atom proposals. The Agent has no Project,
host-home, or Docker-socket mount. It receives the explicit frozen source/rules
over the private Compose network. The ordinary worker, stdio MCP, and Agent
publish no ports. HTTP MCP publishes only on `127.0.0.1`. Containers run as a
non-root user with a read-only image and dropped capabilities.

## Build and test without credentials

From the repository root:

```sh
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py build
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py --mock start
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py --mock status
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py --mock stop
```

Docker Desktop/Engine and Compose must already be available. The image pins
Python 3.14.7, Node 22.20.0, Codex CLI 0.156.1, uv 0.12.18, and the checked-in
Python dependency lock. Build uses the invoking user's UID/GID for mount access.
Each build uses a private, attempt-local Buildx client-state cache outside the
immutable build context; it does not modify the user's global Buildx state.
The build context includes Engine source and dependency declarations, not Project
Atoms, runtime state, authentication, or `.env` files. Compose explicitly disables
implicit `.env` loading. Network restrictions still apply to image building;
Docker is not a workaround for denied registry access.

`--mock` uses a deterministic Agent and no live credentials or paid inference.
It is only for tests: do not enqueue real Atom selections against the mock Agent.
The two real-container end-to-end tests require a successful image build:

```sh
CAPRMEDIO_DOCKER_E2E=1 uv run --group workflow-orchestrator --group rmed-workflow-mcp python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p test_docker_e2e.py -v
```

These use disposable mock Projects. They check MCP admission/disconnection,
fix application, shared Journal/full report recording, terminal-result recovery,
and uncertain dispatch without replay. They do not verify model judgment.

## Live Agent authentication

Pass the exact existing Codex `auth.json` path explicitly; it is never guessed:

```sh
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py --auth-file /ABSOLUTE/PATH/TO/auth.json start
```

Only the Agent receives this runtime-only secret. On its first start it seeds a
private named volume with mode 0600; later starts retain refreshed credentials.
No token is written into an image or Project file. The live Agent alone receives
an outbound network. Protect the secret and private volume as credentials.
Revocation/rotation should be handled explicitly; supplying another seed does
not overwrite an existing Agent cache. The runtime does not expose a deletion
or credential-rotation command.

Inside the mount-isolated Agent, Codex uses the container as its isolation
boundary. This does not change the host Codex permission profile or the native
adapter's read-only policy. It is a trusted local runtime, not a multi-user service
or an adversarial isolation guarantee; the Agent can access its own credentials.

## Connect MCP and run explicitly

Configure MCP's command as `python3` and its arguments as:

```text
/ABSOLUTE/REPOSITORY/102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py
--project-root
/ABSOLUTE/REPOSITORY
mcp
```

Start the worker/Agent first. The stdio MCP container exists only for that client
connection. MCP shutdown does not stop the worker or its queue.

## Launch a selected Project MCP endpoint

Set `CAPRMEDIO_MCP_HTTP_SECRET_TOKEN` in the launching process's environment
through your credential configuration before running this command:

```sh
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py \
  --project-root /ABSOLUTE/PROJECT --source-root /ABSOLUTE/FRAMEWORK-SOURCE project-mcp
```

`--project-root` is the actual Project folder: it directly contains its own
`.caprmedio_<project>/` folder with `caprmedio_project_settings.toml` and
`project_structure.toml`.
Projects nested in one repository use their separate Project folders as roots.
The HTTP endpoint requires no local `.git`. `--control-root .caprmedio_<project>`
can explicitly select a direct control folder when needed.

The command admits a compatible immutable image, builds it when absent, and
lets Docker allocate a loopback port. JSON is the default; successful output
includes these fields, alongside Project, image, and container identities:

```json
{"disposition":"started","condition":"READY_STARTED","readiness":true,"url":"http://127.0.0.1:49152/mcp","port":49152}
```

The illustrated port is not fixed. A healthy repeat returns `reused` and
`READY_REUSED` with the same container and URL. A mismatched or unhealthy runtime
is retained and reported without replacement. Explicit recreation may change
the URL, so reconnect using the newly returned endpoint.

To request one particular loopback port, pass `--port` with an integer from
`1` through `65535`:

```sh
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py \
  --project-root /ABSOLUTE/PROJECT --source-root /ABSOLUTE/FRAMEWORK-SOURCE \
  --port 18092 project-mcp
```

The omitted default lets Docker allocate the port atomically. An existing
healthy Project runtime must already use a requested port exactly; otherwise it
is retained and reported as a mismatch. If a requested port is occupied, startup
fails without stopping the other runtime or selecting a different port.

Every `project-mcp` invocation requires `--source-root` to name a readable
Framework source checkout for image identity and build inputs. Omitting it
returns JSON with `condition: IMAGE_INPUT_UNAVAILABLE`; no repository or ancestor
is inferred. A retained Framework package lacks the Dockerfile and dependency
inputs, so supply the separate source checkout when using its launcher:

```sh
python3 /ABSOLUTE/FRAMEWORK-PACKAGE/FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py \
  --project-root /ABSOLUTE/PROJECT --source-root /ABSOLUTE/FRAMEWORK-SOURCE \
  --output url project-mcp
```

`--output url` prints only the URL on success. Failures still return JSON with
`disposition` and `condition`, exit nonzero, and contain no success URL. Use
`--no-build` to refuse a missing compatible image. `--startup-timeout` defaults
to 60 seconds and accepts at most 60; `--build-timeout` defaults to 600 seconds
and accepts at most 600. Build source is independent of the selected Project.

Docker client commands preserve configured HTTP/HTTPS/SOCKS proxy routing,
including uppercase and lowercase proxy variables. These host routing values
are not emitted in launcher results or supplied as image build arguments.

Configure your Streamable HTTP MCP client with the returned URL and a separate
`Authorization: Bearer <configured-secret>` header using the same token. The
token is absent from the URL and results, is not a command-line argument, and
is not loaded from an `.env` file. Each endpoint uses one container limited to
512 MiB and one CPU. Readiness confirms authenticated host access to MCP; this
command does not start a worker, Agent, queue, or Workflow, or grant execution
authority.

## Explicit-port localhost HTTP MCP

The Docker runtime can additionally expose Streamable HTTP MCP at a caller-chosen
loopback port. Supply both values explicitly in the invoking environment; neither
is read from an `.env` file:

```sh
CAPRMEDIO_MCP_HTTP_PORT=18092 \
CAPRMEDIO_MCP_HTTP_SECRET_TOKEN='set-a-secret-outside-the-repository' \
python3 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/runtime.py \
  --project-root "$PWD" mcp-http-start
```

On success the command returns `http://127.0.0.1:<port>/mcp`. Clients must send
the configured Bearer token. The listener rejects invalid credentials and
non-local Host or Origin values. Startup fails closed unless Compose reports one
healthy `mcp-http` service with the requested loopback TCP publication. Inspect
or stop that endpoint explicitly with `mcp-http-status` or `mcp-http-stop` using
the same environment. This HTTP service is independent of the stdio connection;
starting it neither starts a Workflow nor grants execution authority.

Alternatively, existing native MCP `workflow_orchestrator` calls route to the
Docker worker after a successful explicit `start` publishes `transport.json`.
There is no silent native fallback when Docker is stopped or unreachable. MCP
reload/reconnect is still required to load changed host bridge code.

Use the existing enqueue request and permission flags from the
[orchestrator README](../README.md). Startup, restart, and MCP connection never
create a Run. Do not reuse an existing native Run ID or silently copy its queue;
explicitly select current sources/rules and admit a fresh Docker Run.

## Persistent state and lifecycle

| State | Location |
| --- | --- |
| Docker queue, dispatches, readiness, routing | `.caprmedio_install/workflow_orchestrator/docker/` |
| Native queue/dispatches (not imported) | `.caprmedio_install/workflow_orchestrator/` |
| Existing Workflow progress and individual reports | `.caprmedio_tmp/rmed-base-revise/<run_id>/` |
| Full report | `tmp/RMED Atoms Base Revise/<run_id>.md` |
| Authoritative Journal | existing Project-registered Work Journal |
| Agent authentication | private Compose named volume |

Image source is immutable during a Run; mutable Project state stays in the
explicit mounts. `.git` is read-only: this runtime does not commit or push.
Native and Docker queues are separate, but they use the same canonical Workflow
evidence/Journal locations. Use unique Run IDs and avoid concurrent native/Docker
runs against the same Atom selection.

`stop` retains the queue, reports, Journal, and credential cache. `restart`
explicitly stops and recreates services, retaining persistent state. It may pause
uncertain work; it never blindly repeats an unacknowledged Agent call. Runtime or
prompt changes invalidate frozen implementation bindings; reconcile such Runs
with the Operator instead of replaying them under changed rules. `status` shows
container health; Workflow results still come from `get_execution_status` or
`workflow_orchestrator` status. `logs` returns the latest service logs.

The routing marker remains after stop, deliberately keeping calls fail-closed.
There is no automatic queue migration, native routing reset, hook, daemon startup,
or forced replacement of another worker.

## Validation status

Local protocol, mock-Agent, configuration, and native queue tests can run without
building this image. Actual container lifecycle tests require the image. A skipped
container test is not passing Docker end-to-end evidence. The corrected single
Project mount passed both opt-in real-container tests on 2026-10-04, including
fix/Journal/report persistence, restart recovery, and no uncertain dispatch
replay. Native mock/configuration tests passed 43 cases; nine gateway tests
passed, including explicit Docker namespace propagation without forwarding
arbitrary environment values. These do not establish model judgment.

The one-Atom live pilot `base-revise-docker-20261004055029` completed through MCP
with fixes and replacements enabled. The reviewer recorded five findings; the
fixer addressed them by replacing CA-R-1815 with active CA-R-1820 and archiving
the predecessor. Gather, check, and fix coverage were each 100%; the replacement
hashes matched the confirmed shared-Journal receipts. The terminal state is
`replaced_not_rechecked`: the Workflow does not add a semantic recheck or claim
that the successor has passed one. Both live services remained healthy.
