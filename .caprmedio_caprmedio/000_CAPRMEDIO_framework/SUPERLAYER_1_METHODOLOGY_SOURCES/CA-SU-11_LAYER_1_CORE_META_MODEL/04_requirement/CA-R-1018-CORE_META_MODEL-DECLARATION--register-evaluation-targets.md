---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evaluation_for
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 38
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1018
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1018-CORE_META_MODEL-DECLARATION--register-evaluation-targets.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Register Evaluation targets

## Claim

### Formal Claim

```CFEL
# model
Relation//evaluation_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Evaluation)//$atom ((evaluation_for)) Atom//$atom_2
```

### Prose Claim

#### Applicability
direct `evaluation_for` relations.

`evaluation_for` **means** the direct relation from an Evaluation Atom to an
Atom whose authority the Evaluation checks.

Forward `Host ((evaluation_for)) Target` and reverse `Target <((evaluation_for)) Host` are views of the same Relation fact.
evaluation_for relates Evaluation Atom to Atom whose authority is evaluated.
