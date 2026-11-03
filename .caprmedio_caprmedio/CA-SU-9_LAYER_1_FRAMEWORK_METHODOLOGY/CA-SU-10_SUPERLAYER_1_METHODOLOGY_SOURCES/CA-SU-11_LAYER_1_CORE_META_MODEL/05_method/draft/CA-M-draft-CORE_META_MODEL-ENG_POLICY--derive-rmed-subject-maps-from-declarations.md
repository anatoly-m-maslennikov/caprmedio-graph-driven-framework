---
atom_id: CA-M-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Role := Requirement)/(.Form := Declaration)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER
version: 1
updated_at: 2026-11-03 14:19:59 +0400
relations: {}
tier: 3
role: Method
form: Eng Policy
carrier_destination:
  file:
    name: CA-M-draft-CORE_META_MODEL-ENG_POLICY--derive-rmed-subject-maps-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/draft
---
## Summary

Derive RMED Subject Maps from Declarations

## Claim

- Select and pin Current source Atoms, resolve each active Subject's declared Properties and Relation constraints, then resolve NARROWER inheritance to obtain effective Properties and constraints.
- Label every output Property or constraint as `direct` with its declaring Atom ID@Version or `inherited` with its original Declaration Atom ID@Version.
- Read cardinality, Format, nested names, recursive structure, Relation cardinalities, and a full CFEL Formal Claim only from the applicable Declaration for a displayed Primary Subject or displayed direct or inherited Property.
- Copy each applicable full CFEL Formal Claim block verbatim, including an unparsed or unsupported block; attach its diagnostic without discarding, shortening, merging, inferring, or overriding the Claim.
- Retain a diagnostic rather than treating a missing Declaration as an empty declaration.
