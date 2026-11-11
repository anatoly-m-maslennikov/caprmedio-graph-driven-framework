---
identity:
  atom_id: CA-O-10000
  ref_id: CA-O-10000
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
  status: Active
  version: 1
  updated_at: 2026-11-11 14:05:36 +0400
destination:
  file:
    name: CA-O-10000-PROJECT_CONFIGURATION-ACTION--apply-one-direct-atom-update.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
## Summary

Apply one Direct Atom Update

## Claim scope

One exactly selected non-container Atom and its requested changes.

## Claim

Resolve the selected Draft, Current or Archived Atom and apply supplied property changes in place, carrying omitted properties forward. Derive the carrier filename and location from the resulting properties and model. Preserve Version and Updated At; do not gate the edit on a semantic change classification. Report an explicit error on failure. An actual business observation may be recorded in the Journal independently; a recording failure does not block the edit.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedAtom` a request for additional input, or an explicit failure; any Journal warning is separate.
