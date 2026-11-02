---
atom_id: CA-D-537@4
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 23:34:06 +0400
subjects:
  governs: Tool/WORKFLOW_OPERATIONS/REVERT_CHANGES/Delivery
  depends_on:
  - Tool
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/History/Journal
  - Implementation
relations:
  delivery_for:
  - CA-R-1834
  - CA-E-553
  - CA-E-636
type: Eng Decision
---
# Summary

Bind REVERT_CHANGES delivery boundaries

## Scope

The delivery boundary between REVERT_CHANGES, governed reversal capabilities, and shared Run/Journal support.

## Claim

REVERT_CHANGES **must** deliver manifest validation, currentness guards, ordered effect orchestration, and truthful result assembly, while delegated governed effects and shared Journal serialization retain their existing authority.

## Details

Implementation belongs at the CA-D-536 entrypoint with functional mocks under the same Tool package. It calls supported governed effect capabilities only after admission/currentness checks; it never replaces CA-O-131's semantics, deletes history, performs a Git reset, or implements an internal failure rollback. It passes exact Run/Step/Action identity and evidence references to existing shared Run support and retains actual Run observations and logging diagnostics. Plain Journal append/read is independent observation, not a permission or source-effect completion gate; no durable/pending receipt, logging retry or recovery channel is required or exposed. Actual Run-start failure blocks before effects, and actual Run-terminal failure preserves observed effects and reports its error without claiming terminal persistence. Logging failure does not downgrade an independently completed reversal or authorize effect replay.

Delivery is incomplete until CA-E-553 and CA-E-636 run through the real MCP boundary in the required Docker image. This RMED carrier authorizes no code before independent RMED review and no runtime-success claim.
