---
status: Archived
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Launch Project localhost MCP runtime"
  depends_on: [Action, Project, MCP, Gateway, Docker Runtime, Image, Credential, Carrier]
version: 1
updated_at: "2026-10-09 00:42:28 +0000"
relations: {}
---
# launch one Project localhost MCP runtime

launch Project localhost MCP runtime **means** the reusable bounded Action that selects one Project context and returns a directly reachable, authenticated localhost MCP endpoint only after exact image admission and host-side readiness. Its modeled boundary is one Project MCP service; it is not a Release action, proxy, worker controller, queue controller, or Workflow executor.

## Applicable when

an Operator invokes `project-mcp` for one Project-local HTTP MCP service with `--project-root repo` (the declared Project root) or one safe explicit Project-root path, an optional direct `--control-root .caprmedio_name`, separately explicit readable `--source-root` for image/build closure, the explicit accepted environment credential source, optional `--no-build`, explicit port, and bounded readiness timeout. `build_if_missing` is true for this invocation unless `--no-build` is supplied; the selected Project root need not be a Git root.

## Action

1. resolve exactly one `ProjectSelection` by CA-M-355. Return its attributable selection refusal unchanged if it is missing, unsafe, invalid, ambiguous, or has changed bindings.
2. require the explicit accepted environment credential source before a service start or readiness request. Read its value only for service injection and authenticated host readiness; never serialize it into the request, command line, URL, result, normal log, image, or persistent launcher state.
3. acquire only the selected identity's lock, calculate the exact admitted source fingerprint from `--source-root`, and resolve one immutable matching image by CA-M-356. A missing required source input returns `IMAGE_INPUT_UNAVAILABLE` with a safe request for `--source-root`, without a package/runtime-N change or Release operation. Build an absent matching image when this invocation retains its default `build_if_missing=true`; `--no-build` returns an image refusal. Refuse an explicit wrong/mutable image rather than retagging or replacing it.
4. reuse only one healthy matching selected-Project service after the bounded authenticated loopback readiness probe. If the selected service is live but unhealthy or mismatched, return its refusal without stop, restart, recreate, replacement, or fallback to another Project.
5. when the selected service is absent, start only direct `mcp-http`. Use the explicit `1..65535` loopback port when given; otherwise request Docker-owned dynamic loopback publication and read back exactly one published port. Do not reserve a host port, start a proxy, worker, queue, Agent, Workflow, Tool call, or Release action.
6. perform a bounded authenticated host-side MCP initialization/readiness exchange over the returned loopback URL. Docker health, a container PID, or an open socket alone is insufficient. Return URL and `ready` only after that exchange succeeds.

## Outcome

the default result is JSON with one structured `started`, `reused`, `refused`, `failed`, or `busy` disposition and exactly one safe condition code: `READY_STARTED`, `READY_REUSED`, `PROJECT_SELECTION_REFUSED`, `CREDENTIAL_SOURCE_REFUSED`, `IMAGE_INPUT_UNAVAILABLE`, `IMAGE_REFUSED`, `PROJECT_LOCK_BUSY`, `RUNTIME_MISMATCH`, `RUNTIME_UNHEALTHY`, `BUILD_FAILED`, `DOCKER_START_FAILED`, `DOCKER_PUBLICATION_FAILED`, or `READINESS_FAILED`. It contains safe Project identity, immutable image digest/fingerprint, service disposition, bounded readiness disposition, and, on ready success only, `http://127.0.0.1:<assigned-port>/mcp`. `--output url` emits that URL only for a ready success; every non-success remains an attributable structured result and emits no URL. It never returns a credential, an authorization header, a secret-bearing environment value, or success before authenticated host readiness.

## Failure or stop

stop with the explicit selection, credential-source, image-admission, lock, Docker-publication, or readiness condition when it cannot reach the stated Outcome. Do not infer success, substitute a Project/image/port, retry an unknown effect, or widen this Action into a queue, worker, Workflow, proxy, or Release operation.
