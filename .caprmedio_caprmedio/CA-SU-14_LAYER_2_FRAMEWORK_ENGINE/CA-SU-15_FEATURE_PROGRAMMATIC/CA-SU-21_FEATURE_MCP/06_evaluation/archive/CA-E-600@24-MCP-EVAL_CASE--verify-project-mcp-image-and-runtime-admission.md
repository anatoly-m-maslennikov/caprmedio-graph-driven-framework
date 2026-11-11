---
atom_id: CA-E-600
ref_id: CA-E-600@24
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Runtime/Container Run
  - MODEL//CAPRMEDIO <+ Carrier/Docker Image
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - MODEL//CAPRMEDIO <+ Carrier
  - MODEL//CAPRMEDIO <+ Project.Settings
tier: 5
relations:
  evaluation_for:
  - CA-R-1901
status: Archived
version: 24
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-E-600@24-MCP-EVAL_CASE--verify-project-mcp-image-and-runtime-admission.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

verify Project MCP image and runtime admission

## Claim

### Prose Claim

the Evaluation **must** prove that only a matching immutable image and a healthy same-Project runtime published on the fixed Project Settings port can be used.

## Details

### Image, lock, and runtime checks

- Verify private Buildx `BUILDX_CONFIG` state/logs use only the build-attempt sibling `buildx/`; secret environment variables are excluded, the manifest remains exact, no `~/.docker/buildx` write occurs, and no worker starts.
- Test the ordered source manifest/fingerprint with changed explicit Engine, dependency, Dockerfile/ignore, platform, and argument inputs; each change must alter the fingerprint. Project carriers, credentials, installed state, generated outputs, and unrelated repository source remain outside it.
- Exercise mutable/missing/wrong-schema/fingerprint-mismatched/correct image references. Missing matching images build only under default `build_if_missing=true`; `--no-build` refuses. Capture and re-inspect an immutable digest without moving tags or replacing images; evaluate additive display metadata separately.
- A packaged launcher missing Engine/Docker/dependency input returns `IMAGE_INPUT_UNAVAILABLE`, requests `--source-root`, preserves runtime N, and does not start Release/package replacement/Framework promotion. Under held, healthy matching, unhealthy, and live-mismatch per-Project locks/runtimes, only the healthy matching case reuses; all other live cases preserve service and return a non-success disposition.
- Test `[project_mcp] http_port` valid, missing, non-integer, boolean, zero, and out-of-range values; invalid values fail before Docker and `--port` must equal Settings. Test two Projects with different ports, exact reuse, wrong publication, and occupied port: no random port, pre-reservation, or Workflow. Verify the uv bootstrap forwards only selected Project and port.
- With Docker available, start/reuse one `mcp-http` and verify exactly one `127.0.0.1:<http_port>` publication to `8092`, equal to Settings, without host pre-reservation. Docker absence/denial is incomplete/failed real-Docker evidence, not a pass. Test clean install/upgrade of `.caprmedio_runtime/start_mcp.py`: tracked package bytes, refreshed upgrade, unchanged config/state, no startup during installation, and explicit invocation against installed package without Engine checkout.
- Verify no worker, queue, Agent, Workflow, Tool call, proxy, or Release action starts.

### Readable metadata and dependency acceptance

Use frozen synthetic fixtures and the canonical naming boundary. Require and fingerprint exact `version.toml`; version changes alter identity and unrelated Project/runtime state stays excluded. New builds carry OCI version; absent/invalid version or malformed/unavailable Docker `Created` fails truthfully. Assert `caprmedio-runtime:<framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>` from inspected timestamp, including cached/reused images. Check absent-tag addition, same-digest no-op, occupied-other-digest refusal, mutable/wrong-schema/platform/fingerprint refusal, and full immutable-SHA launch. Exercise development, release, and disposable-test callers with isolated cleanup; historical maintenance requires exact identity/version/date and defers unknown evidence. Real Docker uses isolated disposable builds/readback, never production mutation or mock-only success.

Check the Dockerfile copies lock/manifest before installation, uses BuildKit uv cache, and copies Framework version after installation. Two isolated builds must demonstrate reuse of dependency-installation layer while version changes image identity. Verify `/opt/venv/bin/python` is the direct entrypoint with no retained `uv run` supervisor; the intentional active implementation-generation child remains only when hot reload is explicitly enabled. Keep locked groups, Project admission, MCP startup/health/query behavior, and report launcher memory separately from cache memory.
