---
atom_id: CA-R-1901
ref_id: CA-R-1901
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Runtime/Container Run
  - MODEL//CAPRMEDIO <+ Carrier/Docker Image
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Carrier
  - MODEL//CAPRMEDIO <+ Project.Settings
tier: 3
status: Active
version: 18
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-R-1901-MCP-RULE--admit-one-compatible-project-mcp-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-356
  - CA-D-594
---

## Summary

admit one compatible Project MCP runtime

## Claim

### Prose Claim

the launcher **must** start or reuse a Project MCP runtime only when its immutable image digest has the exact selected source fingerprint and its runtime is healthy and matches the selected Project identity and fixed MCP HTTP port from Project Settings.

## Details

### Image and runtime admission

- Compatibility is the exact deterministic manifest hash of the explicit readable `--source-root`, locked dependency inputs, Docker build inputs, and declared platform/arguments. The source root is only build closure: it is never inferred from Git, another Project, or selection; Project Atoms, installed state, credentials, and generated outputs are excluded. Labels carry the fingerprint and schema; a tag alone is not evidence.
- A missing packaged Dockerfile, dependency, or Engine input returns `IMAGE_INPUT_UNAVAILABLE` with safe missing-input identities and requests explicit `--source-root`; installed runtime N is preserved and no package replacement, Release, or Framework promotion occurs.
- An explicit image must resolve to an immutable digest with matching labels. Wrong, mutable, absent, ambiguous, or fingerprint-mismatched references refuse without retagging, live replacement, or forced recreation. When no admitted image exists, `build_if_missing=true` authorizes one build; `--no-build` refuses. The build returns an immutable labelled digest and never moves or retires an existing tag/image.
- Serialize lifecycle with one lock per selected Project identity. Reuse only a running healthy `mcp-http` runtime whose Project identity, digest/fingerprint, service identity, loopback publication, and Host/Origin-protected readiness all match; unhealthy or mismatched live state refuses without stop/restart/replacement.
- Project Settings `[project_mcp] http_port` is the required integer in `1..65535`; `--port`, when present, must equal it. Missing/invalid settings stop before Docker effects. An absent runtime starts only direct `mcp-http` on `127.0.0.1:<http_port>:8092`; Docker binds atomically and occupied ports refuse without random allocation or destructive replacement. No queue, worker, Agent, Workflow, proxy, full Release, or Release action starts.

### Runtime procedure

1. Accept validated `ProjectSelection`; read the exact Project Settings port and reject invalid values before Docker. With explicit readable `--source-root`, retain the ordered build-input manifest and fingerprint, including Engine, lock, Dockerfile/ignore, platform, and fixed arguments exactly once; changed, missing, or unadmitted input is `IMAGE_INPUT_UNAVAILABLE`.
2. Inspect an immutable digest or locally resolved labelled image and require the exact fingerprint/schema. Build only when the invocation permits it, then re-inspect the same labels; never accept a mutable tag as the result.
3. Acquire the selected identity lock, inspect only labelled Compose resources, and reuse one healthy matching `mcp-http` service after the bounded Host/Origin probe. A live mismatch or unhealthy service returns its truthful refusal.
4. On explicit startup, start only `mcp-http` with selected Project mount and `127.0.0.1:<http_port>:8092`; read exactly one publication and require equality with Project Settings. No host pre-reservation or alternate port is allowed.
5. Probe loopback Host/Origin without password, bearer, Authorization, or credential configuration, with a bounded wait; return probe failure rather than guessing readiness. Release the lock after safe metadata only. No MCP Tool dispatch, Gateway proxy, worker/queue/Agent, Workflow, or Release action.

### Display metadata and dependency cache

- Reuse one canonical naming owner for normal, development, release, and disposable-test builds. Exact `version.toml` is in the admitted closure and `framework.version` is the OCI version; use `caprmedio-runtime:<framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>`, with date from inspected Docker `Created`, not tagging time. Preserve the exact tag-safe version; missing/invalid version or Created metadata stops naming/build truthfully.
- Same-tag/same-digest is a no-op; never move occupied tags, add moving aliases, rebuild only for metadata, or change a container. Explicit maintenance may add an absent display tag only with verified original timestamp/version provenance; unknown history is deferred.
- Use private Buildx `BUILDX_CONFIG` state outside the admitted context; keep uv downloads in a BuildKit cache. Install locked dependencies before copying version/application source so version/source-only changes do not invalidate that layer. Final runtime invokes `/opt/venv/bin/python`, not a retained `uv run` supervisor; retain optional active-generation isolation only when hot reload is explicitly enabled, while default startup is one process. Cached downloads do not replace the lockfile or admit another source.

### Evidence boundary

Carry the selected identity, source manifest/fingerprint, immutable digest, safe service state, loopback publication, readiness disposition, and version/tag provenance only; exclude credentials. The launcher bootstrap is copied from tracked Engine source during install/upgrade, runs through uv only on explicit invocation, and does not install a scheduler or execute a Workflow. Delivery supplements the existing Docker/HTTP Gateway and never replaces package/runtime N or permits live-service replacement.
