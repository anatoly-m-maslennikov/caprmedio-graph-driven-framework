---
subjects:
  active: CFEL <+ Relation
version: 31
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-1040
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1040-CORE_META_MODEL-RULE--reject-authored-inverse-relations.md
  source_atom_id: CA-R-1040
  source_atom_revision: 31
  source_sha256: df4107ad8edbb57ce26f128eda5996991a26c87e76106841d4f78b7d75ea98c5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Reject authored inverse relations

## Claim scope

authored inverse typed relations.

## Claim

validators **must** reject **every** inverse typed relation authored **in** an Atom Carrier.

## Details

Inverse means the derived direction declared by the governing Relation Kind definition, not a direction guessed from its name. In the containment pair, IS_CONTAINED_BY is direct from child to parent and is the only permitted authoritative direction when Atom containment is authored; CONTAINS is the inverse and must not be separately authored. This clarification does not admit a new runtime relation key or waive endpoint Entity Definition constraints.
