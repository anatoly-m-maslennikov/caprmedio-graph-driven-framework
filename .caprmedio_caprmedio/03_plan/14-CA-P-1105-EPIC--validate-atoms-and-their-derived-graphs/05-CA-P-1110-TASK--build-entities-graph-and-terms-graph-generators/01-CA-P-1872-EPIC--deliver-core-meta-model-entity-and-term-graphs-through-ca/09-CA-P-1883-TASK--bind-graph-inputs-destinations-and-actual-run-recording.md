---
atom_id: CA-P-1883
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
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
    - CA-P-1884
    - CA-P-1888
---
# Summary

Bind graph inputs destinations and actual Run recording

## Objective

Bind inputs, destinations and actual Run recording.

## Details

Assignee: AI Agent, as carried above. Estimated own work: 15 minutes.

Inputs: CA-P-1877–CA-P-1882; admitted route schema.

Required Plan prerequisites: [CA-P-1877](05-CA-P-1877-TASK--implement-current-source-backed-definition-recognition.md), [CA-P-1878](06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage.md), [CA-P-1881](07-CA-P-1881-TASK--separate-native-graph-facts-from-atom-incidence-and-metadata.md), [CA-P-1882](08-CA-P-1882-TASK--prepare-the-explicit-owned-core-source-selection.md).

Output: Bind inputs, destinations and actual Run recording with source-backed evidence retained in this Task's work record.

Acceptance check: Correct request shape, separate admitted destinations and executor-supplied recording context.

Exclusive edit/effect scope: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/ request/destination/recording adapter and directly related graph-route tests. Read 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py; a shared executor edit needs a separately bounded admitted Task.

Use two distinct admitted JSON destinations under the configured projection root. Do not overwrite another Run/global graph. Preserve outer executor-supplied recording context; nested graph_request must not drop it or replace it with caller claims.

Inherit the main Epic's boundaries and CA-P-1110's 99% confidence threshold/retry rules. If the current work will exceed 15 minutes, split it into bounded admitted children before execution. Shared graph/fixture edits must be serialized or held by one integration owner. New required defects need separately bounded fix Tasks, not an unbounded review-and-fix loop.

### Definition of Done

the Plan is **not** Done **if** ((the source-backed output for "Bind inputs, destinations and actual Run recording" **or** required evidence is missing) **or** (the stated acceptance check is failed, blocked, stale, conflicting **or** incomplete) **or** (work exceeds the admitted boundary **or** required source/runtime admission is unavailable) **or** (a required effect **or** execution receipt remains uncertain **or** recording-pending) **or** (any direct decomposing Plan is **not** Done)).
