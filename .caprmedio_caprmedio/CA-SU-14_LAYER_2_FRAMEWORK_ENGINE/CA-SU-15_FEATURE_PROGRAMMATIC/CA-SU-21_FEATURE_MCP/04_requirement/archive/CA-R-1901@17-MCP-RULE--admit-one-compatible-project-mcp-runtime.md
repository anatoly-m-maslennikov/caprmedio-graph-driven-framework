---
atom_id: CA-R-1901
ref_id: CA-R-1901@17
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Container Run
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
status: Archived
version: 17
updated_at: 2026-11-09 21:15:45 +0400
carrier_destination:
  file:
    name: CA-R-1901@17-MCP-RULE--admit-one-compatible-project-mcp-runtime.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
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

### Scope

image and lifecycle admission for the selected Project's direct localhost HTTP MCP runtime.

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

### Runtime admission and reuse

the launcher **must** compute one source fingerprint, resolve one immutable image, and evaluate one selected Project runtime under its per-Project lock before it can expose a localhost MCP URL.


##### Scope

the bounded start-or-reuse procedure for the selected Project's HTTP MCP service.

1. accept a validated `ProjectSelection`, read its required Project Settings `[project_mcp] http_port` as an integer in `1..65535`, and reject a missing or invalid value before Docker effects. If `--port` is supplied, require equality with this value. With separately explicit readable `--source-root`, calculate the ordered build-input manifest and its SHA-256 fingerprint, and retain the input manifest as safe evidence. `--source-root` is for Engine/Docker build closure only and never changes Project selection or causes repository/sibling inference. Include admitted Engine, dependency-lock, Dockerfile/ignore, platform, and fixed build-argument inputs exactly once; reject a changed, missing, or unadmitted input as `IMAGE_INPUT_UNAVAILABLE`.
2. inspect an explicit immutable image digest or a locally resolved labelled image. Require the declared label schema and exact fingerprint. If no matching image is present, the launcher invocation's `build_if_missing=true` default authorizes one build; `--no-build` sets it false and returns an image refusal. Capture the builder's immutable digest, then inspect the same labels before use. Do not accept a mutable tag as the result.
3. acquire the selected identity's lock, inspect only Compose resources labelled for that identity, and compare their immutable image digest and fingerprint. Reuse only one running, healthy matching `mcp-http` service after the Host/Origin-protected host-side readiness check. A live mismatch or unhealthy service stops with its truthful disposition; it is not an instruction to stop, recreate, or replace it.
4. on an explicit startup invocation, start only `mcp-http` if no live selected runtime exists, with the selected Project mount and publication `127.0.0.1:<http_port>:8092`. Docker binds the configured port atomically. Read exactly one published mapping and require equality with Project Settings, including during reuse. An occupied port or mismatched existing publication returns failure without selecting another port or replacing the service; never reserve or test-bind a host port separately.
5. perform the host probe without password, bearer, Authorization value, or credential configuration. Validate the loopback Host/Origin boundary, bound the readiness wait, and return its failure rather than guessing readiness.
6. release the per-Project lock after recording only safe metadata. This procedure performs no MCP Tool dispatch, Gateway proxying, worker/queue/Agent start, Workflow execution, or Release action.

###### Shared display-metadata construction

Reuse one canonical image naming owner from the normal, development, release and disposable test build entrypoints. Safely read the exact source/package version.toml as part of the deterministic admitted input closure and carry framework.version in the OCI version label. After immutable image inspection, derive D594's display name/tag from that verified version, Docker Created UTC and immutable digest. Do not inject the maintenance/build-invocation clock into a cached image's date or into source fingerprinting. Check any exact tag binding, retain another image's occupied tag, apply only an absent additive tag, and read back the same immutable digest. Validated reuse with the existing same-digest tag is a no-op. R1901's explicit historical maintenance permission is separate from runtime replacement; preserve immutable returns, Project locks and every existing admission/refusal check.


###### Dependency build cache

