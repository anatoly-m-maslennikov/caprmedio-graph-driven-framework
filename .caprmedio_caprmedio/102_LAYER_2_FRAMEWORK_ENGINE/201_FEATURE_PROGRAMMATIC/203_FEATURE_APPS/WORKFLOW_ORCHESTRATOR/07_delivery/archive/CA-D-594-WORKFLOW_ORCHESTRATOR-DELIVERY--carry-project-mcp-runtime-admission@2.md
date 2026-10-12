---
atom_id: CA-D-594
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 00:42:28 +0000"
subjects:
  governs: "Workflow Orchestrator/Project MCP runtime admission Carrier"
  depends_on: [Project, MCP, Docker Runtime, Image, Gateway, Credential, Carrier]
relations:
  delivery_for: [CA-R-1901, CA-M-356]
  relates_to: [CA-D-525, CA-D-526, CA-D-578]
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
- carry a direct `mcp-http` Compose invocation with selected Project context and no proxy sidecar, Docker socket, worker, Agent, or queue service start. Dynamic allocation uses Docker's empty-host-port loopback publication; its inspected mapping, rather than a requested free port, is the connection-port source.
- accepted readiness credentials are injected from the declared environment source only. No Carrier places them in a URL, argument vector, image, committed configuration, normal log, launch result, or persistent metadata.
- this Delivery supplements the existing Docker runtime and HTTP Gateway Carriers. It is not a full-Release delivery, does not repurpose Release actions, does not replace package/runtime N, and never permits live-service replacement.
