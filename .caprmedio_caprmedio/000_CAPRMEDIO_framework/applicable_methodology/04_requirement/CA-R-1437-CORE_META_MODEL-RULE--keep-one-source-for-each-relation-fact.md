---
subjects:
  active: CFEL <+ Relation
  passive:
  - CFEL <+ Relation
  - Entity
  - Projection
  - Aspects <+ Engineering <+ Traceability
  - Atom.Content
  - Journal
version: 32
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1437
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1437-CORE_META_MODEL-RULE--keep-one-source-for-each-relation-fact.md
  source_atom_id: CA-R-1437
  source_atom_revision: 32
  source_sha256: ef6f072c89042dce91932074b01a8e0380d5cd1cdbd76fb02120d05337bc9adc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep one source for each relation fact

## Claim scope

authoritative source declarations for Relation facts.

## Claim

**every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.

a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.
