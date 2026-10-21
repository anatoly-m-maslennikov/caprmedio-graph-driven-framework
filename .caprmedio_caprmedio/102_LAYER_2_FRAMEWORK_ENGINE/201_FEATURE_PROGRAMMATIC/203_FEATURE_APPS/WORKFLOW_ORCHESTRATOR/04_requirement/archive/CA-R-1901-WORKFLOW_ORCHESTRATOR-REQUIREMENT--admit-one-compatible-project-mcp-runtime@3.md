---
atom_id: CA-R-1901
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-13 22:13:09 +0400"
subjects:
  governs: "Workflow Orchestrator/Project MCP runtime admission"
  depends_on: [Project, MCP, Docker Runtime, Image, Gateway, Operator, Carrier, Project Settings]
relations:
  relates_to: [CA-R-1818, CA-R-1819, CA-R-1884, CA-R-1885]
---
# Summary

admit one compatible Project MCP runtime

## Scope

image and lifecycle admission for the selected Project's direct localhost HTTP MCP runtime.

## Claim

the launcher **must** start or reuse a Project MCP runtime only when its immutable image digest has the exact selected source fingerprint and its runtime is healthy and matches the selected Project identity and fixed MCP HTTP port from Project Settings.

## Details

- compatibility is the exact deterministic manifest hash of the separately explicit, readable `--source-root` Engine source, locked dependency inputs, Docker build inputs, and declared build platform/arguments. The source root is used only for image identity/build closure and is never inferred from a Git repository, another Project, or Project selection. Project Atoms, installed state, credentials, and generated outputs are not build inputs. The image labels carry the fingerprint and schema; an image tag alone is not compatible-image evidence.
- a packaged launcher without the required Dockerfile, dependency, or Engine input reports `IMAGE_INPUT_UNAVAILABLE` with safe missing-input identities and requests an explicit `--source-root`. It preserves installed runtime N and does not widen this operation into a full Release, package replacement, or Framework promotion.
- an explicit image reference must resolve to an immutable digest and matching labels. A wrong, mutable, absent, ambiguous, or fingerprint-mismatched reference returns a truthful image refusal. The launcher neither retags it as compatible nor replaces a live runtime to make it match.
- when no admitted image exists, the launcher invocation's `build_if_missing` field authorizes one build by default; `--no-build` makes that field false and returns an image refusal instead. A permitted build produces an immutable resolved image digest labelled with the computed fingerprint and does not overwrite, retag, retire, or recreate an existing image or runtime.
- lifecycle serialization is one lock per selected Project identity. Under that lock, a running runtime may be reused only if its Project identity, immutable image digest/fingerprint, service identity, loopback publication, and Host/Origin-protected host readiness all match. A live unhealthy or mismatched runtime returns a refusal with no stop, restart, replacement, or forced recreation.
- Project Settings supplies the required `[project_mcp] http_port` integer in `1..65535`. The launcher uses that exact port for this Project. Missing, non-integer, zero or out-of-range values stop before Docker effects. Runtime configuration, CLI arguments and inspected runtime metadata do not choose a replacement port. If `--port` is supplied, it must equal the Project Settings value.
- an absent runtime may start only the direct `mcp-http` service on `127.0.0.1:<http_port>:8092`. Docker atomically binds that configured port; an occupied port reports failure without random allocation, retry on another port or destructive replacement. Startup occurs only on an explicit invocation and starts no queue, worker, Agent, Workflow, proxy, full Release or Release action.
