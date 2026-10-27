---
atom_id: CA-M-400
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Failure Handling
  depends_on: []
relations:
  child_of:
  - CA-M-403
tier: 2
---
# Summary

Apply one shared public-operation error boundary

## Scope

PROGRAMMATIC public operation and process execution boundaries, including all first-party Tools, Workflows, Apps, MCP adapters, service entrypoints and background executors shipped in a delivered Docker image. The policy is not limited to AtomSearch, MCP-mediated invocation or a currently running container.

## Claim

Reuse one transport-neutral error-handling owner at public operation boundaries, applying it through a decorator or equivalent shared wrapper rather than duplicating exception classification and logging across Tools, MCP and other callers.

## Details

1. The shared boundary classifies known failures, emits the technical diagnostic under CA-M-396/397/399, and uses the caller's declared result/error adapter. It does not invent a competing domain model or force different existing public contracts into an undocumented universal envelope.
2. Support synchronous and asynchronous operations while preserving their callable signature/metadata, await behavior and cancellation. Do not turn cancellation, process shutdown or an interrupt into successful output.
3. The operation owner supplies verified completed data, effects and error context under CA-M-398. Pass already-structured partial or failed outcomes through without erasing their data, duplicating diagnostics or reclassifying a Project artifact as runtime failure.
4. Use explicit failure classification and actual context rather than treating a Python exception base class, including RuntimeError, as proof that the runtime is broken. An unexpected failure must remain visible; never silently return success.
5. Apply the boundary once at the relevant public execution owner, not around every helper. Registration and discovery remain effect-free. Generic handling does not start Workflows, append Journals, retry, repair, roll back or replay business work.
6. Reuse the established shared logger and canonical execution/validation owners. Keep transport-specific response encoding in its adapter and business lifecycle recording with the Workflow executor.
7. Derive the affected runtime coverage from the delivered image entrypoints, executable modes and their actual dispatch owners. Wire the shared handling at those owners so direct invocation, worker execution and service execution do not bypass it. Reuse existing package inventories; do not introduce a competing runtime registry, decorate every helper or modify third-party internals. A verified process-startup/runtime failure may terminate the affected process; a failed request or business Workflow does not imply that the runtime is broken.
