---
atom_id: CA-R-2720
ref_id: CA-R-2720
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Operator//Alias
tier: 3
status: Active
version: 3
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2720-CORE_META_MODEL-DECLARATION--declare-cfel-operator-alias.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare CFEL operator alias

## Claim

### Prose Claim

`alias(Relation//RELATION_NAME) == "notation token"` takes a qualified canonical Relation model name or its declared inverse alias model name and binds that written name to one nonempty lexical notation token in the selected effective MODEL. Resolve the name exactly; do not infer case folding or undeclared synonyms. Each written name has at most one authored short token. Reject undeclared Relation names, conflicting alias values and ambiguous token bindings. Without an alias, use the full named Relation notation.

This CFEL operator binds notation metadata; an inverse alias name is not a separate Relation entity; it does not construct a literal-to-Node graph Relation or equate different Relation identities. The token follows its written name's directional reading and grants no endpoint permission, cardinality or second authored fact. In a graph expression, `Relation//NAME` references a canonical Relation model name or its declared inverse alias model name, whereas `((NAME))` invokes that Relation between endpoints.
### Formal Claim

```CFEL
# model
Operator//Alias == "alias(Relation//RELATION_NAME) == \"notation token\""
```

