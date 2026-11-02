---
atom_id: CA-O-101
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Method Lesson Drafting Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Node/Continuant/Actor/Type: AI Agent", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run"]
version: 7
updated_at: "2026-10-19 15:56:52 +0400"
relations:
  relates_to:
    - CA-O-100
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-102-PROJECT_CONFIGURATION-WORKFLOW--learn-methods-from-verified-implementation-issues/CA-O-101-PROJECT_CONFIGURATION-STEP--draft-methods-in-a-separate-learning-run.md
  source_atom_id: CA-O-101
  source_atom_revision: 7
  source_sha256: 80126b7a61effbb044878e9630cd4726358df73d385cc99bbbd2e50aad1b9bf0
  original_relations_sha256: a0977c00fef855cb75511ef588cc370e664b81c980df0701e9805008dbd3288c
---
# Summary

Draft Methods in a separate learning run

## Operation

Method Lesson Drafting Step **means** the node invoking **=1** Action, CA-O-100, **in** Isolated context.

- bind inputs from the separately admitted Method-learning request, selected Plan, retained implementation issue/test/fix evidence, current authority, existing Method Drafts, **and** permissions.
- use a native subagent with the complete bounded handoff; MCP is **not** required. missing capability **or** context blocks the Step rather than silently changing execution context.
- retain exact Action/Step Revisions **and** actual returned evidence; pass `drafted`, `already_covered`, **or** `blocked` **to** the Workflow **without** duplicating Action behavior.

## Details
