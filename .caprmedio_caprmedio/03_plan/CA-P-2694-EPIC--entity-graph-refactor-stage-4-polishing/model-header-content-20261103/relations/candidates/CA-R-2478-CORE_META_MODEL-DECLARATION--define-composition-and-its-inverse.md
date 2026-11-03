---
atom_id: CA-R-2478
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define composition and its inverse

## Claim

### Formal Claim

```CFEL
$part ((IS_CONTAINED_BY)) $container;
Relation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;
alias(Relation//IS_CONTAINED_BY) == "+>";
Relation//IS_CONTAINED_BY ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

IS_CONTAINED_BY relates a contained declared Entity or instance to its immediate Container. The Target has classification `Container = yes`. Containment does not imply narrowing or inheritance. CONTAINS is its derived inverse: its Host and Target are the direct Target and Host, respectively. Store the direct fact once.
