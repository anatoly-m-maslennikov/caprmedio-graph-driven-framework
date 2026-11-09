---
atom_id: CA-E-600@22
ref_id: CA-E-600@22
container:
  scope_unit: CA-SU-2
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Container Run
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 5
relations:
  evaluation_for:
  - CA-R-1901
  - CA-M-356
status: Archived
version: 22
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-E-600@22-WORKFLOW_ORCHESTRATOR-EVAL_CASE--verify-project-mcp-image-and-runtime-admission.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/06_evaluation/archive
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---

## Summary

verify Project MCP image and runtime admission

## Claim

### Prose Claim

the Evaluation **must** prove that only a matching immutable image and a healthy same-Project runtime published on the fixed Project Settings port can be used.

## Details

### Scope

image-fingerprint, lock, Docker-publication, and runtime-reuse checks for the Project MCP launcher.

- regression-test and real-build-check that Buildx writable configuration, state, and logs are located only in the private build attempt sibling `buildx/` directory selected by `BUILDX_CONFIG`; unrelated secret environment variables are excluded, the admitted manifest remains exact, and any failure preserves the immutable admitted context without a `~/.docker/buildx` write or worker start.
- unit-test the ordered source manifest/fingerprint against a changed explicit `--source-root` Engine, dependency, Dockerfile/ignore, platform, or build argument; each change produces a different fingerprint. Verify Project Carriers, credentials, installed state, generated outputs, and any unrelated repository source do not enter the image fingerprint.
- test explicit image references that are mutable, missing, wrong-schema, fingerprint-mismatched, or correct. Verify missing matching images build under the invocation's default `build_if_missing=true`, refuse under `--no-build`, and capture/re-inspect an immutable digest without moving an existing tag or replacing another image; additive display metadata is evaluated separately below.
- exercise a packaged launcher lacking a required Engine/Docker/dependency input. Verify `IMAGE_INPUT_UNAVAILABLE` safely requests `--source-root`, preserves installed runtime N, and does not begin a full Release, package replacement, or Framework promotion.
- simulate a held per-Project lock, a matching healthy runtime, a matching unhealthy runtime, and a live mismatched runtime. Only the healthy matching case is reusable; every other live case preserves the existing service and returns its non-success disposition.
- test the Project Settings `[project_mcp] http_port` field with valid, missing, non-integer, boolean, zero and out-of-range values. Missing or invalid values fail before any Docker effect. A supplied `--port` must equal the configured value; runtime config values do not provide a competing port source.
- test two Project roots with different configured ports, healthy exact-port reuse, an existing wrong-port publication and an occupied requested port. Failure preserves existing resources, makes no random-port attempt and launches no Workflow. Verify the small uv bootstrap forwards only the selected Project and its configured port.
- in a real-Docker gate when Docker is available, explicitly start or reuse one `mcp-http` service and verify exactly one `127.0.0.1:<http_port>` publication for container port `8092`, equal to that Project's Settings value, with no host-side pre-reservation.
- test clean installation and upgrade of the executable `.caprmedio_runtime/start_mcp.py`: its bytes match the selected Engine package, upgrade refreshes it, existing configuration and state remain unchanged, and installation starts neither MCP nor a Workflow. Test explicit bootstrap invocation against an installed package in a target Project without an Engine source checkout.
- verify the admitted launcher starts neither worker, queue, Agent, Workflow, Tool call, proxy, nor Release action. Docker absence or denial is incomplete/failed evidence for the real-Docker case, not a passing mock result.

#### Readable metadata acceptance

Use frozen synthetic source/package fixtures and the real canonical image naming boundary. Verify version.toml is required and fingerprinted; changing framework.version changes identity, and unrelated Project/runtime state remains excluded. New builds carry the exact OCI version label; absent/invalid version and malformed or unavailable Docker Created metadata fail truthfully. Assert caprmedio-runtime:<framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>, using the inspected image timestamp rather than the current maintenance clock, including cached/reused images. Check absent-tag addition, existing same-digest no-op and occupied other-digest refusal without movement. Keep mutable-ref/wrong-schema/platform/fingerprint refusals and full immutable SHA launch unchanged. Exercise development, release and disposable test-build callers with consistent packaged fixtures and safe test-image cleanup. For explicit historical maintenance, verify exact image identity/version/date, no unrelated-image or runtime change, and report unknown version evidence as deferred. Real Docker evidence uses an isolated disposable image/build and readback, never a production mutation test or a claimed pass from mocks alone.


#### Dependency cache acceptance

Check that the Dockerfile copies the dependency manifest/lock before installation, uses a BuildKit uv download cache, and copies the Framework version after dependency installation. A version-only rebuild must reuse the dependency-installation layer while still delivering the new version file and changing the admitted image identity. Verify with two isolated builds and actual build logs; do not infer cache reuse from source ordering alone. Keep the existing locked dependency groups, immutable-image/port/refusal checks and runtime-start boundaries.

Verify the Docker entrypoint directly invokes /opt/venv/bin/python with the existing service entrypoint and arguments. The service process tree has no retained uv run supervisor; the intentional active implementation-generation child remains. Verify locked build dependencies, Project admission and MCP startup/health/query behavior still hold. Report measured launcher memory separately from source-cache memory; do not claim a deployed RAM reduction from image configuration alone.
