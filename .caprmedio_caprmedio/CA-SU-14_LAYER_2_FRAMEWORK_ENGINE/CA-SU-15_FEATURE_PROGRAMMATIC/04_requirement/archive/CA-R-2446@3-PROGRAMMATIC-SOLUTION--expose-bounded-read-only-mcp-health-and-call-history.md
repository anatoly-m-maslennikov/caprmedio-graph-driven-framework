---
identity:
  atom_id: CA-R-2446
  ref_id: CA-R-2446@3
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
  tier: 4
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 00:09:26 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-2446@3-PROGRAMMATIC-SOLUTION--expose-bounded-read-only-mcp-health-and-call-history.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
---
## Summary

Expose bounded, read-only MCP health and call history

## Claim scope

The existing MCP HTTP Gateway **and** its process-local diagnostic view, **without** replacing canonical execution history.

## Claim

MCP **must** expose a browser view at `/health` on the same listener. The view shows:

- bounded health observations;
- recent Tool calls;
- recent Workflow observations with status; **and**
- safe error details.

Preserve the current machine JSON `ready` boolean **and** readiness HTTP status semantics. The diagnostic view is non-authoritative. It **must not** infer successful Tool **or** Workflow execution from gateway liveness, scheduler completion, **or** absence of observations.

## Details

- Render the browser view for explicit `Accept: text/html`. Default, `application/json`, **and** `*/*` requests retain the existing machine representation. Preserve the existing loopback Host/Origin boundary; add no HTTP credential behavior.
- Observe actual Gateway calls **and** results **only**. Retain at most 32 recent Tool-call observations **and** at most 32 recent Workflow observations in process-local memory. Label since-start coverage **and** reset it on restart. This is **not** persistent, cross-process, **or** complete execution history.
- Tool observations identify the admitted Tool name, observation time, returned **or** observed outcome, **and** a fixed safe error category. Do **not** label an ordinary returned response as proof of completed domain effects. Preserve rejected, failed, partial, canceled, **and** uncertain outcomes **without** replay.
- Workflow observations use **only** known Run identities **and** actual call results. Keep `scheduler_status` separate from actual Workflow outcome **or** disposition; queued **or** pending is **not** successful completion. An unobserved actual outcome is unknown even **if** a scheduler reports `SUCCESS`.
- Show gateway generation/process availability **and** registry availability separately from provider-call observations **and** Workflow/worker observations. Last observations are historical facts, **not** live probes. Missing, stale, **or** untested state remains unknown **and** is **not** promoted to healthy.
- Retain **and** display none of: raw arguments, raw results, credentials, absolute paths, **or** provider exception text. Use fixed safe error categories with explanatory labels, including timeout, connection, returned-error, **and** uncertain **where** actually known. Escape **every** dynamic HTML field. Bounded history **must not** grow with arbitrary request sizes.
- A health GET reads the existing snapshot **only**. It does **none** of the following:
  - invoke a Tool **or** Workflow;
  - initialize DBOS/Docker state;
  - scan a Journal;
  - start, reload, **or** recover anything;
  - perform a mutation; **or**
  - replay an uncertain call **or** held Run.
- Keep canonical sources, Journals, **and** execution outcome evidence distinct from this convenience view.
