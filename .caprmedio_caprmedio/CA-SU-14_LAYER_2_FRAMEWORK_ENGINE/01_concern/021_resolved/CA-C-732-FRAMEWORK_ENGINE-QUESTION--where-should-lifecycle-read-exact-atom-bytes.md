---
identity:
  atom_id: CA-C-732
  ref_id: CA-C-732
context:
  role: concern
  form: Question
  tier: 3
  concern:
    priority: Medium
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 2
  status: resolved
  updated_at: '2026-11-12T03:36:57.273397+00:00'
destination:
  file:
    name: CA-C-732-FRAMEWORK_ENGINE-QUESTION--where-should-lifecycle-read-exact-atom-bytes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/021_resolved
---
## Summary

Where should lifecycle read exact Atom bytes

## Question

May Workbench retain exact Atom bytes in a private, rebuildable DuckDB table for lifecycle, or should the one direct read allowance be applied to each target of a multi-Atom operation?

## Details

The Operator approved one exact file read per target. CA-M-1006@6 records the rule for batch Archive, batch Promote Draft, and Plan Status cascades. Lifecycle selects targets through Workbench, reads each selected carrier by its exact path, and reuses verified bytes within the call. Workbench discards those bytes when the call ends. Carrier checks still verify that selected files are current and that writes took effect. Tracked in CA-P-3017.
