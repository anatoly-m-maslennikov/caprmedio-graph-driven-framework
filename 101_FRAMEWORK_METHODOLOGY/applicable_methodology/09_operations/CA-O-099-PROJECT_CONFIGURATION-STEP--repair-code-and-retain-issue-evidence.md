---
atom_id: CA-O-099
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Repair Step"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Occurrent/Execution/Workflow Run", "Entity/Occurrent/Execution/Step Run"]
version: 6
updated_at: "2026-10-19 03:10:21 +0400"
relations:
  relates_to:
    - CA-O-021
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior/CA-O-099-PROJECT_CONFIGURATION-STEP--repair-code-and-retain-issue-evidence.md
  source_atom_id: CA-O-099
  source_atom_revision: 6
  source_sha256: b5519a49dcc0c591a6e8895f5cf4870a491fc7d1548366715accda0a96411811
  original_relations_sha256: 1ea5c7fc0c690b75607075f32f2d9552decfced01b385e0f28a6205f30651f72
---
# Summary

Repair code and retain issue evidence

## Operation

Implementation Repair Step **means** the Workflow node invoking **=1** Action, CA-O-021, **in** Isolated context under CA-R-1527.

- bind inputs from the same assigned implementation subagent context, diagnosis from CA-O-095, admitted retry from CA-O-096, selected P/Plan **and** owned boundary, current candidate, Method Projection **and** R/E/D, regression commands, **and** retained issue **and** regression evidence.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

reuse the assigned subagent for the selected P work across its test, implementation, diagnosis, **and** repair invocations **when** available. replacement requires the complete retained input/evidence handoff **and** fresh admission; do **not** rely on unrecorded conversational memory.

## Details
