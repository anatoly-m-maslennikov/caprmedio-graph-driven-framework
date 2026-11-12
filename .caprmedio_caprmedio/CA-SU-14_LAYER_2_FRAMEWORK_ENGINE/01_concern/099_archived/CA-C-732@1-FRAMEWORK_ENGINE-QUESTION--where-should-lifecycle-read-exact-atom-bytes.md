---
identity:
  atom_id: CA-C-732
  ref_id: CA-C-732@1
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
  version: 1
  status: archived
  updated_at: '2026-11-12T01:57:19.304380+00:00'
destination:
  file:
    name: CA-C-732@1-FRAMEWORK_ENGINE-QUESTION--where-should-lifecycle-read-exact-atom-bytes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/099_archived
---
## Summary

Where should lifecycle read exact Atom bytes

## Question

May Workbench retain exact Atom bytes in a private, rebuildable DuckDB table for lifecycle, or should the one direct read allowance be applied to each target of a multi-Atom operation?

## Details

Candidate discovery uses indexed queries. Exact copy and stale-source checks still read source bytes by path. A batch or Plan cascade can therefore read more than one file. Keeping indexed exact bytes would support the one-file allowance for the entire call, but CA-D-672 excludes retained source bytes. The same choice affects cold-start RAM and Archive scope loading.

Tracked in CA-P-3017.