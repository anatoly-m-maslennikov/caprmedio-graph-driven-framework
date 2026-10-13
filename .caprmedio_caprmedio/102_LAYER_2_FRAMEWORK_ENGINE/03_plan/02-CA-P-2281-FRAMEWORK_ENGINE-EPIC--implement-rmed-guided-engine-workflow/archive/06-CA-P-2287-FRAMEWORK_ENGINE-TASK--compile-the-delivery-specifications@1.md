---
atom_id: CA-P-2287
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
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
  blocks: [CA-P-2288, CA-P-2290, CA-P-2291]
---
# Summary

Compile the Delivery specifications

## Objective

Provide a Step that compiles all applicable active Delivery specifications into one implementation projection.

## Details

Include the applicable carrier, location, format, interface, dependency and package boundaries for the selected target. Use the target's declared Implementation Folder and current Project Structure. Preserve original-source references and Versions. Report contradictions, ambiguous locations and required missing Delivery information. The projection agent must not invent a Delivery choice to hide a gap.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

The D projection preserves the selected applicable Delivery authority and identifies missing or contradictory implementation boundaries.

