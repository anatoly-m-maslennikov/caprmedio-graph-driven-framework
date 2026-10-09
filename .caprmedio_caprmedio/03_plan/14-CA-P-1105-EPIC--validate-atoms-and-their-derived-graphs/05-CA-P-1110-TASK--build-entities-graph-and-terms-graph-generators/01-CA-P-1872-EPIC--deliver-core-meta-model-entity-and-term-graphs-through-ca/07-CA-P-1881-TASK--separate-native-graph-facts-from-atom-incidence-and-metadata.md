---
atom_id: CA-P-1881
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
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
    - CA-P-1882
    - CA-P-1883
    - CA-P-1884
---
# Summary

Separate native graph facts from Atom incidence and metadata

## Objective

Separate native facts from Atom incidence and metadata.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1876; existing attribution code.

Required Plan prerequisites: [CA-P-1876](04-CA-P-1876-TASK--record-graph-qualified-relation-and-property-ownership-contracts.md), [CA-P-1879](06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage/01-CA-P-1879-TASK--implement-current-term-hierarchy-extraction.md).

Output: Separate native facts from Atom incidence and metadata with source-backed evidence retained in this Task's work record.

Acceptance check: No spelling-based joins or promoted Subject dependencies; source metadata is not relabeled as Entity Properties.

Exclusive edit/effect scope: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/ native fact/incidence/metadata attribution and its focused fixtures only.

Source Atom author/content_role and other Carrier metadata stay on that source owner. Governing an Entity does not make this metadata the Entity's Properties. Native Property facts need admitted owner/value/source evidence. Do not invent native Term edges from spelling joins or Subject dependencies.

Inherit the main Epic's boundaries and the Operator's explicit 90% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Separate native facts from Atom incidence and metadata" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
