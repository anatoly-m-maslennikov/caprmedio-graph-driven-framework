---
atom_id: CA-C-576@1
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-R-1527, CA-R-1843, CA-R-1845, CA-O-016, CA-P-2581]
version: 1
updated_at: "2026-10-22T10:19:08Z"
---
# Summary

Current native Workflow dispatch lacks Integrated continuation

## Concern

Current source R1527@7 defines Integrated execution as the current participating session receiving the bound Action inputs and instructions, performing the Action and returning its result to the executor. O016@17 binds all eight current Steps as Integrated. The current native implementation path instead invokes a separate ephemeral Codex CLI callback synchronously. Retaining prior-result data does not make that separate Agent the current participating session.

Read-only inspection found no public pending-prompt/result-submission path in the current enqueue, enqueue_selected and status operations. The native graph immediately transitions after a callback result and its execution session is in memory. A frozen current-graph check also observes O231 dispatching legacy O091. This is current source and isolated-fixture evidence, not an observation of a deployed current Workflow or a production incident.

## Required disposition

After the Operator-directed three-file legacy refactor is independently accepted, implement the existing Integrated context contract through a durable bound pending frontier, prompt/input return to the current session, admitted later result submission and continuation without replaying completed Actions or effects. Reuse the existing Project, request, Run, frozen source, candidate, packet, visit and retry fields. Validate stale, conflicting, repeated and cross-Project submissions and preserve partial evidence. Keep separate-Agent callbacks available only for explicitly Isolated invocations; do not silently substitute them for Integrated Steps.

CA-P-2581 and CA-P-2596 through CA-P-2602 own the bounded implementation and isolated functional acceptance. Existing source authority owns the Workflow graph, permissions, result labels, retry accounting and release handoff; this Problem does not introduce another Workflow, new business gate or release authorization. Do not activate refreshed bindings or claim current native admission from definition-only, callback-only or fixture-integrity checks.

## Evidence boundary

The refreshed full Method projection has 39 verified current source pins. The new frozen fixture carries 17 current Workflow/Step/Action sources plus all 39 exact raw Method carriers and explicit R/D/E support; fixture integrity is distinct from native execution. Initial adapter-boundary tests are genuinely red at O231 versus O091. No production MCP, Docker replacement, full suite or deployment was used in this investigation.
