---
identity:
  atom_id: CA-M-1006
  ref_id: CA-M-1006@3
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
  version: 3
  status: archived
  updated_at: '2026-11-11T22:43:16.307614+00:00'
destination:
  file:
    name: CA-M-1006@3-PROGRAMMATIC-DIRECT_POLICY--read-atoms-through-targeted-workbench-queries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/099_archived
---
## Summary

Read Atoms through targeted Workbench queries

## Claim

### Prose Claim

Use the selected Project’s `query_run` for Atom reads. To speed up a Workflow, at most one direct Atom read is allowed per run. The exact Project-relative path and filename must already be known. All other reads use `query_run`, including reads of Current, Draft, and Archived Atoms and reads inside write operations.

Filter rows in SQL and select only the columns the caller needs. Use joins or CTEs when they avoid repeated queries. Reuse results across steps that need the same data.

## Details

For an exact lookup, report missing, ambiguous, or stale results. Verify the expected Atom state for writes. A query in the same operation must see Atom changes already made by that operation.
