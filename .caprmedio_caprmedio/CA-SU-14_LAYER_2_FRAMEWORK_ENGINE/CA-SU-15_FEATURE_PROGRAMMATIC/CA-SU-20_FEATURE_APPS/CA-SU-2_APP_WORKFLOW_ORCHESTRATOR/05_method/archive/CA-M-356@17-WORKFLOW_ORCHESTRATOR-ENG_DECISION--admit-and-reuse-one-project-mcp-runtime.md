---
atom_id: CA-M-356
ref_id: CA-M-356@17
container:
  scope_unit: CA-SU-2
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Container Run
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 4
relations:
  method_for:
  - CA-R-1901
status: Archived
version: 17
updated_at: 2026-11-07 02:24:38 +0400
carrier_destination:
  file:
    name: CA-M-356@17-WORKFLOW_ORCHESTRATOR-ENG_DECISION--admit-and-reuse-one-project-mcp-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method/archive
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

admit and reuse one Project MCP runtime

## Scope

the bounded start-or-reuse procedure for the selected Project's HTTP MCP service.

## Claim

the launcher **must** compute one source fingerprint, resolve one immutable image, and evaluate one selected Project runtime under its per-Project lock before it can expose a localhost MCP URL.

## Details

1. accept a validated `ProjectSelection`, read its required Project Settings `[project_mcp] http_port` as an integer in `1..65535`, and reject a missing or invalid value before Docker effects. If `--port` is supplied, require equality with this value. With separately explicit readable `--source-root`, calculate the ordered build-input manifest and its SHA-256 fingerprint, and retain the input manifest as safe evidence. `--source-root` is for Engine/Docker build closure only and never changes Project selection or causes repository/sibling inference. Include admitted Engine, dependency-lock, Dockerfile/ignore, platform, and fixed build-argument inputs exactly once; reject a changed, missing, or unadmitted input as `IMAGE_INPUT_UNAVAILABLE`.
2. inspect an explicit immutable image digest or a locally resolved labelled image. Require the declared label schema and exact fingerprint. If no matching image is present, the launcher invocation's `build_if_missing=true` default authorizes one build; `--no-build` sets it false and returns an image refusal. Capture the builder's immutable digest, then inspect the same labels before use. Do not accept a mutable tag as the result.
3. acquire the selected identity's lock, inspect only Compose resources labelled for that identity, and compare their immutable image digest and fingerprint. Reuse only one running, healthy matching `mcp-http` service after the Host/Origin-protected host-side readiness check. A live mismatch or unhealthy service stops with its truthful disposition; it is not an instruction to stop, recreate, or replace it.
4. on an explicit startup invocation, start only `mcp-http` if no live selected runtime exists, with the selected Project mount and publication `127.0.0.1:<http_port>:8092`. Docker binds the configured port atomically. Read exactly one published mapping and require equality with Project Settings, including during reuse. An occupied port or mismatched existing publication returns failure without selecting another port or replacing the service; never reserve or test-bind a host port separately.
5. perform the host probe without password, bearer, Authorization value, or credential configuration. Validate the loopback Host/Origin boundary, bound the readiness wait, and return its failure rather than guessing readiness.
6. release the per-Project lock after recording only safe metadata. This procedure performs no MCP Tool dispatch, Gateway proxying, worker/queue/Agent start, Workflow execution, or Release action.

### Shared display-metadata construction

Reuse one canonical image naming owner from the normal, development, release and disposable test build entrypoints. Safely read the exact source/package version.toml as part of the deterministic admitted input closure and carry framework.version in the OCI version label. After immutable image inspection, derive D594's display name/tag from that verified version, Docker Created UTC and immutable digest. Do not inject the maintenance/build-invocation clock into a cached image's date or into source fingerprinting. Check any exact tag binding, retain another image's occupied tag, apply only an absent additive tag, and read back the same immutable digest. Validated reuse with the existing same-digest tag is a no-op. R1901's explicit historical maintenance permission is separate from runtime replacement; preserve immutable returns, Project locks and every existing admission/refusal check.


### Dependency build cache

Install the locked dependencies before copying the Framework version and application source into the image. Keep uv downloads in a BuildKit-managed cache so another build or a cancelled build does not discard completed package downloads. A version-only or source-only change must not invalidate the dependency installation layer. The version file still belongs in the final image and in its admitted input fingerprint; the OCI version label and immutable-image checks remain unchanged. Cached downloads do not replace the lockfile or admit another dependency source.
