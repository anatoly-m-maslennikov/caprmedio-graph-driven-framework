---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evidence_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 31
updated_at: 2026-11-03 23:25:51 +0400
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
Carrier//$evidence_carrier ((evidence_for)) Carrier//$supported_carrier
```

### Prose Claim

evidence_for is the direct Relation owned by an evidence Carrier. The Host is that evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports.

The generic Target variable retains precisely that source-supported endpoint condition; it does not admit every supported Carrier or introduce a new kind. These are endpoint permissions, not extra fields on a reusable Relation Type or additional storage facts for derived inverses. Forward `Host ((evidence_for)) Target` and reverse `Target <((evidence_for)) Host` are written views of the same direct fact.
