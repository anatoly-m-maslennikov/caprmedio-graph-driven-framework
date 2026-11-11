---
atom_id: CA-M-496
ref_id: CA-M-496@1-draft
container:
  scope_unit: CA-SU-11
role: Method
form: Eng Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Declaration)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER
tier: 3
status: Draft
version: 1
updated_at: 2026-11-03 14:19:59 +0400
carrier_destination:
  file:
    name: CA-M-496@1-draft-CORE_META_MODEL-ENG_POLICY--derive-rmed-subject-maps-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/000_draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Derive RMED Subject Maps from Declarations

## Claim

### Prose Claim


- Select and pin Current source Atoms, resolve each active Subject's declared Properties and Relation constraints, then resolve NARROWER inheritance to obtain effective Properties and constraints.
- Label every output Property or constraint as `direct` with its declaring Atom ID@Version or `inherited` with its original Declaration Atom ID@Version.
- Read cardinality, Format, nested names, recursive structure, Relation cardinalities, and a full CFEL Formal Claim only from the applicable Declaration for a displayed Primary Subject or displayed direct or inherited Property.
- Copy each applicable full CFEL Formal Claim block verbatim, including an unparsed or unsupported block; attach its diagnostic without discarding, shortening, merging, inferring, or overriding the Claim.
- Retain a diagnostic rather than treating a missing Declaration as an empty declaration.
