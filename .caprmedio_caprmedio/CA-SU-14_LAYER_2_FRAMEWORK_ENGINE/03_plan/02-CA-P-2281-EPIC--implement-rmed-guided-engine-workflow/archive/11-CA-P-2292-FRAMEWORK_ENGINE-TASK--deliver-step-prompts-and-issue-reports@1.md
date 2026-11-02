---
atom_id: CA-P-2292
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
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
  blocks: [CA-P-2293]
---
# Summary

Deliver Step prompts and issue reports

## Objective

Provide the Workflow's short subagent prompts, saved handoffs and issue reporting.

## Details

Each Step gets one fresh subagent, its current inputs, permitted Tool calls, output contract and confidence/permission boundary. Gather/compile outputs are reused by later Steps; no extra full-context preload or reviewer substeps are introduced. Every projection and implementation Step can report issues. Save one full Run report under .caprmedio_tmp/ENGINE_IMPLEMENTATION/<run_id>.md with Step outcomes, selected R IDs, projection references, coverage and remaining issues. Use the existing shared Journal for Workflow/Step/Action Run events and durable evidence. Missing Tool readiness, low confidence or required Operator decisions are explicit blocked outcomes. Do not implement a new retry/recovery subsystem.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Prompts are short and self-contained; fixtures verify fresh-agent handoffs, issue reporting, saved reports and truthful shared-Journal outcomes.

