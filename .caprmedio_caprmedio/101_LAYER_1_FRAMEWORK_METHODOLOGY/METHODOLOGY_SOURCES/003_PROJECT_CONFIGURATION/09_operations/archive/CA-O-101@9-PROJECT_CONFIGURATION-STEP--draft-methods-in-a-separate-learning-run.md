---
atom_id: CA-O-101@9
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Method Lesson Drafting Step
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Agentic Step Execution Context
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
version: 9
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-O-100
  - CA-R-1527
  - CA-R-1525
global_tier: 11
---
# Summary

Draft Methods in a separate learning run

## Operation

Method Lesson Drafting Step **means** the node invoking **=1** Action, CA-O-100, **in** Isolated context.

- bind inputs from the separately admitted Method-learning request, selected Plan, retained implementation issue/test/fix evidence, current authority, existing Method Drafts, **and** permissions.
- use a native subagent with the complete bounded handoff; MCP is **not** required. missing capability **or** context blocks the Step rather than silently changing execution context.
- retain exact Action/Step Revisions **and** actual returned evidence; pass `drafted`, `already_covered`, **or** `blocked` **to** the Workflow **without** duplicating Action behavior.

## Details
