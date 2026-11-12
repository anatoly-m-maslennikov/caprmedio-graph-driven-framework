---
identity:
  atom_id: CA-C-733
  ref_id: CA-C-733@1
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
  updated_at: '2026-11-12T01:57:22.674635+00:00'
destination:
  file:
    name: CA-C-733@1-FRAMEWORK_ENGINE-QUESTION--how-should-image-builds-query-lifecycle-placement-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/099_archived
---
## Summary

How should image builds query lifecycle placement declarations

## Question

Which query source should a clean image build use to select lifecycle placement Declarations by Role and main Subject before the Workbench image exists?

## Details

The compiler selects the staged Current Delivery Formal Claims by Role and Topic without pinned selection IDs. It discovers the source files directly during the build. The runtime reads the compiled asset. A fresh offline image build has no running project query_run to select those declarations from.

Tracked in CA-P-3017.