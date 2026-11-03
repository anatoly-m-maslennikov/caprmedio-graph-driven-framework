---
subjects:
  active: CFEL <+ Relation//evidence_for
  passive:
  - CFEL > Relation
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1021
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1021-CORE_META_MODEL-DECLARATION--register-evidence-for-relation.md
  source_atom_id: CA-R-1021
  source_atom_revision: 29
  source_sha256: 7eebfa3ea231237bbb77f249055f7e2e86e2c436338c18938fd5067681c6b4ea
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register evidence_for relation

## Claim scope

`evidence_for` relations.

## Claim

`evidence_for` **means** the direct relation from an Evidence carrier to the
carrier that the Evidence supports.

```CFEL
((evidence_for)) >| Derivation == Direct;

$evidence_carrier ((evidence_for)) Carrier//
```

## Semantics



The Host is an Evidence carrier; the target is the carrier it supports.
Forward `Host ((evidence_for)) Target` and reverse `Target <((evidence_for)) Host` are views of the same Relation fact.
evidence_for relates Evidence carrier to supported carrier.

