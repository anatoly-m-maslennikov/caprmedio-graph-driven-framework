---
atom_id: CA-R-2100
ref_id: CA-R-2100
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
tier: 1
status: Active
version: 8
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2100-CORE_META_MODEL-RULE--limit-each-atom-to-one-governed-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Limit each Atom to one governed Subject

## Claim

### Prose Claim


The direct GOVERNS Subject Relations recorded in an Atom's Subjects.


An Atom **may** have zero or one direct GOVERNS Subject Relation. No Atom's Subjects **may** contain more than one direct GOVERNS Subject Relation.

## Details

This Rule limits cardinality only. It does not require an Atom to have a GOVERNS Subject. The Subjects collection is optional, and DEPENDS_ON relations are not limited by this Rule.
