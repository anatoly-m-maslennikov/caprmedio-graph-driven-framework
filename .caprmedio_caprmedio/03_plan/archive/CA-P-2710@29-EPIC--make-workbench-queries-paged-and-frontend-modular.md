---
atom_id: CA-P-2710
label: Epic
status: Archived
tier: 3
version: 29
updated_at: 2026-11-05 18:50:42 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2710@29-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan/archive
---

## Summary

Make Workbench queries paged and the frontend modular

## Objective

Improve Workbench usability and saved queries/Worksheets according to the reviewed RMEDO.

## Scope

Workbench RMEDO, implementation, tests, documentation and local deployment. Unrelated Engine and methodology migrations remain outside this Epic.

## Completed work (0.4.4.19)

- [x] Update RMEDO for the approved Workbench changes.
- [x] Review the RMEDO against the latest Operator input and related Current sources; fix issues.
- [x] Adopt the reviewed RMEDO.
- [x] Compile applicable PROGRAMMATIC Method Policies into one implementation prompt.
- [x] Implement the adopted RMEDO using that prompt.
- [x] Update callers, tests, fixtures and documentation.
- [x] Replace duplicate implementation-level checks with behavior-focused end-to-end tests.
- [x] Run the relevant tests and frontend checks; fix failures.
- [x] Perform local release.
- [x] Verify the released Workbench in the browser and through MCP.
- [x] Record completion.

## Tasks

- [x] Update and review RMEDO for the requested Workbench refinements.
- [x] Implement the reviewed RMEDO.
- [x] Update behavior-focused tests and run the relevant checks.
- [x] Release locally and verify the deployed result.
- [x] Record completion.

## Sources

Design is in CA-R-2727, CA-R-2728, CA-R-2729, CA-R-2763, CA-R-2776, CA-M-468, CA-M-469, CA-M-470, CA-M-472, CA-D-673, CA-D-674, CA-E-676, CA-E-678 and CA-O-240.

## Previous verification

Done. Workbench 0.4.4.19 is deployed at `http://127.0.0.1:56317/caprmedio/workbench/caprmedio`. Its eight MCP operations and live command-palette Ctrl+P/Ctrl+N navigation were verified.

Verification:

- Local release: 45 selected tests and all launcher integration groups passed.
- After test refinement: 72 Workbench host tests and 3 remaining frontend state-boundary tests passed; TypeScript and Vite build passed.
- One-container MCP/HTTP/watcher/browser suite: 4 tests passed in 79 seconds. Its browser check executes 3 real user flows; no backend mocks or extra server container.
- Retired 11 duplicate or implementation-coupled unit tests. Focused checks for uncovered behavior remain.
- No source Atom was changed by query execution; no container out-of-memory kill occurred.

Receipts: `.caprmedio_runtime/simple_local_release/reports/workbench-20261105-compact-journal-final.md`, `.caprmedio_tmp/workbench/compact-names/live-proof.json` and `.caprmedio_tmp/workbench/compact-names/docker-browser-verified.log`.

The final test refinement changes test/development files and its RMED, not deployed application behavior. The full repository suite was not rerun for this Workbench-only iteration. Unrelated methodology and Engine work remains outside this Epic.

## Last deployment

Workbench 0.4.4.21 is deployed at `http://127.0.0.1:56317/caprmedio/workbench/caprmedio`.

Open Saved is available only in the command palette; the standalone toolbar button and dedicated shortcut are removed. Its ID/URL modal still opens with input focused. Result headers show actual column names and SQL types on separate lines, with types smaller and muted. The SQL schema is unchanged.

The standard local release completed. All 4 selected Docker/API/watcher/browser tests and all launcher groups passed, including the 3 real browser flows. Frontend state tests, TypeScript and Vite build passed. The live browser confirmed `id` and `status_group` are separated from `VARCHAR`, palette-only opening works, and the verification query created no saved entry.

Receipt: `.caprmedio_runtime/simple_local_release/reports/workbench-20261105-palette-column-headers.md`.
Test log: `.caprmedio_tmp/simple_local_release/workbench-20261105-palette-column-headers-tests-a2mf46jn.log`.
Adoption, method prompt and live proof: `.caprmedio_tmp/workbench/palette-headers/`.

The previous header, explicit-save and browser autosave behavior remains verified. Earlier iteration details are retained in archived Epic versions. The full repository suite was not rerun for this UI-only refinement.


