---
atom_id: CA-P-2440
content_role: Plan
type: Plan
label: Task
work_sequence_number: 29
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: [CA-P-2459]
relations:
  is_decomposition_of: [CA-P-2401]
version: 5
updated_at: "2026-10-20T15:10:43.000Z"
---
# Summary

Replace the approved MCP image after isolated proof

## Objective

Complete one bounded Epic CA-P-2401 responsibility with truthful source, fixture and runtime evidence.

## Details

Human explicitly approved replacing running MCP only after isolated tests pass. Use canonical deployment with exact reviewed digest, production Project binding and preserved state, inspect readiness and immutable parser provenance; keep a rollback target. Coordinate Methodology safe handoff and never replay/reset the stopped batch. No broad release/auto-commit authorization inferred.

Use the PROGRAMMATIC M projection. At most15minutes own work; split dependent Tasks before extending. Preserve concurrent edits, exact predecessors and selected uv-managed environment. Review/update dependent Task before execution.

### Definition of Done

Bounded deliverable and reproducible checks are recorded, with runtime effects and limitations explicit.

### Explicit release authorization

The Operator answered Yes—use the full local release to the separate question naming automatic commits of all current changes including otherchat changes. This authorizes the normal localrelease flow only after isolatedtests pass; coordinate source/Git freeze, preserve stoppedbatchstate and record actualphase results/readiness. No publicrelease/push/merge authorization is inferred.

### Latest review gate

The final isolated receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-1q3i92q7/receipt.json` records 3 tests, 0 failures, 0 errors, 0 skips, `production_equal: true`, all 29 matrix pairs passing, Current Concern Active/Done/Canceled coverage, and `//subjects` preview with stage canonical bytes unchanged. The human explicitly approved the full local release flow including all current changes, with source freeze and the full-release approval gate recorded. This Task remains unexecuted: no MCP replacement, deployment, public release, or Git action is claimed here.

### First-attempt checkpoint

The first full local release attempt after the isolated gate failed in tests and was intentionally interrupted with exit 130 (`KeyboardInterrupt`). Root recorded Git checkpoint `c1df`, and the old production state was verified unchanged. The actual retry is delegated to CA-P-2454 after the new CA-P-2453 isolated gate passes; no historical replay or release success is claimed here.

### Successor dependency checkpoint

The second full local release terminal also failed; its bounded runner and frozen-fixture repairs are CA-P-2455 and CA-P-2456, followed by fresh build CA-P-2457, isolated gate CA-P-2458 and release retry CA-P-2459. This replacement Task now depends on CA-P-2459 and remains Active/unexecuted. No MCP replacement, deployment, readiness proof or installed-runtime resolution is claimed.
