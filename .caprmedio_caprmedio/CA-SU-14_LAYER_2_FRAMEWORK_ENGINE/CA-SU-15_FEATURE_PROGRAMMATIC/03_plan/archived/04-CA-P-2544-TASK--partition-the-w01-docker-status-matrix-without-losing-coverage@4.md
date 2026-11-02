---
atom_id: CA-P-2544
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
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
version: 4
updated_at: "2026-10-21T13:05:31Z"
---
# Summary

Partition the W01 Docker status matrix without losing coverage

## Objective

Partition the existing selected Docker module at one cohesive W01 matrix boundary.

## Details

Exclusive edit tests/test_selected_workflows_docker_e2e.py and new tests/test_selected_w01_status_matrix_docker_e2e.py only. Wait current source-frozen full suite terminal and root activation. Remove exactly the29-status W01test from oldclass, rehouse it in one opt-in IsolatedAsyncioTestCase that composes current harness instance, not inheritance/imported TestCase symbols. Reuse fixture/status domains/dispatch/evidence/cleanup; retain every assertion and exact29cases. New file under200lines and new cohesive executable units at most25logical lines where possible; no whitespace compression or invented exemption for remaining legacy file. Preserve old11+new1 unittest inventory, W01-W15/J01-J08coverage and Docker classifier suffix. No fixture/runner/production/deadline/MCP/Git edits or realDocker execution. At most15minutes own work; root integration owns full gate.

### Latest Operator decision

Latest Operator-approved module budget is3600seconds for the next Run, replacing this Task's earlier1800second future constraint. The source change remains test-only W01partition; runner budget/workers belong exclusively to P2546/P2547. Keep old11+new1 inventory, all29statuses, current harness/cleanup and no production API changes.

### Execution handoff after terminal failed gate

Active handoff to Luna source owner: exclusive original and new W01Docker test files only. Canonical module budget3600s in the next profile; no runner or fixture changes. Root separately owns IMAGEtest/README. Coordinate with P2545 on baseline12 ->11+1 inventory; freeze final hashes before review. New helpers should meet25logical lines and newfile200physical-line ceiling without losing assertions.

### Latest focused-only validation instruction

Latest Operator instruction: after these fixes, DO NOT rerun the full suite; run only broken and related checks. This supersedes all earlier next-full-gate clauses in this current Task/Epic. Focused acceptance includes stale image-reference tests/related image selection, scheduler regression portfolio and the original11-test plus new1-test W01Docker modules (all29statuses). Use3600second module budget,4host+2Docker capacity, isolated crash-probe scheduling; no unrelated test rerun or production mutation test. Report focused results accurately; do not call the current HEAD full-suite green or invoke the normal Local-release command that automatically reruns it.
