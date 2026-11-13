---
identity:
  atom_id: CA-O-10005
  ref_id: CA-O-10005@2-draft
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
  updated_at: '2026-11-13T08:17:27.587673+00:00'
destination:
  file:
    name: CA-O-10005@2-draft-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/000_draft
---
## Summary

Promote one Atom Draft

## Claim scope

This Action publishes one exact selected Draft for one non-container Atom under the applicable model. Replacement targets explicitly named by the Draft are archived as part of promotion.

## Claim

For a Draft of a new Version of the same Atom, include its exact same-ID predecessor. Also include every target named by `IS_REPLACEMENT_FOR`. Resolve this combined set once per identity, including targets with different IDs and many-to-one replacement. Before publishing the Draft as Current, archive each eligible Current target once and skip every target already Archived, including one archived by composed Update. Preserve archived targets' Version and Updated At. Then publish the Draft using the supplied allowed Current Status and remove its Draft carrier. Publish Version 1 when promoting the Version 1 Draft of an unpublished Atom ID. Preserve any other Drafts for that ID. If Summary or Content Role changed from its source, promote a new identity at Version 1. For an update under an existing published ID, publish one more than the maximum existing Version for that ID across Current, Archived and Draft carriers, including the selected Draft. Preserve the selected Draft content and resolve the actual Current predecessor independently of its Draft Version. Derive the filename and location from the model. On an effect failure stop and report completed and incomplete effects. Journal business observations are independent and nonblocking.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedCurrentAtom`, archived replacement targets and `removedDraft`, a request for additional input, or an explicit failure; any Journal warning is separate.
