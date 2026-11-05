---
atom_id: CA-P-2710
label: Epic
status: Archived
tier: 3
version: 23
updated_at: 2026-11-05 13:49:57 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2710@23-EPIC--make-workbench-queries-paged-and-frontend-modular.md
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

Active. The previous Workbench 0.4.4.21 release remains recorded above. The new audit and proposal are complete; their implementation and validation remain pending. Invalid Scope Unit Declarations retain the stricter stop-and-restart behavior, as confirmed by the Operator. Query-result retention follows the confirmed Worksheet lifetime. MCP and health-page service restart contracts and source implementation are complete. Focused real MCP/lifecycle and HTTP checks and independent code review passed. The running container remains at the previous release; deployment of this change is pending. Other audit fixes, general Policy adoption and query-result retention implementation remain pending.

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
- [ ] Implement the adopted Project-context contract.
- [ ] Prepare, review and adopt RMED for full reread.
- [ ] Implement the adopted full-reread contract and its interface controls.
- [ ] Run the affected real MCP, HTTP and database checks.
- [ ] Review and fix the completed implementation.
- [ ] Release locally and verify both capabilities.

## Codex integration tasks

- [x] Prepare the WORKBENCH_CODEX Scope Unit Declaration Draft.
- [ ] Review and adopt the Scope Unit Declaration.
- [ ] Prepare, review and adopt Codex integration RMED.
- [ ] Compile or reuse applicable M Policies and gather implementation sources.
- [ ] Implement the reviewed RMED.
- [ ] Run meaningful integration and interface checks; review and fix issues.
- [ ] Release locally and verify the integrated chat.

Project-context sources and the compiled prompt are indexed in `.caprmedio_tmp/mcp-project-context/`. Codex scope is proposed in CA-R-2790. The Epic remains Active; source implementation and release are separate outcomes.
