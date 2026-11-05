---
atom_id: CA-P-2710
label: Epic
status: Archived
tier: 3
version: 31
updated_at: 2026-11-05 20:27:36 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2710@31-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan/archive
---

## Summary

Make Workbench queries paged and the frontend modular

## Objective

Improve Workbench queries, Views and the read-only result grid according to the reviewed RMEDO.

## Scope

Workbench RMEDO, implementation, tests, documentation and local deployment. Unrelated Engine and methodology migrations remain outside this Epic. Design belongs in RMED, not in task descriptions.

## Completed work

- [x] Implement and release the shared paged SQL backend, Svelte frontend and saved-item Journal.
- [x] Implement and verify MCP query/discovery, Project context and full reread.
- [x] Declare CODEX_EXTENSION and implement Workspace/View controls and the plugin package.
- [x] Fix the four reported defects, record Resolved Problems C700–C703 and retain linked regression Evaluations E750–E753.
- [x] Correct the local-release startup caller and complete local release 0.4.4.23.
- [x] Prepare, review and adopt watcher change-log and initial sync/interface RMED.
- [x] Implement the watcher, change log, nonblocking status, initial interface refinements and ordinary-file disappearance fix in source.

## Current implementation cycle

- [ ] Create remaining RMED for the requested Workbench changes.
- [ ] Review against the latest Operator input and related Current sources; fix contradictions and gaps.
- [ ] Adopt the reviewed RMED.
- [ ] Gather or reuse applicable Method Policies from PROGRAMMATIC through each target Scope Unit and compile one implementation prompt for that Scope Unit.
- [ ] Gather the adopted Requirements, Evaluations, Delivery and non-Policy Methods for each implementation scope.
- [ ] Implement those sources and reconcile callers, fixtures, configuration and documentation.
- [ ] Implement and run behavior-focused end-to-end tests.
- [ ] Review and fix the integrated changes.
- [ ] Perform local release and verify the running MCP and browser behavior.
- [ ] Record verified completion.

The reviewed source packets cover the result grid, display settings, unified Views, transient result retention and hourly query-log batches. Query-log retention is now two days, following the latest Operator decision. Temporary result retention follows its separate Workbench contract.

## Scoped lanes

| Scope Unit | Owner responsibility |
| --- | --- |
| WORKBENCH | Shared capability RMED and integrated acceptance. |
| WORKBENCH_BACKEND | Backend RMED, database, watcher, result pages and lifecycle. |
| WORKBENCH_FRONTEND | Frontend RMED, interface, result grid and browser checks. |
| CODEX_EXTENSION | Native integration and unified Workspace/View delivery sources. |

Each subagent works within one Scope Unit. The main agent owns adoption, transport integration, shared-state changes, Git and release. Ready independent lanes may run in parallel. Drafts, tests and deployed runtime are distinct outcomes.

## Other open tasks

- [ ] Review and adopt the general PROGRAMMATIC Policy proposals in CA-A-1322.
- [ ] Finish the remaining confirmed Workbench audit and trace issues recorded there.
- [ ] Install the local Codex plugin and trust its SessionStart hook in the desktop app.
- [ ] Review final Epic acceptance before closing it.

## Deferred

Standalone chat is disabled. Its remaining implementation, lifecycle repairs, tests and deployment stay deferred by the Operator and do not block the embedded Workbench.

## Current status

Active. Version 0.4.4.23 is the last deployed version. The watcher, sync and initial UI changes are implemented in source but not yet released. The remaining grid, unified View, retention and hourly query-log sources are being reviewed before implementation. Existing invalid Scope Unit Declarations still stop indexing; an ordinary file disappearing before admission is skipped. No unrelated source migration is included.

## Source and verification index

- General Policy proposal: CA-A-1322.
- MCP/discovery proposal: CA-A-1323.
- Source packets and adoption records: `.caprmedio_tmp/workbench/watcher-change-log/`, `sync-status/`, `grid-workbench/`, `result-display/`, `grid-backend/`, `unified-views/` and `result-retention/`.
- Per-scope Policy prompts and implementation source indices: `.caprmedio_tmp/workbench/scoped-implementation/`.
- Last standard release: `.caprmedio_runtime/simple_local_release/reports/workbench-20261105-codex-extension-3.md`.
- Last live native MCP proof: `.caprmedio_tmp/workbench/codex-extension/live-release-23.json`.

The last release passed 42 selected tests and all launcher integration groups. A fresh native MCP client verified the same 42 catalog/tool names, current query parameters, metadata-only View Run, paged fetch and focus. The native plugin is not installed or trusted. Earlier release details remain in archived Epic versions.
