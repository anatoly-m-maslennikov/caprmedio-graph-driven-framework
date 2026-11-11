---
atom_id: CA-E-601
ref_id: CA-E-601
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Runtime/Container Run
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Communication
  - MODEL//CAPRMEDIO <+ Carrier
tier: 3
relations:
  evaluation_for:
  - CA-O-235
status: Active
version: 17
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-E-601-MCP-EVAL_CASE--verify-project-mcp-launch-results-and-readiness.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

verify Project MCP launch results and readiness

## Claim

### Prose Claim

the Evaluation **must** verify that every launcher disposition is structured, safe, and attributable, and that a success URL is returned only after actual loopback Host/Origin-protected host readiness.

## Details

### Result and readiness checks

- Exercise every exact CA-O-235 safe code: READY_STARTED, READY_REUSED, PROJECT_SELECTION_REFUSED, IMAGE_INPUT_UNAVAILABLE, IMAGE_REFUSED, PROJECT_LOCK_BUSY, RUNTIME_MISMATCH, RUNTIME_UNHEALTHY, BUILD_FAILED, DOCKER_START_FAILED, DOCKER_PUBLICATION_FAILED, and READINESS_FAILED. Each maps to one disposition; only ready started/reused includes a URL. Verify default JSON and --output url, with no URL for non-success.
- In the real-Docker gate, connect to the Docker-reported 127.0.0.1 port and complete Host/Origin-protected MCP initialization/readiness. Container health/open socket alone cannot produce a success URL; Authorization neither grants nor denies localhost readiness.
- Assert output contains only safe Project identity/root references, immutable digest/fingerprint, service/publication/readiness facts, and bounded diagnostics. Search structured output/ordinary diagnostics for password, bearer, Authorization, credential URL query/fragment, and secret environment values; none may occur.
- Verify readiness and failures start no worker, queue, Agent, Workflow, Tool call, proxy, or Release action. Failed/refused outcomes preserve a live selected runtime and claim no replacement/completion.
