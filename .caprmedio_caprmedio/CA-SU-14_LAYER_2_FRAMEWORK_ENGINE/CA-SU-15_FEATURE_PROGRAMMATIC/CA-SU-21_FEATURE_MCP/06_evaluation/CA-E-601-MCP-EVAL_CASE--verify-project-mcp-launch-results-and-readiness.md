---
atom_id: CA-E-601
ref_id: CA-E-601
role: Evaluation
form: Eval Case
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 19:59:38 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime/Container Run
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Carrier
relations:
  evaluation_for:
  - CA-O-235
tier: 3
container:
  scope_unit: CA-SU-21
carrier_destination:
  file:
    name: CA-E-601-MCP-EVAL_CASE--verify-project-mcp-launch-results-and-readiness.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---
# Summary

verify Project MCP launch results and readiness

## Scope

the observable output and host-side MCP readiness boundary of the Project MCP launcher.

## Claim

the Evaluation **must** verify that every launcher disposition is structured, safe, and attributable, and that a success URL is returned only after actual loopback Host/Origin-protected host readiness.

## Details

- exercise each exact safe code in CA-O-235: `READY_STARTED`, `READY_REUSED`, `PROJECT_SELECTION_REFUSED`, `IMAGE_INPUT_UNAVAILABLE`, `IMAGE_REFUSED`, `PROJECT_LOCK_BUSY`, `RUNTIME_MISMATCH`, `RUNTIME_UNHEALTHY`, `BUILD_FAILED`, `DOCKER_START_FAILED`, `DOCKER_PUBLICATION_FAILED`, and `READINESS_FAILED`. Each outcome has one matching disposition; only ready `started`/`reused` outcomes contain a URL. Verify default JSON result output and `--output url`, which emits no URL for every non-success.
- for a real-Docker gate, connect from the host to the exact Docker-reported `127.0.0.1` port and complete the Host/Origin-protected MCP initialization/readiness exchange. Prove that container health or an open socket alone cannot produce a success URL, and that Authorization values neither grant nor deny localhost readiness.
- assert the result contains only Project identity, safe selected root/control-root references, immutable image digest/fingerprint, service/publication/readiness facts, and bounded diagnostics. Search structured output and ordinary diagnostics for password, bearer, Authorization, URL query/fragment credential, and secret-bearing environment values; none may occur.
- verify readiness and every failure case start no worker, queue, Agent, Workflow, Tool call, proxy, or Release action. Verify a failed or refused outcome preserves a live selected runtime and does not claim replacement or completion.
