---
atom_id: CA-R-1993
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//CARRIES
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
relations:
  child_of:
  - CA-R-1174
version: 19
updated_at: 2026-11-02 08:06:47 +0400
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1993-CORE_META_MODEL-DECLARATION--define-carries.md
  source_atom_id: CA-R-1993
  source_atom_revision: 19
  source_sha256: e4462760db620dd372907ce4ed3a1098c5182f6711ffb5ec9958ea63cf5e6dbd
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary
Define CARRIES

## Claim scope
Carrier bindings of non-ephemeral Entities.

## Claim

CARRIES **means** the directed Relation from a Carrier **to** the non-ephemeral Entity that it stores **or** represents.

```CFEL
((CARRIES)) ((HAS_INVERSE)) ((IS_CARRIED_BY));

((CARRIES)) >| Derivation == Direct;

Carrier// ((CARRIES)) $represented_entity
```

## Semantics



The Target is the non-ephemeral Entity stored or represented by the Carrier.
Forward `Host ((CARRIES)) Target` and reverse `Target <((CARRIES)) Host` are views of the same Relation fact.
CARRIES relates Carrier to non-ephemeral Entity.

## Details

IS_CARRIED_BY **means** the inverse of CARRIES, directed from a non-ephemeral Entity to its Carrier. The Carrier binding exposes this inverse direction; it is not a separately authored primitive Relation fact. This preserves the existing meaning defined by CA-D-257. Neither direction requires a separately registered binding for each YAML field or Markdown section, a new Carrier, a snapshot or a historical record. The applicable D policy specifies how the represented Entity is bound and represented. No additional endpoint class, graph ownership, cardinality or inference permission is introduced by moving this definition to R.
