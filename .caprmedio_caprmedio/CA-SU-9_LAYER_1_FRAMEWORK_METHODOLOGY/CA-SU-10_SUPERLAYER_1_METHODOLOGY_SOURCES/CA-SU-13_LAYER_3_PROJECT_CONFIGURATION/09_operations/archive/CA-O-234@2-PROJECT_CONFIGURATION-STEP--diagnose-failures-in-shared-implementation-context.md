---
atom_id: CA-O-234@2
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Implementation Failure Diagnosis Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 2
updated_at: "2026-10-22T21:21:30+04:00"
relations:
  relates_to:
    - CA-O-089
    - CA-R-1527
    - CA-R-1525
global_tier: 11
---
# Summary

Diagnose failures in shared implementation context

## Operation

Implementation Failure Diagnosis Step **means** the Workflow node invoking **=1** Action, CA-O-089, **in** Integrated context under CA-R-1527.

- bind inputs from the same retained participating-session context, selected P/Plan, current candidate **and** phase, failure evidence from CA-O-094 or confirmed review findings from CA-O-230, test definitions, direct full `methods` rows **and** R/E/D, **and** applicable confidence **and** permission gates. An optional legacy `method_projection` may accompany those rows but is not required.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

Retain the participating session and complete source-bound work/evidence across these Integrated invocations. A replacement requires a complete retained handoff and fresh admission; conversational memory alone is not evidence.

- retain shared request/Plan, current source-bound R/M/E/D, exact candidate and actual prior results, findings, and remaining retry/resource state. This explicit Integrated binding does not alter the context of standalone review Steps.

## Details
