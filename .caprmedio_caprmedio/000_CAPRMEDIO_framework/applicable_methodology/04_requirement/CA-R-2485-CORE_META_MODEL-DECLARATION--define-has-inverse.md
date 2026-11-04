---
atom_id: CA-R-2485
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_INVERSE
version: 7
updated_at: 2026-11-04 23:01:11 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2485-CORE_META_MODEL-DECLARATION--define-has-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2485-CORE_META_MODEL-DECLARATION--define-has-inverse.md
  source_atom_id: CA-R-2485
  source_atom_revision: 7
  source_sha256: 0139782312689c308d27c2ca6fa4c7facd52e6458bd4e71593ace82610fc02be
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Define HAS_INVERSE

## Claim

### Formal Claim

```CFEL
# model
Relation//$relation ((HAS_INVERSE)) Relation//$relation_2;

alias(Relation//HAS_INVERSE) == "<-->";

Relation//HAS_INVERSE ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

HAS_INVERSE binds a direct graph Relation to its derived inverse graph Relation. The Host is Direct and the Target is Derived. The inverse swaps Host and Target for each admitted direct fact. The two Relation identities remain distinct. The direct Declaration owns the shared meaning, endpoint signature, endpoint conditions and this binding; the derived Declaration supplies the reverse written counterpart binding and its own lexical alias when one exists. A bound inverse is inferred from the direct fact and is not authored separately. The inferred IS_DERIVED_RELATION_OF metadata is not repeated in the minimal derived Declaration. A qualified derived counterpart requires its qualification at the direct Declaration and is not an unconditional inverse.

`<-->` is the Subject notation alias for this binding. Written as `Relation//DIRECT <--> Relation//DERIVED` inside the direct Declaration, its left operand identifies the direct Relation and its right operand identifies the derived inverse. It is neither equality nor aliasing of the two Relation identities. The binding does not grant endpoint permissions or outgoing cardinalities.
