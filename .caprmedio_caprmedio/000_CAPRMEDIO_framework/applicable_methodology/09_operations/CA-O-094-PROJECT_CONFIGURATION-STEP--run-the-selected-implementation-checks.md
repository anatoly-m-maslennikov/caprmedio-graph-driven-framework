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
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 9
updated_at: "2026-10-19 15:56:39 +0400"
relations:
  relates_to:
    - CA-O-020
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-016-PROJECT_CONFIGURATION-WORKFLOW--implement-evaluations-before-required-behavior/CA-O-094-PROJECT_CONFIGURATION-STEP--run-the-selected-implementation-checks.md
  source_atom_id: CA-O-094
  source_atom_revision: 9
  source_sha256: 02890626c9020c6a3da10fa550918c33b2059e7945a1587cf1476de879ae0c10
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
