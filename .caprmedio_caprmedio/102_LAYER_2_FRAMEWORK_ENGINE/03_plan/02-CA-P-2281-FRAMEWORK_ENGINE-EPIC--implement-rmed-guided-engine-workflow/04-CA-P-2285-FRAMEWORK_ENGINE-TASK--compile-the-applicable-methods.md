---
atom_id: CA-P-2285
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 5
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Workflow
  depends_on: [Requirement, Method, Evaluation, Delivery, Tool, Projection, Implementation, Plan, Journal, Operator, AI Agent]
version: 2
updated_at: "2026-10-13 03:09:24 +0400"
relations:
  is_decomposition_of: [CA-P-2281]
  blocks: [CA-P-2288, CA-P-2290, CA-P-2291]
---
# Summary

Compile the applicable Methods

## Objective

Provide a Step that compiles all applicable active Methods into one implementation projection.

## Details

Include the target unit and applicable ancestors, such as TOOLS plus the selected TOOL_NAME; do not include unrelated sibling Tools. Include applicable Methodology and project-level constraints under the current applicability model. Preserve complete operative content and readable original-source references/Versions. The projection is derived, not editable authority. Its agent reports conflicting or ambiguous Methods and incomplete selection. Keep this compilation independent from the E and D compilation Steps so they can run in parallel after the R selection.

Use the new TOOLS workflow: run the admitted D625 `query` through CA-O-046 under CA-R-863 to return the applicable Method Atom IDs and matching facts; Query returns matches, not full content. Then invoke CA-O-047 under CA-R-864 with a D625 `read` for every selected ID. Preserve each Atom's full operative content, exact identity/Version, actual `current_state` and source evidence/attribution. Block compilation and report incomplete selected coverage if any selected Atom is missing, unreadable, malformed, truncated or otherwise incomplete; never compile partial data.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

The Method projection preserves every applicable active M, excludes unrelated/non-active inputs and reports conflicts, ambiguity or incomplete coverage.

