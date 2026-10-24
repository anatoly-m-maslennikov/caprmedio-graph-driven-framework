---
atom_id: CA-O-094@10
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: "Implementation Evaluation Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 10
updated_at: "2026-10-22T21:21:30+04:00"
relations:
  relates_to:
    - CA-O-020
    - CA-R-1527
    - CA-R-1525
global_tier: 11
---
# Summary

Run the selected implementation checks

## Operation

Implementation Evaluation Step **means** the Workflow node invoking **=1** Action, CA-O-020, **in** Integrated context under CA-R-1527.

- bind inputs from the selected P/Plan, exact current candidate **and** phase, prepared tests **and** commands, direct full `methods` rows **and** R/E/D, relevant complete test inputs, **and** retained issue **and** regression evidence from prior Step results. An optional legacy `method_projection` may accompany those rows but is not required.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

## Details
