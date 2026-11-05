---
atom_id: CA-E-791
ref_id: CA-E-791@1-draft
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER
tier: 3
status: Draft
version: 1
updated_at: 2026-11-03 14:19:59 +0400
carrier_destination:
  file:
    name: CA-E-791@1-draft-CORE_META_MODEL-EVAL_POLICY--check-rmed-subject-map-declaration-provenance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Check RMED Subject Map Declaration Provenance

## Claim

### Prose Claim


- Pass when every displayed Primary Subject, direct or inherited Property, or Relation constraint identifies its effective Current Requirement/Form: Declaration by Atom ID@Version, preserves direct versus inherited source labeling, and preserves each applicable full CFEL Formal Claim block verbatim with any parse diagnostic.
- Fail when any cardinality, Format, Property presence, nested name, recursive structure, Relation cardinality, or Formal Claim is taken from a non-Declaration RMED Atom.
- Fail when missing provenance, a fabricated inherited Declaration, missing or conflicting Declaration, or unsupported CFEL is presented as an empty or authoritative result.
- Check one direct Declaration and one inherited Property reusing its original Declaration; check missing provenance, a non-Declaration source, unsupported CFEL, absent Declaration, conflicting Declarations, and a fabricated local inherited Declaration.
