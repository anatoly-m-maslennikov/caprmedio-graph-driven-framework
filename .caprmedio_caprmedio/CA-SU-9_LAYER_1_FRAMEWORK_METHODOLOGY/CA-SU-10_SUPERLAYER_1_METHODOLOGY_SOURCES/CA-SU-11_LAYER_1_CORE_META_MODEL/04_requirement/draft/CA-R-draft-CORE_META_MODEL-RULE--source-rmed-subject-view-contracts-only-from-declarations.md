---
atom_id: CA-R-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Rule)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  - CAPRMEDIO_MODEL <+ Projection
version: 1
updated_at: 2026-11-03 14:19:59 +0400
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-draft-CORE_META_MODEL-RULE--source-rmed-subject-view-contracts-only-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Source RMED Subject View Contracts Only from Declarations

## Claim

### Prose Claim


For a selected effective MODEL, an RMED Subject Map must obtain a displayed Primary Subject's or displayed direct or inherited Property's allowed Relation cardinalities, Property presence, direct-value cardinality, direct-value Format, nested Property names, recursive Property structure, and full CFEL Formal Claim only from its effective Current Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration). It must preserve each applicable Declaration's full CFEL Formal Claim block verbatim; a missing, unsupported, or conflicting Declaration result is a diagnostic, not a fallback to another RMED Atom.

An inherited Property must cite and reuse its original effective Declaration; the Map must not create a local Property node or a replacement Declaration. No Claim merger, override inference, or inferred cardinality, Format, nested name, recursive structure, or Formal Claim is permitted.

Absence is distinct from an empty declared value: an empty value is shown only when the selected Declaration explicitly carries it; missing or unsupported CFEL remains unresolved.