## Audit follow-up tasks

- [x] Review Workbench implementation traces, architecture, leftovers and watcher coverage.
- [x] Prepare a Spec Proposal for PROGRAMMATIC Policies, the implementation prompt and workflow.
- [x] Record the Operator decision on invalid Scope Unit Declaration handling in CA-A-1322.
- [x] Record the Operator decision on transient query-result retention.
- [x] Prepare, review and adopt RMED for the requested MCP service operation.
- [x] Implement the adopted MCP service operation and its behavior checks.
- [x] Prepare, review and adopt RMED for the requested health-page control.
- [x] Implement the approved health-page control and its behavior checks.
- [ ] Implement the approved result-retention behavior.
- [ ] Review and adopt the general PROGRAMMATIC Policy proposals in CA-A-1322.
- [ ] Fix confirmed Workbench defects and the selected trace and performance issues.
- [ ] Add the missing real lifecycle and browser behavior checks.
- [ ] Run the affected checks and independent review; fix remaining issues.
- [ ] Perform local release and verify the deployed result.
- [ ] Record completion and close the Epic.

## Current status

Active. Local release 0.4.4.23 completed. All 42 selected tests and all launcher integration groups passed. A fresh native MCP client verified the running query parameters, an existing Workspace/View, metadata-only Run, paged fetch, preserved focus and matching discovery catalog. Native plugin installation and hook trust are still pending. The watcher change-log RMED is adopted and implementation is in progress. The requested sync indicator and UI refinements are being prepared in RMED. Other audit and general Policy tasks remain open.

Design and review findings: CA-A-1322, `../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/02_analysis/draft/CA-A-1322@1-draft-PROGRAMMATIC-SPECIFICATION_PROPOSAL--simplify-programmatic-implementation-policies-and-workflow.md`.

Verification of service restart: `.caprmedio_tmp/workbench/service-restart/verification.json`. No new generic service registry, container controls, automatic recovery, browser-crash handling or MCP Release result operation were added.


## MCP query and discovery refinement tasks

- [x] Prepare, review and adopt the requested RMEDO refinements.
- [x] Implement the adopted query operations and update their callers.
- [x] Implement the adopted root discovery catalog and its release integration.
- [x] Update and run the relevant native SQL, MCP/HTTP, frontend and release checks.
- [ ] Review the completed changes and fix confirmed issues.
- [ ] Perform local release and verify the installed result.

Design is recorded in CA-A-1323 and its RMED index. This adds MCP catalog generation and its local-release hook to scope. Existing unrelated methodology/Engine migrations remain excluded. General Policy adoption and result-retention implementation remain separate pending tasks.


## MCP Project context and full-reread tasks

- [x] Prepare, review and adopt the Project-context RMED.
- [x] Reuse and verify the compiled PROGRAMMATIC M Policy prompt.
- [x] Implement the adopted Project-context contract.
- [x] Prepare, review and adopt RMED for full reread.
- [x] Implement the adopted full-reread contract and its interface controls.
- [x] Run the affected real MCP, HTTP and database checks.
- [ ] Review and fix the completed implementation.
- [ ] Release locally and verify both capabilities.

## Standalone chat — deferred

- [x] Prepare, review and adopt the initial standalone chat sources.
- [x] Preserve the unfinished standalone implementation and review findings.
- [x] Disable the standalone chat pane, bridge route and release startup.
- Remaining standalone chat implementation, lifecycle repairs, tests and deployment are deferred by the Operator. They are not acceptance gates for the Codex extension.

## Codex extension tasks

- [x] Declare CODEX_EXTENSION within WORKBENCH.
- [x] Prepare RMEDO for the embedded Workbench and Workspace/View controls.
- [x] Review against the latest Operator decisions and related RMEDO; fix issues.
- [x] Adopt the reviewed sources.
- [x] Reuse the applicable PROGRAMMATIC M Policy prompt and gather implementation sources.
- [x] Implement the adopted sources, reusing existing query execution, pagination and saving.
- [x] Add real MCP/HTTP and interface behavior checks; review and fix issues.
- [ ] Release locally and verify the embedded Workbench.

