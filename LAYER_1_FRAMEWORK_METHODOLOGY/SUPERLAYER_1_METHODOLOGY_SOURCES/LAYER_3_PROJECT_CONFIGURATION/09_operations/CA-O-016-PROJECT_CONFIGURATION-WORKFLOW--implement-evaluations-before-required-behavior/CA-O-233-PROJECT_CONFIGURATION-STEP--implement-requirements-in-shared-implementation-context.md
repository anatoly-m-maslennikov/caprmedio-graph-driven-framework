---
atom_id: CA-O-233
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Requirement Implementation Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 2
updated_at: "2026-10-22T21:21:30+04:00"
relations:
  relates_to:
    - CA-O-019
    - CA-R-1527
    - CA-R-1525
global_tier: 11
---
# Summary

Implement requirements in shared implementation context

## Operation

Requirement Implementation Step **means** the Workflow node invoking **=1** Action, CA-O-019, **in** Integrated context under CA-R-1527.

- bind inputs from the selected P/Plan item **and** admitted work from CA-O-231, the same retained participating-session context, direct full `methods` rows **and** R/E/D, prepared tests from CA-O-232, baseline evidence from CA-O-094 **and** CA-O-234 **when** available, **and** the current owned work boundary. An optional legacy `method_projection` may accompany those rows but is not required.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

Retain the participating session and complete source-bound work/evidence across these Integrated invocations. A replacement requires a complete retained handoff and fresh admission; conversational memory alone is not evidence.

- retain shared request/Plan, current source-bound R/M/E/D, exact candidate and actual prior results, findings, and remaining retry/resource state. This explicit Integrated binding does not alter the context of standalone review Steps.

## Details
