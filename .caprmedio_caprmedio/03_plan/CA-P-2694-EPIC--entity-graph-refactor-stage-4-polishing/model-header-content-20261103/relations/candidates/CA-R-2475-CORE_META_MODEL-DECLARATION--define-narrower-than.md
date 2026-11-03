---
atom_id: CA-R-2475
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//NARROWER_THAN
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define NARROWER_THAN

## Claim

### Formal Claim

```CFEL
$narrower ((NARROWER_THAN)) $broader;
Relation//NARROWER_THAN ((HAS_INVERSE)) Relation//HAS_NARROWER;

alias(Relation//NARROWER_THAN) == "/";
Relation//NARROWER_THAN ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

NARROWER_THAN relates a narrower MODEL kind to a broader MODEL kind. A Property does not narrow. Both endpoints are MODEL kinds; Property bearers and instance populations do not become kinds through this notation. The narrower kind inherits applicable Relation and Property constraints without cloning declarations or instance facts. HAS_NARROWER is its derived inverse. In `X/Y`, Y is narrower than X; traversal runs from broader to narrower.
