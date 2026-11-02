---
atom_id: CA-R-2434@1
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: 2026-10-29 23:57:07 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
  depends_on: []
relations: {}
tier: 4
type: Goal
---
## Summary

MCP exposes bounded, read-only, non-authoritative health and call observations

## Claim scope

the existing MCP HTTP Gateway **and** its process-local diagnostic view, **without** replacing canonical execution history.

## Claim

MCP **must** expose a browser view at `/health` on the same listener, showing bounded health observations, recent Tool calls, recent Workflow observations with status, **and** safe error details. MCP **must** preserve the current machine JSON `ready` boolean **and** readiness HTTP status semantics.

the diagnostic view is non-authoritative. MCP **must not** infer successful Tool **or** Workflow execution from **any** of:

- Gateway liveness;
- scheduler completion; **or**
- absence of observations.

## Details

- render the browser view for explicit `Accept: text/html`. default, `application/json`, **and** `*/*` requests retain the existing machine representation. preserve the existing loopback Host/Origin boundary; add no HTTP credential behavior.
- observe actual Gateway calls **and** results **only**. retain at most 32 recent Tool-call observations **and** at most 32 recent Workflow observations **in** process-local memory. label since-start coverage **and** reset it on restart; the view is **not** persistent, cross-process, **or** complete execution history.
- for each Tool observation, identify the admitted Tool name, observation time, returned **or** observed outcome, **and** a fixed safe error category. do **not** label an ordinary returned response as proof of completed domain effects. preserve rejected, failed, partial, canceled, **and** uncertain outcomes **without** replay.
- use only known Run identities **and** actual call results for Workflow observations. keep `scheduler_status` separate from actual Workflow outcome **or** disposition; queued **or** pending is **not** successful completion. an unobserved actual outcome remains unknown even **if** a scheduler reports `SUCCESS`.
- show gateway generation/process availability **and** registry availability separately from provider-call observations **and** Workflow/worker observations. last observations are historical facts, **not** live probes; missing, stale, **or** untested state remains unknown **and** is **not** promoted to healthy.
- retain **and** display none of: raw arguments, raw results, credentials, absolute paths, **or** provider exception text. use fixed safe error categories with explanatory labels, including timeout, connection, returned-error, **and** uncertain **when** actually known. escape **every** dynamic HTML field; bounded history **must not** grow with arbitrary request sizes.
- a health GET reads the existing snapshot **only**. it invokes no Tool **or** Workflow, initializes no DBOS/Docker state, scans no Journal, starts, reloads **or** recovers nothing, performs no mutation, **and** replays no uncertain call **or** held Run. keep canonical sources, Journals, **and** execution outcome evidence distinct from this convenience view.
