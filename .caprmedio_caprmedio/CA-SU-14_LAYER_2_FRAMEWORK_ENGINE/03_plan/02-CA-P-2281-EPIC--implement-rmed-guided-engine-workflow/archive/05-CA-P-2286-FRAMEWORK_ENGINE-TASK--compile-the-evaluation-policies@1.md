---
atom_id: CA-P-2286
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
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
  blocks: [CA-P-2288, CA-P-2289, CA-P-2290]
---
# Summary

Compile the Evaluation policies

## Objective

Provide a Step that compiles all applicable active Evaluation policies into one implementation projection.

## Details

Select applicable Evaluation policies governing how to create and assess tests, including scope, observable boundaries and evidence rules. Keep policies distinct from existing Standard test cases, which are retained as candidate reusable cases. Preserve their source references and Versions. Report conflicting, unclear or missing policy inputs. Reuse current PROGRAMMATIC CA-E-389 and CA-M-285: emphasize functional/public-boundary and integration checks, while retaining useful small semantic tests; do not invent a fixed unit-test quota or universal end-to-end mandate.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Fixtures distinguish Evaluation policies from test cases, preserve applicable authority and expose policy conflicts and gaps.

