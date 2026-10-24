---
atom_id: CA-P-2581@4
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
version: 4
updated_at: "2026-10-22T18:28:31Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2577]
  depends_on: [CA-P-2579]
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

### Reviewed parallel storage boundary — 22 October 2026

Parent is Active after accepted packet/refactor prerequisites. Dependency review separates independent durable-store construction from Action semantics: CA-P-2596 may execute now; CA-P-2597 retains both the durable-store and CA-P-2580 Action-acceptance dependencies. Graph/MCP dispatch remains gated by their actual acceptance. This container has zero own implementation work; no prerequisite is waived for a dependent execution.

### Current acceptance checkpoint — 22 October 2026

The continuation/retry child portfolio has bounded evidence: CA-P-2596, CA-P-2597, CA-P-2598, CA-P-2599, CA-P-2600, CA-P-2601, CA-P-2602, CA-P-2608, CA-P-2609 and CA-P-2610 are Done; CA-C-581 is Resolved. The real-SDK journey passed 4/4 and the separate integrated, validator, packet-binding, route, status, guard and naked-stdio checks are recorded on the child Plans. This closes the focused implementation and isolated safety work only.

The installed binding remains O016@13 with CA-O-091, so the current O016@18 source/fixture reconciliation is not admitted. CA-P-2582 is the next source-binding and fixture task, followed by CA-P-2583 isolated current-Workflow verification and CA-P-2584 independent review/handoff. Current Project binding, runtime admission and handoff stay separate. Keep this zero-own-work container Active; no full-suite rerun, release, deployment or live-binding mutation is claimed.

