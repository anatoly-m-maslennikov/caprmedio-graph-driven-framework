---
atom_id: CA-R-2720
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Operator//Alias
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2720-CORE_META_MODEL-DECLARATION--declare-cfel-operator-alias.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare CFEL operator alias

## Claim

### Formal Claim

```CFEL
# model
Operator//Alias == "alias(Relation//RELATION_NAME) == \"notation token\""
```

### Prose Claim

`alias(Relation//RELATION_NAME) == "notation token"` takes a qualified Relation-object address and binds that declared graph Relation's exact name to one nonempty lexical notation token in the selected effective MODEL. Resolve the name exactly; do not infer case folding or undeclared synonyms. A Relation has at most one authored alias. Reject undeclared Relation names, conflicting alias values and ambiguous token bindings. Without an alias, use the full named Relation notation.

This CFEL operator binds notation metadata; it does not construct a literal-to-Node graph Relation or equate different Relation identities. The token follows the owning Relation Declaration's directional reading and grants no endpoint permission, cardinality or second authored fact. In a graph expression, `Relation//NAME` references a Relation object as an endpoint, whereas `((NAME))` invokes that Relation between endpoints.
