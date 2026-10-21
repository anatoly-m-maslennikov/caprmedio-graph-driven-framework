---
atom_id: CA-P-2543
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
version: 2
updated_at: "2026-10-21T12:53:16Z"
---
# Summary

Diagnose selected-workflow Docker case work and partition

## Objective

Identify the smallest evidence-backed way to keep complete selected Docker workflow coverage within existing bounded module execution.

## Details

Read-only Luna source/caller/fixture mapping for the timed-out module and its partial log. Find exact case inventory, per-case dispatch/container setup work and feasible cohesive module separation without duplicated unittest discovery or changed acceptance. Prefer existing shared fixture ownership; do not implement generic selectors/scheduler/batch APIs. No edits/tests/Docker/MCP/Git/release or deadline changes. At most15minutes own work. Return exact files/ownership and acceptance proposal; root records dependent implementation Tasks before any writes after the current suite terminates. Follow compact M/E/D guidance; preserve all other work.

### Reviewed diagnosis and dependent work

Read-only inventory finds12current tests:2Journal harness and10Docker class cases. The13-route aggregate completes in the actual log before the29-status W01 matrix begins; later W01work exhausts the aggregate module budget. Eight status domains still total29 (3+3+3+3+6+5+3+3). Historical completed full-module times784.239-1440.810s are context, not a current pass. Smallest coherent proposal: move only W01status matrix to test_selected_w01_status_matrix_docker_e2e.py, use composition of existing SelectedWorkflowsDockerEndToEnd('runTest') as established by native W04matrix. Oldmodule11tests plusnew1 must equal old12, no inheritance/imported-TestCase duplication. Existing filename classifier automatically admits the new Docker module; no runner/production/deadline changes. P2544/P2545 wait current suite terminal before source edits; actual timing acceptance stays in the next complete release gate.
