---
atom_id: CA-R-1901@13
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Runtime
  - Subject/Graph Node/Engineering/Image
  - Subject/Graph Node/Engineering/Gateway
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/Project.Settings
relations:
  relates_to:
  - CA-R-1818
  - CA-R-1819
  - CA-R-1884
  - CA-R-1885
tier: 3
type: Rule
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
- when no admitted image exists, the launcher invocation's `build_if_missing` field authorizes one build by default; `--no-build` makes that field false and returns an image refusal instead. A permitted build produces an immutable resolved image digest labelled with the computed fingerprint and does not move an existing tag, overwrite or retire an image, or recreate a runtime; the additive display-metadata permission below is separate.
- lifecycle serialization is one lock per selected Project identity. Under that lock, a running runtime may be reused only if its Project identity, immutable image digest/fingerprint, service identity, loopback publication, and Host/Origin-protected host readiness all match. A live unhealthy or mismatched runtime returns a refusal with no stop, restart, replacement, or forced recreation.
- Project Settings supplies the required `[project_mcp] http_port` integer in `1..65535`. The launcher uses that exact port for this Project. Missing, non-integer, zero or out-of-range values stop before Docker effects. Runtime configuration, CLI arguments and inspected runtime metadata do not choose a replacement port. If `--port` is supplied, it must equal the Project Settings value.
- an absent runtime may start only the direct `mcp-http` service on `127.0.0.1:<http_port>:8092`. Docker atomically binds that configured port; an occupied port reports failure without random allocation, retry on another port or destructive replacement. Startup occurs only on an explicit invocation and starts no queue, worker, Agent, Workflow, proxy, full Release or Release action.

### Readable image names and version/build-date tags

CAPRMEDIO image builds and validated reuse must carry additive display metadata while continuing to return and launch only the full immutable sha256 image ID. This includes the canonical launcher/release/test builder and the development build entrypoint. The exact source/package version.toml is a required admitted fingerprint input; its framework.version is carried as org.opencontainers.image.version. Display metadata is not image compatibility, Project ownership, admission or cleanup evidence.

Use caprmedio-runtime:<framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>. Derive the timestamp from the inspected image's Docker Created value, including cache hits, not the current tagging/reuse time; date is not a source-fingerprint input. Preserve the exact Docker-tag-safe version rather than substitute a current checkout version or silently normalize it. Missing/invalid required version or Created metadata stops the affected naming/build result truthfully. A same-tag/same-digest binding is a no-op; never move an occupied tag to another digest, add latest/local moving aliases, rebuild an image merely for metadata, or change a container. Explicitly authorized maintenance may add this display tag to an existing positively identified CAPRMEDIO digest only with verified original timestamp and exact version provenance. Unknown historical versions remain reported/deferred, not guessed. This narrow permission supersedes the earlier blanket no-retag wording only for additive display metadata; mutable-reference and mismatched-image refusals remain unchanged.
