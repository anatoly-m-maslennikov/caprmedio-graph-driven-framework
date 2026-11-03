---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ Atom
version: 42
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-806
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-806-CORE_META_MODEL-RULE--register-complete-relation-kind-metadata.md
  source_atom_id: CA-R-806
  source_atom_revision: 42
  source_sha256: 83b65a4ae7b063a7d6c2da639fc1f07dd4d1fd7f5109577faf2769c931c1fd5a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Complete Relation Kind Metadata

## Claim scope

admitted Relation Types and their defining source Claims.

## Claim

The canonical name and meaning of each Relation Type **are** defined in its governing R Claim(s). A governing Claim **may** state a relevant inverse, derivation, or transitivity rule; no such optional property is required when it is not relevant.

## Details

Relation Type names are shared and unique in the Project. Existing Entity Definition constraints, where applicable, supply graph-specific admission, endpoint classes, endpoint graph contexts, cardinality, and other permissions or prohibitions; this contract does not require a separate Graph Rule for every known Type or choose default-allow/default-deny semantics. The Type definition retains its canonical meaning and any evidenced optional inverse, derivation, or transitivity semantics. A declared direct direction identifies the one authored fact where relevant; inverse or derived navigation remains derived under its defining authority. A name such as IS_CONTAINED_BY does not make that direction an inverse. Existing endpoint and admissibility constraints remain in their governing Entity Definition constraints; this contract does not itself rewrite them.
