---
atom_id: CA-P-2710
label: Epic
status: Active
tier: 3
version: 12
updated_at: 2026-11-05 00:47:18 +0400
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
    path: .caprmedio_caprmedio/03_plan
---

## Summary

Make Workbench queries paged and the frontend modular

## Objective

Improve Workbench usability and saved queries/Worksheets according to the reviewed RMEDO.

## Scope

Workbench RMEDO, implementation, tests, documentation and local deployment. Unrelated Engine and methodology migrations remain outside this Epic.

## Tasks

- [ ] Update RMEDO for the approved Workbench changes.
- [ ] Review the RMEDO against the latest Operator input and related Current sources; fix issues.
- [ ] Adopt the reviewed RMEDO.
- [ ] Compile applicable PROGRAMMATIC Method Policies into one implementation prompt.
- [ ] Implement the adopted RMEDO using that prompt.
- [ ] Update callers, tests, fixtures and documentation.
- [ ] Run the relevant tests and frontend checks; fix failures.
- [ ] Perform local release.
- [ ] Verify the released Workbench in the browser and through MCP.
- [ ] Record completion.

## Sources

Design belongs in RMEDO, not in these Tasks. The current change packet updates CA-R-2727, CA-R-2728, CA-R-2763, CA-R-2776, CA-M-469, CA-M-470, CA-D-673, CA-D-674, CA-E-676, CA-E-678 and CA-O-240. Draft tracking: `.caprmedio_tmp/workbench/compact-names/drafts.json`.

## Status

Active. Workbench 0.4.4.18 is the verified released baseline. The new RMEDO packet is being prepared for review; this iteration has not been implemented or released.

Earlier completed work and verification remain in the archived versions of this Epic.
