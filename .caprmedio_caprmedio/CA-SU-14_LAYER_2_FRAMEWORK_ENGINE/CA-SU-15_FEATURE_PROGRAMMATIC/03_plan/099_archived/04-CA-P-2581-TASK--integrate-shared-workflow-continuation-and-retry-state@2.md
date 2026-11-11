---
atom_id: CA-P-2581
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 2
updated_at: "2026-10-22T10:17:20Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2577]
  depends_on: [CA-P-2580]
  relates_to: [CA-O-016, CA-O-230, CA-E-652]
---
# Summary

Integrate shared Workflow continuation and retry state

## Objective

Select the current adapter from trusted frozen graph identity, not overlapping Step IDs or caller flags. Carry observed results, freshness and one retry counter through revisits/recovery; retain the separately admitted release handoff without dispatching release.

## Details

One Task per file; at most 15 minutes of own work per leaf. Split before expanding. Review and update dependent Tasks after observed predecessor results, before execution. Initiative is CA-P-2577; preserve one stable action identity for each actual mutation. Use current PROGRAMMATIC M/E/D guidance and the selected locked uv environment. Preserve unrelated dirty work, exact predecessors, canonical ownership, partial results, failure visibility, retry/permission bounds and business-only Journal semantics. Create C/Problem or C/Question for actual blockers or unresolved decisions. No release, deployment, production MCP traffic, full-suite run, uncertain replay or Git publication is authorized by this Task.

This is a zero-own-work container, decomposed into CA-P-2596 through CA-P-2602 (each at most 15 minutes). Current R1527@7 and O016@17 require actual Integrated prompt/result continuation through the current participating session. Investigation found no public continuation surface: the old native path calls a separate ephemeral Codex CLI and cannot satisfy this context merely by passing prior results. Preserve the old explicitly Isolated adapter, but do not substitute it for the new Integrated path. These children remain Backlog behind the reviewed legacy-refactor gate and packet/action prerequisites. Workflow graph/result/retry authority already exists; ordinary technical envelope names do not introduce another business Workflow or policy.

### Definition of Done

Retain the bounded changed paths, current source bindings, focused commands/results and unresolved limits for this responsibility; review and update the next dependent Task before it executes.
