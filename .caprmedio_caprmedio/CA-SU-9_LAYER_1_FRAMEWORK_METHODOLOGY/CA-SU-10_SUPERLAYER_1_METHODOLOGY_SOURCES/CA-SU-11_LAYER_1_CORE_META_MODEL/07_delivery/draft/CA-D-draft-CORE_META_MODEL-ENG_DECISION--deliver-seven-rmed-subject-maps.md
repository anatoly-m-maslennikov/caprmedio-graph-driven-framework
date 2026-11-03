---
atom_id: CA-D-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER
version: 1
updated_at: 2026-11-03 14:19:59 +0400
relations: {}
tier: 3
role: Delivery
form: Eng Decision
carrier_destination:
  file:
    name: CA-D-draft-CORE_META_MODEL-ENG_DECISION--deliver-seven-rmed-subject-maps.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
---
## Summary

Deliver Seven RMED Subject Maps

## Claim

### Prose Claim


Deliver seven named Maps from an explicit named source selection: `Subject Tree`, `Direct Property List`, `Effective Property List`, `Effective Formal Claim List`, `Passive-only Subject Audit`, `Missing Requirement Declaration Audit`, and `Defining Atom Summary`. Each Map must pin complete source provenance as selected Current Atom ID@Version values, state its bounded scope, and report diagnostics.

`Subject Tree` renders selected Subjects and NARROWER structure. `Direct Property List` shows only directly declared Properties. `Effective Property List` shows direct and inherited Properties with source labels, cardinalities, Formats, nested names, and recursive structure. `Effective Formal Claim List` preserves each full verbatim CFEL Formal Claim block applicable to a displayed Primary Subject or displayed direct or inherited Property, including an unparsed block with its diagnostic. `Passive-only Subject Audit` lists exact passive Subject paths that have no active occurrence in the selection. `Missing Requirement Declaration Audit` lists selected Subjects and their displayed direct or inherited Properties whose effective Requirement/Form: Declaration coverage is absent, conflicting, or unsupported.

`Defining Atom Summary` covers entity-level Subjects. It reports defining coverage from a Current Requirement whose Form name ends in Declaration or Definition, including Scope Unit Declaration, or from a Current Method Term Definition for a Term. Legacy Entity and Relation Definitions count only as defining coverage. It reports two independent flags: `no defining Atom` when no qualifying defining-coverage Atom exists, and `no active Atom` when no Current Atom has that Subject as its active Subject; either, both, or neither flag may be set. Defining coverage never supplies cardinality, Format, or Formal Claim authority. The source selection and source ID@Version provenance remain visible for every Map; direct and inherited source labels remain distinct.
