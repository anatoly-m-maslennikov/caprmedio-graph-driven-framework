---
identity:
  atom_id: CA-R-3089
  ref_id: CA-R-3089
context:
  role: requirement
  form: Rule
  tier: 3
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 2
  status: active
  updated_at: '2026-11-12T16:57:45.022241+00:00'
destination:
  file:
    name: CA-R-3089-FRAMEWORK_ENGINE-RULE--create-an-independent-draft-from-an-atom.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---
## Summary

Create an independent Draft from an Atom

## Claim

### Prose Claim

Create Draft lets the caller choose to copy an existing Atom into a new independent Draft. The source may be Current, Archived or another Draft. If the caller supplies only an Atom ID, select Current. An explicit Version or Draft reference selects the exact requested source.

Give the copy a new Atom ID and Version 1 at creation. Copy the source, including all Relations, and apply only the supplied changes. Do not add a replacement relation to the source just because it was copied. Leave the source unchanged. The copy does not supersede it.

The existing successor option retains its identity and Version rules.
