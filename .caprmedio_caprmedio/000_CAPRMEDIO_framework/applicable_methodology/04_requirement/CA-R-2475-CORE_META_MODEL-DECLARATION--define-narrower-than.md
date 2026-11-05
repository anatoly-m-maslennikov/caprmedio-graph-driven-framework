---
atom_id: CA-R-2475
ref_id: CA-R-2475
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
tier: 3
status: Active
version: 5
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2475-CORE_META_MODEL-DECLARATION--define-narrower-than.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2475-CORE_META_MODEL-DECLARATION--define-narrower-than.md
  source_atom_id: CA-R-2475
  source_atom_revision: 5
  source_sha256: 6e5a7cf8ff9b5123695d88c31fd358f67d0ffbff061e079893f5e54e83c1927f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define NARROWER_THAN

## Claim

### Prose Claim

NARROWER_THAN relates a narrower MODEL kind to a broader MODEL kind. A Property does not narrow. Both endpoints are MODEL kinds; Property bearers and instance populations do not become kinds through this notation. The narrower kind inherits applicable Relation and Property constraints without cloning declarations or instance facts. HAS_NARROWER is its derived inverse. In `X/Y`, Y is narrower than X; traversal runs from broader to narrower.
### Formal Claim

```CFEL
# model
$narrower ((NARROWER_THAN)) $broader;

Relation//NARROWER_THAN ((HAS_INVERSE)) Relation//HAS_NARROWER;

alias(Relation//NARROWER_THAN) == "/";

Relation//NARROWER_THAN ((HAS_CLASSIFICATION)) Derivation == Direct
```

