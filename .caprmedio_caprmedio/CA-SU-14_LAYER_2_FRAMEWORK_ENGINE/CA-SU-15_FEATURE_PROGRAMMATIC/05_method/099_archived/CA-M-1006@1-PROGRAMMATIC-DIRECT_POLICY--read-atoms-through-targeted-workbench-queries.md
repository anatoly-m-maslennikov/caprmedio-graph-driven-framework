---
identity:
  atom_id: CA-M-1006
  ref_id: CA-M-1006@1
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
  version: 1
  status: archived
  updated_at: '2026-11-11T22:37:20.213205+00:00'
destination:
  file:
    name: CA-M-1006@1-PROGRAMMATIC-DIRECT_POLICY--read-atoms-through-targeted-workbench-queries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/099_archived
---
## Summary

Read Atoms through targeted Workbench queries

## Claim

### Prose Claim

Read Atom data through the selected Project’s `query_run`. Filter rows in SQL and select only the columns needed by the caller. Use joins or CTEs to retrieve related rows together when that avoids repeated queries. Reuse the result across steps that need the same data.

## Details

An exact Atom lookup must report missing, ambiguous or stale data. Before a write, check the selected carrier and its expected state. Steps in the same operation must see the Atom changes already made by that operation.
