---
atom_id: CA-O-098
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step//Corrective Method Acceptance Step'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
version: 13
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-O-090
  - CA-R-1527
  - CA-R-1525
tier: 3
---
# Summary

Verify and activate corrective Method Drafts

## Operation

Corrective Method Acceptance Step **means** the Workflow node invoking **=1** Action, CA-O-090, **in** Integrated context under CA-R-1527.

- bind inputs from CA-O-101 **in** the separately admitted Method-learning Run: Draft references, retained passing implementation/regression checks, diagnosis **and** actual fix evidence, current baseline **and** Author bindings, selected learning Plan, existing Method authority, **and** current confidence **and** permission gates. this Step is **not** a node of CA-O-016.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

## Details
