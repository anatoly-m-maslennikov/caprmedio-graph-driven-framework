---
atom_id: CA-P-1884
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
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
    - CA-P-1886
    - CA-P-1889
---
# Summary

Add current-form golden graph fidelity cases

## Objective

Add current-form golden graph fidelity cases.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1877–CA-P-1883; any CA-P-1878 gap Tasks.

Required Plan prerequisites: [CA-P-1877](05-CA-P-1877-TASK--implement-current-source-backed-definition-recognition.md), [CA-P-1878](06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage.md), [CA-P-1881](07-CA-P-1881-TASK--separate-native-graph-facts-from-atom-incidence-and-metadata.md), [CA-P-1882](08-CA-P-1882-TASK--prepare-the-explicit-owned-core-source-selection.md), [CA-P-1883](09-CA-P-1883-TASK--bind-graph-inputs-destinations-and-actual-run-recording.md).

Output: Add current-form golden graph fidelity cases with source-backed evidence retained in this Task's work record.

Acceptance check: Nodes, edges, Property owner/value/source, roots, constraints and external references match authority; metadata-leak negative case passes.

Exclusive edit/effect scope: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/ current-form golden and negative fixtures/tests only; no unbounded implementation repairs.

Expected node/edge, Property owner/value/source, roots, constraints and external references must match pinned authority. Include a negative metadata-leak case. Required relation-gap children must be complete before this Task.

Inherit the main Epic's boundaries and CA-P-1110's 99% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Add current-form golden graph fidelity cases" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
