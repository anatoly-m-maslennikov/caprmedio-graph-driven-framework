---
identity:
  atom_id: CA-M-1006
  ref_id: CA-M-1006
context:
  role: method
  form: direct_policy
  tier: 5
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Source Retrieval
  container:
    scope_unit: PROGRAMMATIC
state:
  version: 6
  status: active
  updated_at: '2026-11-12T03:32:52.174163+00:00'
destination:
  file:
    name: CA-M-1006-PROGRAMMATIC-DIRECT_POLICY--read-atoms-through-targeted-workbench-queries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---
## Summary

Read Atoms through targeted Workbench queries

## Claim

### Prose Claim

Use the selected Project’s `query_run` for Atom reads, including reads of Current, Draft, and Archived Atoms inside write operations. Select the exact carriers and retrieve derived relations through `query_run`. Filter rows in SQL, select only the columns needed, and use joins or CTEs when they avoid repeated queries. Reuse results across steps that need the same data.

When an operation needs exact source bytes, a single-target operation may read at most one Atom file directly. Batch Archive, batch Promote Draft, and Plan Status cascades may read at most one exact Atom file per target. Every direct read uses the Project-relative path and filename already selected through `query_run`. Reuse the bytes within the call without keeping a persistent copy.

## Details

For lifecycle selection, use the first valid native carrier that matches the requested Atom and, when supplied, its expected Version. Report a missing or stale selection explicitly. If the requested Archive is unloaded, report that separately. Workbench reports duplicate Current and Archived revisions through its audit. Verify the selected carrier’s expected state before a write and check the actual effects. Queries within an operation must see changes already made by that operation.
