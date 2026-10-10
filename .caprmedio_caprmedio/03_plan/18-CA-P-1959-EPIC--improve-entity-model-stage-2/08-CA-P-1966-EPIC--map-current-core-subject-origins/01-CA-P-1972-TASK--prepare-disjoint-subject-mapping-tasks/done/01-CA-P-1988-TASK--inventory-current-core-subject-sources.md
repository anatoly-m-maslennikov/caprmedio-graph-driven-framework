---
atom_id: CA-P-1988
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 2
updated_at: "2026-10-11 01:05:16 +0400"
relations:
  is_decomposition_of: [CA-P-1972]
  blocks: ["CA-P-1990","CA-P-1991"]
---
# Summary

Inventory current Core Subject sources

## Objective

Pin every selected current Core source and Subject occurrence without proposing a replacement.

## Details

Estimated own work: 15 minutes. Inherit CA-P-1959 and CA-P-1972 boundaries. This decomposition records the expanded preparation work; it does not pretend the rejected first inventory was accepted.

Complete the one-off inventory producer and exact create-only source/batch outputs defined by stage2/current-subjects.contract.md. Reopen the registered Core path. Record all role/lifecycle exclusions, malformed selected sources and compatibility findings. Keep actual field/index/value and full source pins. Verify bounds and stable output bytes; no Source or captured-review write. Output: current-subjects.inventory.json, current-subjects.batches.json and inputs/current-subjects.batch-*.json. The old uncommitted outputs with missing Structure pins were rejected; this Task requires corrected output, not those drafts.

Root owns shared integration and Git. Preserve other workers' edits. Use uv and .caprmedio_tmp for scratch. No MCP/FPF, authority, runtime or captured-review mutation. Creating this Plan does not complete its checks.

### Definition of Done

Not Done if the required evidence/output is missing or stale, coverage or independent checks fail, a Source or captured artifact changes, unsupported authority/adoption is claimed, or own work exceeds 15 minutes without decomposition.
