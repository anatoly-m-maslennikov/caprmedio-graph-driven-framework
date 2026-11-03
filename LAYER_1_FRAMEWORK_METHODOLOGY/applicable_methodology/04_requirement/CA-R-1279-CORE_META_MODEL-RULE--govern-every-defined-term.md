---
subjects:
  active: CFEL <+ Relation//GOVERNS
  passive:
  - Atom.Content.Semantics
  - Entity
  - Term
  - Atom.Content
version: 32
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1279
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term.md
  source_atom_id: CA-R-1279
  source_atom_revision: 32
  source_sha256: d138a55d90bb223d443bb8a4556c1242ea64e2e52f93ec60dcd9caa7e5c9c329
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Govern Every Defined Term

## Claim scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

when an Atom's Claim explicitly defines a Term, it **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by that Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim, source use, **and** applicable Atom.Semantics establish that Term's meaning; the other Term components **in** the path are references **to** their own meanings, **not** additional meanings supplied by this Atom.
