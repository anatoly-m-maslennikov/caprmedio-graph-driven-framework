---
atom_id: CA-P-2710
label: Epic
status: Done
tier: 3
version: 13
updated_at: 2026-11-05 02:50:12 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan/done
---

## Summary

Make Workbench queries paged and the frontend modular

## Objective

Improve Workbench usability and saved queries/Worksheets according to the reviewed RMEDO.

## Scope

Workbench RMEDO, implementation, tests, documentation and local deployment. Unrelated Engine and methodology migrations remain outside this Epic.

## Tasks

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

## Sources

Design is in CA-R-2727, CA-R-2728, CA-R-2729, CA-R-2763, CA-R-2776, CA-M-468, CA-M-469, CA-M-470, CA-M-472, CA-D-673, CA-D-674, CA-E-676, CA-E-678 and CA-O-240.

## Status

Done. Workbench 0.4.4.19 is deployed at `http://127.0.0.1:56317/caprmedio/workbench/caprmedio`. Its eight MCP operations and live command-palette Ctrl+P/Ctrl+N navigation were verified.

Verification:

- Local release: 45 selected tests and all launcher integration groups passed.
- After test refinement: 72 Workbench host tests and 3 remaining frontend state-boundary tests passed; TypeScript and Vite build passed.
- One-container MCP/HTTP/watcher/browser suite: 4 tests passed in 79 seconds. Its browser check executes 3 real user flows; no backend mocks or extra server container.
- Retired 11 duplicate or implementation-coupled unit tests. Focused checks for uncovered behavior remain.
- No source Atom was changed by query execution; no container out-of-memory kill occurred.

Receipts: `.caprmedio_runtime/simple_local_release/reports/workbench-20261105-compact-journal-final.md`, `.caprmedio_tmp/workbench/compact-names/live-proof.json` and `.caprmedio_tmp/workbench/compact-names/docker-browser-verified.log`.

The final test refinement changes test/development files and its RMED, not deployed application behavior. The full repository suite was not rerun for this Workbench-only iteration. Unrelated methodology and Engine work remains outside this Epic.
