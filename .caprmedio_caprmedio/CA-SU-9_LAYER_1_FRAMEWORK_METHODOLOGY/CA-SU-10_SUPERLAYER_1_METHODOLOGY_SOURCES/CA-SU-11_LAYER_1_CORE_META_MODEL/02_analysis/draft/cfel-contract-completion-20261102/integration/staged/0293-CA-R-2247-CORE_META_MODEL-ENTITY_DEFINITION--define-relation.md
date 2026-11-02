---
atom_id: CA-R-2247
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Relation

## Claim

Relation defines a reusable directed Relation Type. A Relation Type has a Name
and Meaning. A named Type can connect many endpoint pairs. Direction and
transitivity describe the Type, not one actual edge. CFEL represents this Type
with a `Relation` expression. The expression can name an optional derived
counterpart; it does not make every Relation have one. An actual connection is
the tuple (source, Relation Type, target). Each endpoint is a declared model
entity or instance, including Carrier and CFEL; literal values are operands of
CFEL operators, not Relation endpoints. Persist each direct fact once. The
direct tuple remains the source of any derived view. A separate Relation ID is
not required.


```CFEL
CFEL <+ Relation;
Relation.Name{:1}: [string]{:1};
Relation.Name.*[]{:0};
Relation.Meaning{:1}: [string]{:1};
Relation.Meaning.*[]{:0}
```

## Semantics

Endpoint permissions and Relation cardinalities are declared by the governing
Relation Declarations. This Definition describes the CFEL representation of a
Relation Type; it is notation, not a Graph Relation or an operator, and it does
not create an actual graph edge.

## Details

CFEL can use `((RELATION_TYPE))` where no short notation exists. A named Type
and its endpoint permissions remain separate from each actual source/target
tuple.
