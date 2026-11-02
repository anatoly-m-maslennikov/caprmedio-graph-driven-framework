---
atom_id: CA-P-2548@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2536
version: 2
updated_at: '2026-10-21T13:30:19Z'
---
# Summary

Verify repaired selected Docker modules in parallel

## Objective

Accept only the broken and related Docker workflow tests after the reviewed test/profile fixes, honoring the Operator's no-full-rerun decision.

## Details

Root exclusively runs .caprmedio_tmp/focused-release-repair-20261021/run_focused_docker_checks.py via canonical run_logged_test_process. One current_code_test_image context, same immutable digest for original11-test selected-workflow module plus new1-test W01status matrix, two Docker jobs,3600second per-module limit. No full suite, launcher repeat, release/version bump/adoption, production mutation tests or paid Agent. All12tests and29statussubcases execute with0skips. Preserve before/after exact network/container-ID baseline and original production metadata/health; canonical image owner cleans only unused attributed test image. Retain durable focused log and actual per-module timing/results. At most15minutes own work excluding passive tests; if blocked/failing split a concrete Concern/Task before expanding. Static41-check success and old full-run receipts are not complete current HEAD full-suite evidence.

### Actual focused verification completed

Both opted-in Docker modules passed on the same immutable current-source image: W01 matrix 1 test / all 29 role-status cases in 269.220 seconds, original portfolio 11 tests in 629.254 seconds, zero skips. They ran concurrently; no full-suite or launcher repeat. Durable log: .caprmedio_tmp/focused-release-repair-20261021/focused-docker.log. Exact before/after container and network IDs match (two existing containers, five networks); original production e812/08f and endpoint remain identical and healthy. Canonical owner removed the unused test image 28d4700c55e7ecb84be706df4f7959e66ada5cdfd21554f30a0a252ec4a4993d; direct absence readback confirmed. Together with 41 fast related checks, 53 tests passed. This is focused acceptance, not a full-green current HEAD, new release or speedup benchmark for the entire suite.
