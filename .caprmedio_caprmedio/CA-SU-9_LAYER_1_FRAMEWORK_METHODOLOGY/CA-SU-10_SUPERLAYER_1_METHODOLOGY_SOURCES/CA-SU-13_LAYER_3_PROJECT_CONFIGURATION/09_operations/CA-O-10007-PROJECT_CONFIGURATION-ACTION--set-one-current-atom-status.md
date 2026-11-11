---
identity:
  atom_id: CA-O-10007
  ref_id: CA-O-10007
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
    name: CA-O-10007-PROJECT_CONFIGURATION-ACTION--set-one-current-atom-status.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
## Summary

Set one Current Atom Status

## Claim scope

One exact Current Atom and one requested Status in its qualified model's Current group.

## Claim

Set the selected Current Atom's Status to the supplied value allowed by its applicable Current status model. Derive carrier location; preserve Version and Updated At. Report an explicit error on failure. Journal business observations are independent and nonblocking.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedCurrentAtom` a request for additional input, or an explicit failure; any Journal warning is separate.
