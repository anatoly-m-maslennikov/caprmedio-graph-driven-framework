---
atom_id: CA-P-1875
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Projection
  depends_on:
    - Entity
    - Term
    - Atom
    - Property
    - Scope Unit
    - Tool
    - MCP
    - Workflow
    - Action
    - Journal
    - Plan
version: 2
updated_at: "2026-10-09 18:10:33 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1877
---
# Summary

Record the current definition extraction contract

## Objective

Record the current definition extraction contract.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1873; pinned Core RMED and representative Claims.

Required Plan prerequisites: [CA-P-1873](01-CA-P-1873-TASK--verify-graph-admission-and-local-plan-integrity.md).

Output: Record the current definition extraction contract with source-backed evidence retained in this Task's work record.

Acceptance check: Exact admitted forms, source references and ambiguity rejection; not a new semantic authority.

Exclusive edit/effect scope: This Task's source-pinned extraction contract and evidence. Read Core RMED and representative Claims; do not edit governing Atoms.

Current Requirement Claims containing means are only definition candidates. Record the admitted Claim grammar, unique Active defining authority, matching governed target and source-backed recognition/rejection conditions, not a blanket substring rule.

Inherit the main Epic's boundaries and the Operator's explicit 90% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Record the current definition extraction contract" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
