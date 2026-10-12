---
atom_id: CA-P-2279
content_role: Plan
type: Plan
label: Task
work_sequence_number: 38
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Project Configuration, Workflow, Plan]
version: 1
updated_at: "2026-10-13 02:45:37 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2251, CA-P-2280]
---
# Summary

Define complete configuration Read

## Objective

The shared TOML connector has an explicit complete Configuration Read contract, with both configuration Workflows bound to its result.

## Details

Estimated own work: 15 minutes. The Operator approved FPF proposal F002: add Read to the existing shared TOML connector, not a separate snapshot supplier. This is a source-only correction of I002 from the completed approved design challenge. It is not an implementation or migration instruction.

Author the operation-specific RMEDO under CONNECTOR_TOOLS and align the affected TOOL_WORKFLOWS contracts. Reuse CA-D-625's closed logical request/result contract. Read and Modify stay independent. Read returns the complete identified configuration and exact observed source state using supplied schema, source view and read authorization. Failures return precise errors, not fabricated empty success; no configuration mutation is allowed. Both configuration Workflows consume the Read result before validating their complete proposal. Preserve Modify currentness, permission and safety checks, and one Action per Step.

A different reviewer accepts the actual changed sources, complete operation coverage, consumers, references, exact predecessors and current pins. Root owns shared Plan state and Git. Use the smallest source change and split any larger own-work portion before execution. No new transport, runtime route, Core change, live migration, retry or concurrency policy is authorized. Existing accepted receipts remain historical; changed pins require fresh acceptance and the affected follow-up review before implementation.

### Definition of Done

The Plan is **not** Done if the complete Read contract or either consumer binding is missing, independent source acceptance is absent, exact history is lost, current-state/schema/permission checks are weakened, or source edits are presented as implemented capability.
