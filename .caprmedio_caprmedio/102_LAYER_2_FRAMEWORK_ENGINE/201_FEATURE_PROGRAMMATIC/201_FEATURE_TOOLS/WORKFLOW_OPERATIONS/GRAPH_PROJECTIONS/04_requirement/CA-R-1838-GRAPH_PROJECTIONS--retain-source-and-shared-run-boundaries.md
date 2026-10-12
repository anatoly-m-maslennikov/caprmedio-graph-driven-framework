---
atom_id: CA-R-1838
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Boundary"
  depends_on: [Tool, Workflow, Action, Projection, Artifact, Journal, Workflow Run, Step Run]
relations:
  relates_to: [CA-R-1835, CA-R-1836, CA-R-1837, CA-O-133, CA-O-136, CA-R-1720, CA-R-1728]
---
# Summary

Retain source and shared Run boundaries

## Scope

The boundary between graph projection construction, source authority, and accepted shared Run/Journal support.

## Claim

The builders **must** consume the selected Workflow/Step/Action bindings and shared Run/Journal receipts by reference, without creating a second Journal schema or treating a Projection as source authority.

## Details

Each attempt preserves requested graph kind, source frontier, source Atom/Claim/Project Structure identities and revisions, Workflow/Step/Action definition revisions, actual parent/Run references, admitted output destination if any, and exact effects. An admitted derived fact context is a source-bound input Projection, not another authority; its exact binding and ultimate source evidence are retained under CA-D-539 rather than replaced by a remembered or independently maintained interpretation.

The caller's serializable request is distinct from the trusted execution context. The shared executor supplies actual parent/Run bindings and confirmed Action-start recording context before Action effects. Caller-authored receipt strings or objects do not establish that context, and request unwrapping must preserve the executor's actual binding. An unresolved start record blocks construction. The builder consumes this context by reference and performs no direct Journal write; the shared recorder appends actual events once without rewriting existing Journal history or mutating source authority.

Terminal recording follows the actual effects. A construction result or confirmed start does not establish terminal recording or completed Action/Workflow execution. A terminal recording failure retains the produced output and exact effects, confirmed references and the shared pending/blocking reference, with truthful `recording_pending` or blocked completion. A recording-only recovery reconciles the same event identity and payload through shared support, preserving the original result and effects without replaying construction or publication. It creates no second Journal schema, invented Artifact mutation or new construction attempt.

Source correction, vocabulary admission, Relation-kind admission, scope declaration, retry, or regeneration is not authorized by an incomplete or failed build. A separately admitted retry retains the prior effects and recording state rather than erasing them.

Projection consumers, including GRAPH_SERVER and optional UI, are read-only consumers of derived output. No builder, consumer, or output may modify source authority to make a graph pass, use a Projection to establish missing source completeness, or silently substitute current files for the admitted frontier.

### Sources

- CA-O-133, CA-O-134, CA-O-136 and CA-O-137 at the exact revisions admitted for the work.
- CA-R-1387 v8; shared Run/Journal authority is referenced, not redefined.
