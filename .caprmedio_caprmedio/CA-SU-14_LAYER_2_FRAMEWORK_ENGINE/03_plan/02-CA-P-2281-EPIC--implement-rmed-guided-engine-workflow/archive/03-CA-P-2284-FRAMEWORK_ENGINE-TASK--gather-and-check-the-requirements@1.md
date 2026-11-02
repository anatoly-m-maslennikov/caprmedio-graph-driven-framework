---
atom_id: CA-P-2284
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 5
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Workflow
  depends_on: [Requirement, Method, Evaluation, Delivery, Tool, Projection, Implementation, Plan, Journal, Operator, AI Agent]
version: 1
updated_at: "2026-10-13 02:55:29 +0400"
relations:
  is_decomposition_of: [CA-P-2281]
  blocks: [CA-P-2285, CA-P-2286, CA-P-2287, CA-P-2288]
---
# Summary

Gather and check the Requirements

## Objective

Provide a Step that gathers all active Requirements selected for implementation and reports their conflicts and gaps.

## Details

Accept the target Scope Unit or explicit Atom list, descendant selection and implementation boundary. Supply Active and Requirement filters explicitly; the connector does not invent selection defaults. Read each selected Atom's full relevant properties and Markdown. Separate target Rs from applicable ancestor constraints. Save a complete R projection with readable original-source references and Versions, selected IDs and exclusions. Check contradictions, unclear expected outcomes and missing inputs needed to implement them. Report exact affected sources and missing information; do not silently change their authority.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Fixtures prove complete selected-R coverage, explicit scope/status filtering and truthful missing, ambiguous and conflicting Requirement reports.

