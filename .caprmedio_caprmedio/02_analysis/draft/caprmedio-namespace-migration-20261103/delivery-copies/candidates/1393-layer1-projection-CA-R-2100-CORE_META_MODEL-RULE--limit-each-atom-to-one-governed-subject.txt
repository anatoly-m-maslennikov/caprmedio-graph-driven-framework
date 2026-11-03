---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Subjects
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation//GOVERNS
atom_id: CA-R-2100
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 8
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2100-CORE_META_MODEL-RULE--limit-each-atom-to-one-governed-subject.md
  source_atom_id: CA-R-2100
  source_atom_revision: 8
  source_sha256: b2ffead2ad37816a6e3d08874b643be9fa284779606c3e84afa801f68d9ecc43
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Limit each Atom to one governed Subject

## Claim scope

The direct GOVERNS Subject Relations recorded in an Atom's Subjects.

## Claim

An Atom **may** have zero or one direct GOVERNS Subject Relation. No Atom's Subjects **may** contain more than one direct GOVERNS Subject Relation.

## Details

This Rule limits cardinality only. It does not require an Atom to have a GOVERNS Subject. The Subjects collection is optional, and DEPENDS_ON relations are not limited by this Rule.
