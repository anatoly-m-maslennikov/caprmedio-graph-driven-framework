---
atom_id: CA-P-1879@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Entity
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Tool
  - MCP
  - Workflow
  - Action
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-1878
  blocks:
  - CA-P-1881
tier: 3
---
# Summary

Implement current term hierarchy extraction

## Objective

Implement current term hierarchy extraction.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1876; existing hierarchy parser.

Required Plan prerequisites: [CA-P-1876](../04-CA-P-1876-TASK--record-graph-qualified-relation-and-property-ownership-contracts.md), [CA-P-1877](../05-CA-P-1877-TASK--implement-current-source-backed-definition-recognition.md).

Output: Implement current term hierarchy extraction with source-backed evidence retained in this Task's work record.

Acceptance check: Correct `NARROWER_THAN` direction and source evidence; no unsupported alias.

Exclusive edit/effect scope: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/ term hierarchy extractor and its focused fixtures only.

Use the current NARROWER_THAN contract with correct direction and evidence. Do not silently accept legacy SUBKIND_OF.

Inherit the main Epic's boundaries and the Operator's explicit 90% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Implement current term hierarchy extraction" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
