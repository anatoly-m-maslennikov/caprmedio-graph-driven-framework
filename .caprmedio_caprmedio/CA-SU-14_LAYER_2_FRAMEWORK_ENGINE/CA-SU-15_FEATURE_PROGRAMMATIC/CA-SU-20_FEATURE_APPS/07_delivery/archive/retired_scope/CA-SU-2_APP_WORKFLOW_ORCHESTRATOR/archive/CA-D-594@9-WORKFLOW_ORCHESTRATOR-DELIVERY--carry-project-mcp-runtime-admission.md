---
atom_id: CA-D-594@9
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Workflow Orchestrator/Project MCP runtime admission Carrier
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - MCP
  - Subject/Engineering/Runtime/Docker Runtime
  - Image
  - Gateway
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Project.Settings
relations:
  delivery_for:
  - CA-R-1901
  - CA-M-356
  relates_to:
  - CA-D-525
  - CA-D-526
  - CA-D-578
type: Eng Decision
tier: 3
---
# Summary

carry Project MCP runtime admission

## Scope

the image-admission, selected-runtime, lock, and loopback-publication Carriers for one Project MCP launcher invocation.

## Claim

the delivered launcher boundary **must** carry exact image and selected-Project runtime evidence without making image tags, host ports, or credentials a substitute for admission.

## Details

- Docker Buildx client writable configuration, state, and logs use the private build attempt sibling `buildx/` directory through `BUILDX_CONFIG`. This client-only state is outside the immutable admitted context and excluded from the admitted source manifest, its fingerprint, and the image. This permits no widening of permissions, no write under `~/.docker/buildx`, and no worker.
- carry the exact ordered build-input manifest from separately explicit readable `--source-root`, its SHA-256 source fingerprint, image label schema, and resolved immutable image digest. The source root is only image/build closure and does not widen or replace Project selection. Compatibility checks use these values, not a mutable tag or a Project-derived image name. Missing packaged Engine/Docker/dependency inputs carry `IMAGE_INPUT_UNAVAILABLE` and a safe `--source-root` remediation.
- carry the selected Project identity as the Compose/resource label and namespace key, with one lock and safe runtime metadata per identity. The metadata records only resolved digest/fingerprint, service state, loopback publication, and readiness disposition; it excludes tokens and other credentials.
- the authoritative carrier is the selected control root's `caprmedio_project_settings.toml`, with `[project_mcp] http_port` as the required integer in `1..65535`. The actual per-Project value lives only there, not in runtime defaults or duplicate runtime configuration. An optional `--port` argument is an equality assertion, not an override.
- carry a direct `mcp-http` Compose invocation with selected Project context and exact loopback publication `127.0.0.1:<http_port>:8092`. Its inspected mapping confirms the configured value and does not select a different port. Startup includes no proxy sidecar, Docker socket, worker, Agent or queue service.
- deliver the small explicit `start_mcp.py` bootstrap under `.caprmedio_runtime/`, copied from its tracked Engine source during installation and refreshed during upgrade. The installed copy resolves the installed Engine package without requiring an Engine checkout in the target Project. Installation preserves Project configuration and runtime state and does not start MCP. When explicitly invoked, the bootstrap runs through uv, starts or reuses only the selected Project MCP HTTP container and returns its URL. Importing, installing or connecting to this script does not execute a Workflow; no scheduler or automatic Workflow hook is installed.
- the readiness probe carries no password, bearer, Authorization value, or credential configuration. No Carrier places an HTTP credential in a URL, argument vector, image, committed configuration, normal log, launch result, or persistent metadata.
- this Delivery supplements the existing Docker runtime and HTTP Gateway Carriers. It is not a full-Release delivery, does not repurpose Release actions, does not replace package/runtime N, and never permits live-service replacement.

### Image display metadata

Carry version.toml within the exact admitted source/package build closure and its source fingerprint; framework.version is encoded as the Docker/OCI org.opencontainers.image.version label. Deliver repository caprmedio-runtime and the tag <framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>, deriving the date from the inspected Docker Created value and the suffix from the full immutable sha256 ID. UTC date and tag are descriptive output, not source fingerprint inputs or runtime selectors. Preserve the exact safe version string. Never emit latest/local moving aliases or move an existing tag to a different digest. Same-digest display binding is idempotent. Historical additive naming requires R1901's explicit permission and verified image/version evidence; absent evidence is reported, not reconstructed from today's checkout. Existing launch/result interfaces retain immutable image ID/fingerprint and unchanged safe Project metadata; tags grant no ownership, admission, cleanup or live replacement authority.
