---
atom_id: CA-R-1901
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 00:42:28 +0000"
subjects:
  governs: "Workflow Orchestrator/Project MCP runtime admission"
  depends_on: [Project, MCP, Docker Runtime, Image, Gateway, Credential, Operator, Carrier]
relations:
  relates_to: [CA-R-1818, CA-R-1819, CA-R-1884, CA-R-1885]
---
# Summary

admit one compatible Project MCP runtime

## Scope

image and lifecycle admission for the selected Project's direct localhost HTTP MCP runtime.

## Claim

the launcher **must** start or reuse a Project MCP runtime only when its immutable image digest has the exact selected source fingerprint and its existing runtime is healthy and matches that selected Project identity.

## Details

- compatibility is the exact deterministic manifest hash of the separately explicit, readable `--source-root` Engine source, locked dependency inputs, Docker build inputs, and declared build platform/arguments. The source root is used only for image identity/build closure and is never inferred from a Git repository, another Project, or Project selection. Project Atoms, installed state, credentials, and generated outputs are not build inputs. The image labels carry the fingerprint and schema; an image tag alone is not compatible-image evidence.
- a packaged launcher without the required Dockerfile, dependency, or Engine input reports `IMAGE_INPUT_UNAVAILABLE` with safe missing-input identities and requests an explicit `--source-root`. It preserves installed runtime N and does not widen this operation into a full Release, package replacement, or Framework promotion.
- an explicit image reference must resolve to an immutable digest and matching labels. A wrong, mutable, absent, ambiguous, or fingerprint-mismatched reference returns a truthful image refusal. The launcher neither retags it as compatible nor replaces a live runtime to make it match.
- when no admitted image exists, the launcher invocation's `build_if_missing` field authorizes one build by default; `--no-build` makes that field false and returns an image refusal instead. A permitted build produces an immutable resolved image digest labelled with the computed fingerprint and does not overwrite, retag, retire, or recreate an existing image or runtime.
- lifecycle serialization is one lock per selected Project identity. Under that lock, a running runtime may be reused only if its Project identity, immutable image digest/fingerprint, service identity, loopback publication, and authenticated host readiness all match. A live unhealthy or mismatched runtime returns a refusal with no stop, restart, replacement, or forced recreation.
- an absent runtime may start only the direct `mcp-http` service. Docker, not a host pre-bind probe, atomically owns a dynamic loopback port when no explicit port is requested. This admission does not start a queue, worker, Agent, Workflow, proxy, full Release, or a Release action.
