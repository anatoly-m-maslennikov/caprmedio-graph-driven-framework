---
atom_id: CA-R-2720
ref_id: CA-R-2720@2-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Operator//Alias
version: 2
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 06:30:39 +0400
carrier_destination:
  file:
    name: CA-R-2720@2-draft-DECLARATION--declare-cfel-operator-alias.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Declare CFEL operator alias

## Claim

### Formal Claim

```CFEL
# model
Operator//Alias == "alias($r) == \"notation token\""
```

### Prose Claim

`alias($r) == "notation token"` takes an already bound Relation participant, such as one selected by `$r[<Relation>, (.Name = RELATION_NAME)]`, and binds that declared graph Relation's exact name to one nonempty lexical notation token in the selected effective MODEL. Resolve the name exactly; do not infer case folding or undeclared synonyms. A Relation has at most one authored alias. Reject undeclared Relation names, conflicting alias values and ambiguous token bindings. Without an alias, use the full named Relation notation.

This CFEL operator binds notation metadata; it does not construct a literal-to-Node graph Relation or equate different Relation identities. The token follows the owning Relation Declaration's directional reading and grants no endpoint permission, cardinality or second authored fact. In a graph expression, an already bound Relation participant references that Relation object as an endpoint, whereas `((NAME))` invokes that Relation between endpoints.
