---
atom_id: CA-R-2007@9
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/UX/MCP Health and Diagnostic View
  depends_on: []
relations:
  depends_on:
  - CA-R-1884
  - CA-R-1885
  - CA-R-1848
tier: 4
type: Goal
---
# Summary

Expose bounded read-only MCP health and call history

## Scope

The existing MCP HTTP Gateway and its process-local diagnostic view, without replacing canonical execution history.

## Claim

MCP must expose a same-listener /health browser view of bounded health observations, recent Tool calls, recent Workflow observations with status, and safe error details. Preserve the current machine JSON ready boolean and readiness HTTP status semantics. The diagnostic view is non-authoritative and must never infer successful Tool or Workflow execution from gateway liveness, scheduler completion or absence of observations.

## Details

- For explicit Accept: text/html, render the browser view. Default, application/json and */* requests retain the existing machine representation. Preserve the existing loopback Host/Origin boundary; no HTTP credential behavior is added.
- Observe actual Gateway calls/results only. Retain at most 32 recent Tool-call observations and at most 32 recent Workflow observations in process-local memory. Label since-start coverage and reset on restart; this is not persistent, cross-process or complete execution history.
- Tool observations identify the admitted Tool name, observation time, returned/observed outcome and a fixed safe error category. Do not label an ordinary returned response as proof of completed domain effects. Preserve rejected, failed, partial, canceled and uncertain outcomes without replay.
- Workflow observations use only known Run identities and actual call results. Keep scheduler_status separate from actual Workflow outcome/disposition; queued or pending is not successful completion. An unobserved actual outcome is unknown even if a scheduler reports SUCCESS.
- Show gateway generation/process availability and registry availability separately from provider-call observations and Workflow/worker observations. Last observations are historical facts, not live probes; missing, stale or untested state remains unknown and is not promoted to healthy.
- Retain/display no raw arguments, raw results, credentials, absolute paths or provider exception text. Use fixed safe error categories with explanatory labels, including timeout/connection/returned-error/uncertain where actually known. Escape every dynamic HTML field; bounded history must not grow with arbitrary request sizes.
- A health GET reads the existing snapshot only. It invokes no Tool or Workflow, initializes no DBOS/Docker state, scans no Journal, starts/reloads/recovers nothing, performs no mutation and replays no uncertain call or held Run. Keep canonical sources, Journals and execution outcome evidence distinct from this convenience view.
