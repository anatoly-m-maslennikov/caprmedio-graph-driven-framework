---
atom_id: CA-M-400
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-21T18:40:43Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  child_of: [CA-M-387]
  relates_to: [CA-M-396, CA-M-397, CA-M-398, CA-M-399]
---
# Summary

Apply one shared public-operation error boundary

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Reuse one transport-neutral error-handling owner at public operation boundaries, applying it through a decorator or equivalent shared wrapper rather than duplicating exception classification and logging across Tools, MCP and other callers.

## Details

1. The shared boundary classifies known failures, emits the technical diagnostic under CA-M-396/397/399, and uses the caller's declared result/error adapter. It does not invent a competing domain model or force different existing public contracts into an undocumented universal envelope.
2. Support synchronous and asynchronous operations while preserving their callable signature/metadata, await behavior and cancellation. Do not turn cancellation, process shutdown or an interrupt into successful output.
3. The operation owner supplies verified completed data, effects and error context under CA-M-398. Pass already-structured partial or failed outcomes through without erasing their data, duplicating diagnostics or reclassifying a Project artifact as runtime failure.
4. Use explicit failure classification and actual context rather than treating a Python exception base class, including RuntimeError, as proof that the runtime is broken. An unexpected failure must remain visible; never silently return success.
5. Apply the boundary once at the relevant public execution owner, not around every helper. Registration and discovery remain effect-free. Generic handling does not start Workflows, append Journals, retry, repair, roll back or replay business work.
6. Reuse the established shared logger and canonical execution/validation owners. Keep transport-specific response encoding in its adapter and business lifecycle recording with the Workflow executor.
