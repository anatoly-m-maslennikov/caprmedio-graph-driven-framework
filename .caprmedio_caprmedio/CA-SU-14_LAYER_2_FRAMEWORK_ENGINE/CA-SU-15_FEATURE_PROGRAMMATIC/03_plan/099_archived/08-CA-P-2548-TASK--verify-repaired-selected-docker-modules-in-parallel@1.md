---
atom_id: CA-P-2548
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
version: 1
updated_at: "2026-10-21T13:14:49Z"
---
# Summary

Verify repaired selected Docker modules in parallel

## Objective

Accept only the broken and related Docker workflow tests after the reviewed test/profile fixes, honoring the Operator's no-full-rerun decision.

## Details

Root exclusively runs .caprmedio_tmp/focused-release-repair-20261021/run_focused_docker_checks.py via canonical run_logged_test_process. One current_code_test_image context, same immutable digest for original11-test selected-workflow module plus new1-test W01status matrix, two Docker jobs,3600second per-module limit. No full suite, launcher repeat, release/version bump/adoption, production mutation tests or paid Agent. All12tests and29statussubcases execute with0skips. Preserve before/after exact network/container-ID baseline and original production metadata/health; canonical image owner cleans only unused attributed test image. Retain durable focused log and actual per-module timing/results. At most15minutes own work excluding passive tests; if blocked/failing split a concrete Concern/Task before expanding. Static41-check success and old full-run receipts are not complete current HEAD full-suite evidence.
