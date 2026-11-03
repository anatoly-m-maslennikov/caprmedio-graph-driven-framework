---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evidence_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 30
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1021
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1021-CORE_META_MODEL-DECLARATION--register-evidence-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Register evidence_for relation

## Claim

### Formal Claim

```CFEL
Relation//evidence_for ((HAS_CLASSIFICATION)) Derivation == Direct;

$evidence_carrier ((evidence_for)) Carrier//
```

### Prose Claim

#### Applicability
`evidence_for` relations.

`evidence_for` **means** the direct relation from an Evidence carrier to the
carrier that the Evidence supports.

The Host is an Evidence carrier; the target is the carrier it supports.
Forward `Host ((evidence_for)) Target` and reverse `Target <((evidence_for)) Host` are views of the same Relation fact.
evidence_for relates Evidence carrier to supported carrier.
