---
atom_id: CA-O-092
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Evaluation Implementation Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 9
updated_at: "2026-10-21T23:57:54+00:00"
relations:
  relates_to:
    - CA-O-018
    - CA-R-1527
    - CA-R-1525
global_tier: 11
---
# Summary

Prepare tests in the implementation subagent

## Operation

Evaluation Implementation Step **means** the Workflow node invoking **=1** Action, CA-O-018, **in** Isolated context under CA-R-1527.

- bind inputs from the selected P/Plan item, assigned subagent context, governing Method Projection, R/E/D, owned work boundary, current candidate **and** tests, **and** admitted prerequisites returned by CA-O-091.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.

## Details
