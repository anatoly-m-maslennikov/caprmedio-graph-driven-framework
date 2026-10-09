---
atom_id: CA-P-1882
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
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
version: 1
updated_at: "2026-10-09 17:13:17 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1883
    - CA-P-1884
---
# Summary

Prepare the explicit owned-Core source selection

## Objective

Prepare the explicit Core source selection.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1873; pinned Structure and current Atom Properties.

Required Plan prerequisites: [CA-P-1873](01-CA-P-1873-TASK--verify-graph-admission-and-local-plan-integrity.md), [CA-P-1881](07-CA-P-1881-TASK--separate-native-graph-facts-from-atom-incidence-and-metadata.md).

Output: Prepare the explicit Core source selection with source-backed evidence retained in this Task's work record.

Acceptance check: Active owned-Core predicate; target scope stays separate; malformed/missing/duplicate sources are reported.

Exclusive edit/effect scope: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/ explicit source-selection helper and its focused fixtures only; read project_structure.toml and carried Properties, never change source Atoms.

Use current Active Atoms with current_scope_unit == CORE_META_MODEL. Keep claim_target_scope_unit separate. Bind current Project Structure and explicit Properties; record admitted support sources/external references separately. Do not infer membership from folders or add recursion/query grammar without authority.

Inherit the main Epic's boundaries and CA-P-1110's 99% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Prepare the explicit Core source selection" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
