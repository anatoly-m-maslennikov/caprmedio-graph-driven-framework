---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-2131
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Active
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2131-CORE_META_MODEL-RULE--admit-numeric-tiers-in-non-project-scope-units.md
  source_atom_id: CA-R-2131
  source_atom_revision: 10
  source_sha256: 13d00b81fe6e67ada09b6a54daaea57910a87a22ff62b50d2a3c93b3d9cdf48b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Admit Numeric Tiers in Non-Project Scope Units

## Claim scope

ordinary Atoms owned by non-Project Scope Units.

## Claim

a non-Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
