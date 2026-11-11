---
identity:
  atom_id: CA-O-10005
  ref_id: CA-O-10005
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
    name: CA-O-10005-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
## Summary

Promote one Atom Draft

## Claim scope

This Action publishes one exact selected Draft for one non-container Atom under the applicable model. Replacement targets explicitly named by the Draft are archived as part of promotion.

## Claim

For a Draft of a new Version of the same Atom, include its exact same-ID predecessor. Also include every target named by `IS_REPLACEMENT_FOR`. Resolve this combined set once per identity, including targets with different IDs and many-to-one replacement. Before publishing the Draft as Current, archive each eligible Current target once and skip every target already Archived, including one archived by composed Update. Preserve archived targets' Version and Updated At. Then publish the Draft using the supplied allowed Current Status and remove its Draft carrier. If Summary or Content Role changed from its source, promote a new identity at Version 1; otherwise retain the existing Draft Version without an additional increment. Derive the filename and location from the model. On an effect failure stop and report completed and incomplete effects. Journal business observations are independent and nonblocking.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedCurrentAtom`, archived replacement targets and `removedDraft`, a request for additional input, or an explicit failure; any Journal warning is separate.