The extension uses the existing Codex chat, with one Workspace per chat and at least one View. Workspace/View behavior and extension delivery belong in RMEDO, not in task design. The requested operations include listing Workspaces; creating a View first/last; listing, updating, running, fetching paged results, focusing, renaming, removing and saving Views. Standalone chat remains disabled and deferred. Existing unrelated audit tasks remain open.

Project context and full reread have passed focused source checks. The tested image is now running; the automated release caller and catalog completion remain separate from that runtime verification.


Extension source index and review: `.caprmedio_tmp/workbench/codex-extension/adoption.json` and `review.md`. Design is in R2901–R2903, R2792–R2793, M476 and D681; E684 covers observable acceptance. Source conflicts found during review were corrected.


## Reported defect tasks

- [x] Check and correct the role-only Draft indexing defect.
- [x] Check and correct unreachable cached results after failed first-page delivery.
- [x] Correct recoverable query-error diagnostics and retain runtime-failure severity.
- [x] Verify the old deployed query schema and add a real MCP regression for current parameters.
- [x] Correct the new Scope Unit Declaration carrier and recheck source loading.
- [x] Fix browser integration failures and rerun the affected flows.
- [x] Activate the tested implementation and verify the current query parameters in the running MCP.

The decisions for the reported defects are recorded in M462, M463 and M465. Building or testing source does not update the running container.


## Reported Problems and regression Evaluations

- [x] Record the four reported defects as Problems and link reusable regression Evaluations.
- [x] Resolve the three verified source defects.
- [x] Verify the deployed query boundary and resolve CA-C-703.

CA-C-700, CA-C-701, CA-C-702 and CA-C-703 are Resolved. CA-E-750, CA-E-751, CA-E-752 and CA-E-753 remain Active regression cases, linked through evaluation_for. Carrier paths and statuses are indexed in `.caprmedio_tmp/workbench/codex-extension/problems.json`. No deployed success is inferred from source tests.


## Release completion follow-up

- [x] Verify the tested image through a fresh native MCP client.
- [x] Correct the local-release startup caller and its catalog environment.
- [x] Complete independent review and the corrected local release.
- [x] Verify the released catalog and the running interface.
- [ ] Install the local Codex plugin and trust its hook in the desktop app.

The earlier automated release stopped at startup. The existing Project bootstrap restored the tested image; the corrected standard release then completed with 0.4.4.23. A native client verified 42 tool descriptors, `preview: 0, save: false`, Workspace/View creation, SQL update, metadata-only Run, paged fetch and focus. This does not claim a successful automatic release receipt or a native plugin installation. Evidence: `.caprmedio_tmp/workbench/codex-extension/live-proof.json`.

## Watcher change-log tasks

- [x] Prepare RMED Drafts for the requested watcher change log.
- [ ] Review the Drafts against the Operator input and existing watcher; resolve open decisions.
- [x] Adopt the reviewed RMED.
- [ ] Reuse the implementation prompt and implement the adopted RMED.
- [ ] Add and run end-to-end checks for the adopted behavior.
- [ ] Review and fix the changes.
- [ ] Release locally and verify the result.

Draft source index: CA-R-2950, CA-M-490, CA-D-695, CA-E-780 and CA-R-2724. The packet and open decisions are tracked in `.caprmedio_tmp/workbench/watcher-change-log/drafts.json`. The reviewed watcher sources are Current contracts; implementation remains in progress. The adoption index is `.caprmedio_tmp/workbench/watcher-change-log/adoption.json`.


## Sync indicator and interface refinement tasks

- [ ] Prepare and review RMED for the requested interface refinements.
- [ ] Adopt the reviewed RMED.
- [ ] Reuse the implementation prompt and implement the adopted RMED.
- [ ] Add and run browser and MCP/HTTP behavior checks.
- [ ] Review and fix the changes.
- [ ] Release locally and verify the result.

Design and source tracking: `.caprmedio_tmp/workbench/sync-status/drafts.json`. The latest Operator decisions are the authority for these refinements; task entries do not define the design.

## Latest release evidence

Standard release receipt: `.caprmedio_runtime/simple_local_release/reports/workbench-20261105-codex-extension-3.md`.
Live MCP proof: `.caprmedio_tmp/workbench/codex-extension/live-release-23.json`.
The catalog contains the same 42 tool names as native MCP. Workspace/View result verification returned20rows and4columns, fetched5rows and preserved focus. No plugin installation or new change-log deployment is inferred from this check.
