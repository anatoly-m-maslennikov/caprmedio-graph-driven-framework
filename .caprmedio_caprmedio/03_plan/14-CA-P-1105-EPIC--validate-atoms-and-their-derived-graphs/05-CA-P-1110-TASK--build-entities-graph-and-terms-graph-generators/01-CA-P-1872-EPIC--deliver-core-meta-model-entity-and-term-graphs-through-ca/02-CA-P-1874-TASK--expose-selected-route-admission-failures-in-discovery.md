---
atom_id: CA-P-1874
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
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
updated_at: "2026-10-09 19:23:34 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1889
---
# Summary

Expose selected-route admission failures in discovery

## Objective

Expose selected-route admission failures in discovery.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1873; existing discovery code.

Required Plan prerequisites: [CA-P-1873](01-CA-P-1873-TASK--verify-graph-admission-and-local-plan-integrity.md).

Output: Expose selected-route admission failures in discovery with source-backed evidence retained in this Task's work record.

Acceptance check: Safe actionable diagnostics; missing/stale bindings remain non-executable.

Exclusive edit/effect scope: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/capability_discovery/service.py and directly related discovery tests only.

Report safe actionable admission diagnostics without exposing secrets. Missing or stale bindings must remain non-executable; do not swallow the reason or bypass the manifest gate.

Inherit the main Epic's boundaries and the Operator's explicit 90% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Expose selected-route admission failures in discovery" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
