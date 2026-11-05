---
atom_id: CA-P-2410
ref_id: CA-P-2410
container:
  atom: CA-P-2408
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool//PROJECT_MCP_RUNTIME_ADMISSION
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Engineering/Workflow
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2408
status: Active
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 1-CA-P-2410-TASK--prepare-a-fresh-isolated-mcp-audit-image-and-harness.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/7-CA-P-2408-TASK--establish-and-verify-the-isolated-nonproduction-mcp-harness
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Prepare a fresh isolated MCP audit image and harness

## Objective

Admit an audit-owned disposable MCP fixture without affecting the production Project MCP, before any scoped failure reproduction.

## Details

This bounded child splits image/harness preparation from the parent safety preflight. Reuse existing current-code test image and Project launcher harnesses; do not implement a new server or change product code. Read the exact protected-root/instance/port/container receipt in .caprmedio_tmp/mcp-audit-20261020/isolation/preflight-receipt.md. Production port56317, production root/state/container/image and every retained previous fixture are excluded from test targets and cleanup.

Prepare one fresh immutable current-source test image under an audit-owned attempt; do not tag over or remove production/existing images. Use a fresh non-symlink strict child of .caprmedio_tmp/mcp-audit-20261020/isolation for project/golden fixtures and separate state/locks/cache/Runs/receipts/Journal. Verify distinct loopback ports, exact root/control-root labels, instance IDs, namespace and mounts before invoking any MCP test. Serialize Docker build/test execution, preserve declared resource caps, and stop with an attributable hold rather than exhausting host resources. No production test traffic, port probe, stop, restart, reload, redeploy or cleanup is permitted. Normal production traffic is not test evidence.

Retain protected-file and normalized production-container pre/post snapshots, exact test commands, immutable image digest, created fixture IDs/paths/ports and any fixture-only cleanup receipts. Existing two-project launcher proof may be used only with fresh fixture identities and no production selection. If readiness or guarded execution is unavailable, retain truthful unverified/blocked state; never substitute production or declare current defect resolution from source tests alone.

### Budget and dependency

Own work at most15minutes; split any longer image/harness attempt into a separately recorded bounded subtask before continuation. Use a Luna worker. Parent: CA-P-2408. The four historical audit lanes need no test endpoint. Current reproductions under CA-P-2409 require this admission and the parent isolation checks.

### Prepared admission and bounded smoke continuation

A fresh audit-only immutable image and fixture admission were prepared under the isolated attempt, with protected pre/post equality. No server or MCP smoke has run. The initial review required no-write interpreter, exact loopback-port projection and immediate source/Compose rechecks; these guards are under independent re-review. [CA-P-2419](01-CA-P-2410-TASK--prepare-a-fresh-isolated-mcp-audit-image-and-harness/01-CA-P-2419-TASK--launch-the-isolated-mcp-fixture-and-verify-context-smoke.md) owns any later bounded fixture launch/smoke only after unconditional guard acceptance. This parent remains Active until those results and production non-interference are verified.

### Definition of Done

A fresh immutable image and disposable fixture endpoint are identity-checked, scoped smoke/admission evidence and production non-interference receipts are retained, and exact supported/blocked limits are stated. No production or existing fixture is changed. Planning checkpoint: not started.
