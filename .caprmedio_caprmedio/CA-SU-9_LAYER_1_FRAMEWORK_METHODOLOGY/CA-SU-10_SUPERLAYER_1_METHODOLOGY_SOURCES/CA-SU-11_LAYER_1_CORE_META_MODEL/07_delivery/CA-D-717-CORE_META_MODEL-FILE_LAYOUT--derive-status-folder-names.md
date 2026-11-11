---
identity:
  id: CA-D-717
  ref_id: CA-D-717
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: file_layout
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  tier: 3
state:
  status: active
  version: 1
  updated_at: '2026-11-11T19:37:43+04:00'
destination:
  file:
    name: CA-D-717-CORE_META_MODEL-FILE_LAYOUT--derive-status-folder-names.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---

## Summary

Derive Status folder names

## Claim

### Prose Claim

For a Status with a folder, read the Status Order Number from its Requirement Declaration.

1. Write the number as three decimal digits with leading zeros.
2. Encode the Status name in lowercase snake case.
3. Join the number and name with one underscore.

Use this name for the `<status folder>` segment in the applicable Status Group's File Layout Claim.
