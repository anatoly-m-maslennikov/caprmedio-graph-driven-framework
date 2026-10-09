---
atom_id: CA-O-173
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: compile candidate Methodology"
  depends_on: [Workflow, Step, Action, Applicable Methodology, Compiler, Delivery, Journal]
version: 5
updated_at: 2026-10-09 16:36:54 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Compile the candidate Applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile`, binding only the complete delivered source manifest from CA-O-172 and the reviewed selected-snapshot compiler Tool boundary. Its candidate output is only the sealed child materialization under `.caprmedio_tmp/release_candidates/<run_id>/compiled/`; neither live root `methodology/` nor the selected Project control tree is this Step's output. CA-O-169 later promotes the same sealed export, source copy and projection after the complete gate. A later installed projection is not compiler output authority.

## Details

This is not another compiler graph: CA-O-166 uses the reviewed Tool boundary required for a selected pinned snapshot while preserving source authority. A changed frontier, incomplete delivery, unbound Tool/layout, child-materialization mismatch, or any source/delivery mutation stops without runtime installation, image work or promotion.
