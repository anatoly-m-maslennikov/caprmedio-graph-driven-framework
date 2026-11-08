---
atom_id: CA-E-794
ref_id: CA-E-794@2
container:
  scope_unit: CA-SU-43
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  is_evaluation_for:
  - CA-R-2723
  - CA-R-2725
  - CA-M-500
status: Archived
version: 2
updated_at: 2026-11-07 15:22:11 +0400
carrier_destination:
  file:
    name: CA-E-794@2-WORKBENCH-EVAL_CASE--verify-workbench-on-the-current-project-with-a-temporary-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archived
author: Anatoly Maslennikov
---

## Summary

Verify Workbench on the current Project with a temporary Scope Unit.

## Claim scope

An explicitly selected live Project and its running Workbench backend.

## Claim

### Prose Claim

Run a canary against the current Project, in addition to disposable-fixture E2E tests:

- Record the selected Project, backend version and measured visibility timings for every operation.
- Create an isolated, uniquely named temporary Scope Unit tree with its Declarations and test Atoms.
- Exercise create, update, rename, move and delete for the temporary Atoms, checking query-visible identity, Version, container Scope Unit ID, Scope Unit name, destination filename and destination path after each operation.
- Exercise create, update, rename, move and delete for temporary Scope Units, including updates to their actual Declarations and authority folders. Keep each published Declaration state valid; a Scope rename or move may replace its Declaration while natively moving its owned folder. Record these distinct events honestly.
- Keep a child Atom through its Scope Unit move and rename. Update its carrier metadata with the operation, then check the exact indexed values. The Scope Unit ID stays stable; its name and the child Atom destination change as applicable.
- Query Workbench after each operation to verify the expected Scope Unit structure and source rows.
- Remove the temporary Scope Units, their Declarations and test carriers.
- Query Workbench until those temporary rows are absent.

Use the real source readers, watcher and query interface. Do not substitute mocked data or a copied Project for this canary. Check the complete temporary Declaration before placing it in the watched tree. Remove only artifacts created by this run, including on failure, and report any cleanup that could not complete. Preserve unrelated files and concurrent work.

If any operation fails, stop the canary and clean up only its own artifacts. Keep the failure in the report.

Keep this canary separate from ordinary tests and require explicit live-Project selection before it can write. Report failures and observed latency; do not invent a latency limit or claim that a live test used a newer backend than the version actually running.

These direct-source fixtures verify watcher and index visibility. They do not establish that a lifecycle Workflow performs the Header changes.
