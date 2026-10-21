---
atom_id: CA-P-2536
content_role: Plan
type: Plan
label: Task
work_sequence_number: 89
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
  is_decomposition_of: [CA-P-2401]
version: 2
updated_at: "2026-10-21T11:55:43Z"
---
# Summary

Run fresh Local release after isolated suite repair

## Objective

Complete the Operator-requested full Local release after P2533's reviewed scheduler repair, then resume native container acceptance.

## Details

Root exclusively owns Git, real release and Docker mutations. Freeze source before launch. Use Project3.14virtualenv and canonical O164host command with NEW Run local-20261021-isolated-gate-114321, not interrupted-run replay. Complete full suite before version/product/image/adoption. Canonical dated/versioned image naming then exact candidate MCP replacement/smoke precedes selected-Project-only retention. Preserve foreign/unowned/referenced images and all safety checks; no force/prune/push. Observe actual report/log/runtime digest/version/health and tool discovery; separate failure, cleanup_pending and installed acceptance. C565 remains Active until actual gate evidence; C564 is separate acknowledged source-conformance debt, not waived. At most15minutes own work excluding passive gate wait, split any discovered repair into new Tasks/Concerns. No production mutation tests or held replay. Native Epic acceptance follows only after terminal release state.

### Latest actual checkpoint

Fresh Run local-20261021-isolated-gate-114321 failed its full suite: test_docker_e2e anonymousHTTPstartup could not create Compose networks because all predefined Docker address pools were fully subnetted (3tests/1error135.597s). Prior crash module25/25passed397.444s; C565Resolved@3. Root inspected exact releasePID96380 and sentINT only after confirmed failed gate; terminalreportfailed/tests/KeyboardInterrupt/exit130 preserves preceding RuntimeError in testlog. No delivery/versionbump/adoption/retention occurred; original0.4.4.9 MCP unchanged. C566/P2537 now own bounded network attribution/cleanup-lifetime diagnosis; no blind retry, broadprune or foreignresource deletion.
