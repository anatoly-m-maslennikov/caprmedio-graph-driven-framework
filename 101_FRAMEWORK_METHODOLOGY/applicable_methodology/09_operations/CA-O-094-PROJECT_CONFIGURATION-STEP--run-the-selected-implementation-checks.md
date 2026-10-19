---
atom_id: CA-O-094
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Evaluation Step"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Occurrent/Execution/Workflow Run", "Entity/Occurrent/Execution/Step Run"]
version: 8
updated_at: "2026-10-19 03:09:18 +0400"
relations:
  relates_to:
    - CA-O-020
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior/CA-O-094-PROJECT_CONFIGURATION-STEP--run-the-selected-implementation-checks.md
  source_atom_id: CA-O-094
  source_atom_revision: 8
  source_sha256: 1c7b10b865ea6755dbbada2c624a4a77ac7e87b223bc123bd20eebd9bedc67a6
  original_relations_sha256: cd052311878518f500a8ccd80afc312a57fa48a2982146a8df18aedb7d1cbc92
---
# Summary

Run the selected implementation checks

## Operation

Implementation Evaluation Step **means** the Workflow node invoking **=1** Action, CA-O-020, **in** Integrated context under CA-R-1527.

- bind inputs from the selected P/Plan, exact current candidate **and** phase, prepared tests **and** commands, governing Method Projection **and** R/E/D, relevant complete test inputs, **and** retained issue **and** regression evidence from prior Step results.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

## Details
