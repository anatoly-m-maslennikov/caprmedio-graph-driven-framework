---
atom_id: "CA-O-095@draft"
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: "Draft"
subjects:
  governs: "Implementation Failure Diagnosis Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 8
updated_at: "2026-10-19 11:49:07 +0000"
relations:
  relates_to:
    - CA-O-089
    - CA-R-1527
    - CA-R-1525
global_tier: 11
---
# Summary

Diagnose failures in the assigned subagent

## Operation

Implementation Failure Diagnosis Step **means** the Workflow node invoking **=1** Action, CA-O-089, **in** Isolated context under CA-R-1527.

- bind inputs from the same assigned implementation subagent context, selected P/Plan, current candidate **and** phase, failure evidence from CA-O-094, test definitions, current Method Projection **and** R/E/D, **and** applicable confidence **and** permission gates.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.

## Details
