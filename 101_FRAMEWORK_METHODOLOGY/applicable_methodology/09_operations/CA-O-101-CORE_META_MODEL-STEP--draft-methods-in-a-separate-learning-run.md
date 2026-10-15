---
atom_id: CA-O-101
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Method Lesson Drafting Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "AI Agent"
    - "Workflow Run"
    - "Step Run"
version: 3
updated_at: "2026-10-14 13:43:13 +0400"
relations:
  relates_to:
    - CA-O-100
    - CA-R-1527
    - CA-R-1525
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-102-CORE_META_MODEL-WORKFLOW--learn-methods-from-verified-implementation-issues/CA-O-101-CORE_META_MODEL-STEP--draft-methods-in-a-separate-learning-run.md
  source_atom_id: CA-O-101
  source_atom_revision: 3
  source_sha256: 4031288d0ffdf62f6b9747204f8235745ee4c150359b3c8aac89acb9f9c30bf2
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
