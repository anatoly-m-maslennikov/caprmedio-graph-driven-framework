---
identity:
  atom_id: CA-C-733
  ref_id: CA-C-733
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
  updated_at: '2026-11-12T08:51:50.875119+00:00'
destination:
  file:
    name: CA-C-733-FRAMEWORK_ENGINE-QUESTION--how-should-image-builds-query-lifecycle-placement-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/021_resolved
---
## Summary

How should image builds query lifecycle placement declarations

## Question

Which query source should a clean image build use to select lifecycle placement Declarations by Role and main Subject before the new Workbench image exists?

## Details

The Operator chose the N+1 build rule. The new image build uses the previous ready image’s Workbench backend to query staged Current sources by Delivery Role and main Subject. The previous image runs in an isolated Docker helper with the staged sources mounted read-only. The compiler verifies the returned path, Atom ID, Version and content hash before compiling the Formal Claims. The source selection has no pinned Atom IDs.

The first build uses native staged-source selection when no previous ready image exists. A recorded predecessor that cannot run the query fails the build.

The exact predecessor image selected the same five placement Formal Claims as the staged-source bootstrap. The replacement image built successfully using that predecessor. Tracked in CA-P-3017 and CA-P-3024.
