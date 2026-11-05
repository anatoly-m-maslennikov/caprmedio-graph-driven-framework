---
atom_id: CA-R-2475
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
version: 5
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2475-CORE_META_MODEL-DECLARATION--define-narrower-than.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define NARROWER_THAN

## Claim

### Formal Claim

```CFEL
# model
$narrower ((NARROWER_THAN)) $broader;

Relation//NARROWER_THAN ((HAS_INVERSE)) Relation//HAS_NARROWER;

alias(Relation//NARROWER_THAN) == "/";

Relation//NARROWER_THAN ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

NARROWER_THAN relates a narrower MODEL kind to a broader MODEL kind. A Property does not narrow. Both endpoints are MODEL kinds; Property bearers and instance populations do not become kinds through this notation. The narrower kind inherits applicable Relation and Property constraints without cloning declarations or instance facts. HAS_NARROWER is its derived inverse. In `X/Y`, Y is narrower than X; traversal runs from broader to narrower.
