---
atom_id: CA-P-2579
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 3
updated_at: "2026-10-22T09:54:58Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2577]
  depends_on: [CA-P-2578, CA-P-2595]
  relates_to: [CA-O-016, CA-O-230, CA-E-652]
---
# Summary

Validate current shared Workflow packets and sources

## Objective

Implement strict boundary validation and current-source/full-Method projection checks using canonical readers. Preserve native packets and caller-owned permissions; reject stale, incomplete and cross-Project bindings before effects.

## Details

One Task per file; at most 15 minutes of own work per leaf. Split before expanding. Review and update dependent Tasks after observed predecessor results, before execution. Initiative is CA-P-2577; preserve one stable action identity for each actual mutation. Use current PROGRAMMATIC M/E/D guidance and the selected locked uv environment. Preserve unrelated dirty work, exact predecessors, canonical ownership, partial results, failure visibility, retry/permission bounds and business-only Journal semantics. Create C/Problem or C/Question for actual blockers or unresolved decisions. No release, deployment, production MCP traffic, full-suite run, uncertain replay or Git publication is authorized by this Task.

Predecessor review: CA-P-2578 is Done with 39 current Method pins, a frozen 17-source current Workflow fixture and a genuine O231-versus-O091 adapter mismatch. Preserve the existing native envelope: base_packet/step_packets, plan_item, full Method {content,sources}, list-valued evidence, flat source_bindings and Markdown-string R/D/E content. Do not introduce a replacement packet protocol. Select the current adapter using trusted frozen Workflow profile/pin and entry Step, never an untrusted caller flag or overlapping Step ID. This Task remains Backlog until independent refactor acceptance CA-P-2595 is Done.

### Definition of Done

Retain the bounded changed paths, current source bindings, focused commands/results and unresolved limits for this responsibility; review and update the next dependent Task before it executes.
