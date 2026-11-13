---
identity:
  atom_id: CA-O-10003
  ref_id: CA-O-10003@2-draft
context:
  container:
    scope_unit: CA-SU-13
  role: Operations
  form: Action
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  tier: 3
state:
  status: draft
  version: 2
  updated_at: '2026-11-13T08:16:20.123624+00:00'
destination:
  file:
    name: CA-O-10003@2-draft-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/000_draft
---
## Summary

Create one Atom Draft

## Claim scope

One non-container Draft materialization under its applicable model.

## Claim

Create a Draft from `newAtom` properties or from a selected existing Atom and supplied property changes. For an existing Atom read its full properties and content, merge supplied properties, and carry all others forward. Derive Draft metadata, filename and path from the resulting properties and model; the caller does not provide a filename or path. A supplied Scope Unit is a logical property and determines derived placement under the destination Scope Unit. For an existing Atom with unchanged Summary and Content Role, assign an unused Draft Version for the same ID. Promotion determines the published Version independently. If Summary or Content Role changes, the result is a new identity promoted at Version 1. Editing an existing Draft in place preserves its Version and Updated At. Check formats and allowed values without a semantic gate. On missing or invalid input provide a short explanation and request an additional input dictionary; wait for it. Report an effect failure explicitly. Journal business observations are independent and nonblocking.

### Outputs

`savedDraft`, a request for additional input, or an explicit failure; any Journal warning is separate.
