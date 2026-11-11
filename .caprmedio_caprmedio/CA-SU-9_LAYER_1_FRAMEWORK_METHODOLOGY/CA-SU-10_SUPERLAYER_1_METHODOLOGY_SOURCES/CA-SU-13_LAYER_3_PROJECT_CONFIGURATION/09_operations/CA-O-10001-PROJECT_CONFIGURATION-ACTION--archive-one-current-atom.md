---
identity:
  atom_id: CA-O-10001
  ref_id: CA-O-10001
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
    name: CA-O-10001-PROJECT_CONFIGURATION-ACTION--archive-one-current-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
## Summary

Archive one Current Atom

## Claim scope

One exact selected Current Atom. The caller handles any contained Atoms through separate invocations under CA-R-1521. Archived inputs, inferred replacements, and overwrites are invalid.

## Claim

Archive the selected Current Atom using its applicable status model and derived carrier location. Preserve Version and Updated At. Report an explicit error on failure. An actual business observation may be recorded in the Journal independently; a recording failure does not block archival.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedArchivedAtom` a request for additional input, or an explicit failure; any Journal warning is separate.
