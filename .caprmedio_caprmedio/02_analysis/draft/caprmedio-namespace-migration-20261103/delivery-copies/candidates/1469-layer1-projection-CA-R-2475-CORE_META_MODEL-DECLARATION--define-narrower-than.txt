---
atom_id: CA-R-2475
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//NARROWER_THAN
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2475-CORE_META_MODEL-DECLARATION--define-narrower-than.md
  source_atom_id: CA-R-2475
  source_atom_revision: 4
  source_sha256: a322ecf983e39b89c74286cf2400e7c49ebc047a380b859668eb8218059ed06b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define NARROWER_THAN

## Claim

The narrower kind inherits applicable Relation and Property constraints without cloning declarations or instance facts.

```CFEL
$narrower ((NARROWER_THAN)) $broader;
((NARROWER_THAN)) ((HAS_INVERSE)) ((HAS_NARROWER));

((NARROWER_THAN)) == /;
((NARROWER_THAN)) >| Derivation == Direct
```

## Semantics

The endpoints are declared kinds supporting narrowing; a Property does not narrow. The narrower kind inherits applicable constraints.



Forward `Host ((NARROWER_THAN)) Target` and reverse `Target <((NARROWER_THAN)) Host` are views of the same Relation fact.
In `X/Y`, Y NARROWER_THAN X; traversal runs from broader to narrower.
NARROWER_THAN relates narrower declared kind to broader declared kind.

