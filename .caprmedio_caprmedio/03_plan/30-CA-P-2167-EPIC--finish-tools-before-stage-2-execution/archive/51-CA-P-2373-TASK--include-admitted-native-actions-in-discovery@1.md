---
atom_id: CA-P-2373
content_role: Plan
type: Plan
label: Task
work_sequence_number: 51
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-14 06:20:26 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Include admitted native Actions in discovery

## Objective

Discovery and execution context associate an admitted native Action with its existing exposed selected route.

## Details

Reuse CA-D-547's exact native_action_calls binding alongside ordered_actions in the shared capability catalog under CA-R-1810, CA-R-1805 and CA-R-1806. CA-O-030 belongs to update_atom even when it is not an ordered Action. Preserve selected-manifest admission, source freshness and actual exposed-server-frontier checks. Do not create a standalone native Action endpoint, invent a schema, refresh source pins, publish a manifest or claim installed readiness.

Bound implementation to capability_discovery/service.py and focused discovery tests. Keep unrelated dirty work unchanged. Root owns integration and Git. Estimated own work: up to 15 minutes; split before exceeding it.

### Definition of Done

A regression test fails before the correction and passes after it. Through the shared discovery/context paths, an admitted and exposed update_atom includes CA-O-030 exactly once. Unexposed routes, invalid or stale manifests and unrelated native Actions do not gain availability. Existing discovery checks pass. A different reviewer accepts the actual change and its bounded evidence; live MCP activation remains separate.

