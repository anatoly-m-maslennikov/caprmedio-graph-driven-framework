---
atom_id: CA-P-2289
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
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
  blocks: [CA-P-2290]
---
# Summary

Create Requirement-linked test cases

## Objective

Provide a Step that gives every selected Requirement at least one E test case covering its required behavior.

## Details

Read the R, M, E-policy and D projections. Reuse an existing suitable E case instead of duplicating it; otherwise create the E Atom through the new authoring Workflow and applicable permission rules. Link each case to the R it checks through the proper Evaluation relation. Cover each required failure predicate, using positive, failure and boundary cases where meaningful. Prefer stable functional/public-interface and integration boundaries; focused unit tests remain available for pure logic. Save the R-to-E-to-planned-executable-test coverage map, including any uncovered requirement or untestable ambiguity.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Every selected R has at least one named E case, all required observable outcomes are covered or explicitly unresolved, and new cases are authored through verified new Tools.

