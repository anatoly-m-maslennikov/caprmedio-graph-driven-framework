---
atom_id: CA-R-2813
ref_id: CA-R-2813@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 14:25:52 +0400
carrier_destination:
  file:
    name: CA-R-2813@1-draft-RULE--define-recursive-property-selection-with.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define recursive Property selection with `**`

## Claim

### Prose Claim

Within one bearer, `p.**` selects the distinct dependent Property identities recursively below Property `p` across all descendant depths. `p.**{::n}` counts that selected set across all descendant depths; it does not count values or Properties belonging to another bearer.
