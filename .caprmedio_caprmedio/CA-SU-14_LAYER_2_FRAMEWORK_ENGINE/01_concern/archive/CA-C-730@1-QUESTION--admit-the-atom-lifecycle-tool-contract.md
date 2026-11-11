---
identity:
  id: CA-C-730
  ref_id: CA-C-730@1
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Archived
  version: 1
  updated_at: 2026-11-11 06:21:04 +0400
destination:
  file:
    name: CA-C-730@1-QUESTION--admit-the-atom-lifecycle-tool-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archive
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-O-127
  - CA-P-2934
---
 
## Summary

Admit the Atom Lifecycle Tool contract

## Concern

Which operations and invalid-input behavior should the new MCP Tools expose under P2934? Current O127 admits seven operations in one Workflow, including Move. It waits for an additional input dictionary on a format or allowed-value error and allows cancellation while waiting. The six separate Workflow drafts remain unadopted and omit Move.

## Details

Select the Current combined operation contract or review and adopt the split contracts with a disposition for Move. Decide how a new Tool obtains corrected input when no generic Workflow engine is in scope. The retained MCP provider has transport cancellation but no lifecycle input continuation. An immediate invalid-input result would change the Current waiting behavior.

The retirement removed the old lifecycle effect adapters. Retained metadata, Header, scope and Journal primitives can support new effects. Direct Update of an exactly selected carrier has Current requirements for persisted readback, unchanged ID, Version and Updated At, and preservation of omitted properties. P2934 can prepare that isolated effect and its fixtures while Tool publication awaits an admitted contract.