Install the locked dependencies before copying the Framework version and application source into the image. Keep uv downloads in a BuildKit-managed cache so another build or a cancelled build does not discard completed package downloads. A version-only or source-only change must not invalidate the dependency installation layer. The version file still belongs in the final image and in its admitted input fingerprint; the OCI version label and immutable-image checks remain unchanged. Cached downloads do not replace the lockfile or admit another dependency source.

The immutable Docker runtime must start through the exact Python executable in its built /opt/venv environment, without retaining uv run as a supervising process. Dependency installation remains a locked image-build operation; retain the current runtime admission, fixed image fingerprints, no-env-file behavior, arguments and optional active-generation isolation when hot reload is explicitly enabled. Default MCP startup uses one process.

### Image and Project evidence

the delivered launcher boundary **must** carry exact image and selected-Project runtime evidence without making image tags, host ports, or credentials a substitute for admission.


##### Scope

the image-admission, selected-runtime, lock, and loopback-publication Carriers for one Project MCP launcher invocation.

- Docker Buildx client writable configuration, state, and logs use the private build attempt sibling `buildx/` directory through `BUILDX_CONFIG`. This client-only state is outside the immutable admitted context and excluded from the admitted source manifest, its fingerprint, and the image. This permits no widening of permissions, no write under `~/.docker/buildx`, and no worker.
- carry the exact ordered build-input manifest from separately explicit readable `--source-root`, its SHA-256 source fingerprint, image label schema, and resolved immutable image digest. The source root is only image/build closure and does not widen or replace Project selection. Compatibility checks use these values, not a mutable tag or a Project-derived image name. Missing packaged Engine/Docker/dependency inputs carry `IMAGE_INPUT_UNAVAILABLE` and a safe `--source-root` remediation.
- carry the selected Project identity as the Compose/resource label and namespace key, with one lock and safe runtime metadata per identity. The metadata records only resolved digest/fingerprint, service state, loopback publication, and readiness disposition; it excludes tokens and other credentials.
- the authoritative carrier is the selected control root's `caprmedio_project_settings.toml`, with `[project_mcp] http_port` as the required integer in `1..65535`. The actual per-Project value lives only there, not in runtime defaults or duplicate runtime configuration. An optional `--port` argument is an equality assertion, not an override.
- carry a direct `mcp-http` Compose invocation with selected Project context and exact loopback publication `127.0.0.1:<http_port>:8092`. Its inspected mapping confirms the configured value and does not select a different port. Startup includes no proxy sidecar, Docker socket, worker, Agent or queue service.
- deliver the small explicit `start_mcp.py` bootstrap under `.caprmedio_runtime/`, copied from its tracked Engine source during installation and refreshed during upgrade. The installed copy resolves the installed Engine package without requiring an Engine checkout in the target Project. Installation preserves Project configuration and runtime state and does not start MCP. When explicitly invoked, the bootstrap runs through uv, starts or reuses only the selected Project MCP HTTP container and returns its URL. Importing, installing or connecting to this script does not execute a Workflow; no scheduler or automatic Workflow hook is installed.
- the readiness probe carries no password, bearer, Authorization value, or credential configuration. No Carrier places an HTTP credential in a URL, argument vector, image, committed configuration, normal log, launch result, or persistent metadata.
- this Delivery supplements the existing Docker runtime and HTTP Gateway Carriers. It is not a full-Release delivery, does not repurpose Release actions, does not replace package/runtime N, and never permits live-service replacement.

###### Image display metadata

Carry version.toml within the exact admitted source/package build closure and its source fingerprint; framework.version is encoded as the Docker/OCI org.opencontainers.image.version label. Deliver repository caprmedio-runtime and the tag <framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>, deriving the date from the inspected Docker Created value and the suffix from the full immutable sha256 ID. UTC date and tag are descriptive output, not source fingerprint inputs or runtime selectors. Preserve the exact safe version string. Never emit latest/local moving aliases or move an existing tag to a different digest. Same-digest display binding is idempotent. Historical additive naming requires R1901's explicit permission and verified image/version evidence; absent evidence is reported, not reconstructed from today's checkout. Existing launch/result interfaces retain immutable image ID/fingerprint and unchanged safe Project metadata; tags grant no ownership, admission, cleanup or live replacement authority.
