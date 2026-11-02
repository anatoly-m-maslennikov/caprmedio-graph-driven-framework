---
subjects:
  governs: Entity/Property
  depends_on:
  - Entity
  - Entity/Graph Syntax <+ Relation//IS_PROPERTY_OF
  - Entity/Graph Syntax <+ Format
  - Entity/Graph Syntax <+ Cardinality
  - Entity/Carrier
version: 23
updated_at: 2026-10-30 14:38:47 +0400
relations: {}
atom_id: CA-R-1193@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Property

## Claim scope

Properties and their bearer Relations, representation and declared direct values.

## Claim

A Property is an Entity whose identity depends on its immediate bearer, related to that bearer by IS_PROPERTY_OF. A Property has no separate Carrier of its own. Its governing definition declares the applicable direct-value Format and cardinality, including an explicit zero-direct-value declaration where appropriate. The directed IS_PROPERTY_OF Relations must be acyclic, including no self-loop.

### Formal claim

```text
Entity/Property
Property {1}((IS_PROPERTY_OF)) Bearer
```

## Semantics

The Relation expression is schematic: Property denotes each Property occurrence and Bearer denotes its immediate bearer, using the full admitted Entity expressions in actual references. It does not assert that the Property kind node itself is related to the Entity kind node. IS_PROPERTY_OF runs from the Property occurrence to its bearer, whose identity is required by the Property. Exactly one immediate bearer is constrained in the Formal claim.

Each IS_PROPERTY_OF Relation instance is binary: it connects two endpoint nodes or node instances, the source Property and its target immediate bearer. In `Property {1}((IS_PROPERTY_OF)) Bearer`, the count before the Relation token constrains exactly one outgoing Relation instance of that Type per Property occurrence. A count after the token would independently constrain the reverse count per Bearer; none is specified here. The counts do not count distinct target nodes or Relation arity. A Property may therefore still be the bearer of other Properties. In `property[format]{cardinality}`, the brackets declare the direct-value Format and the suffix counts direct values. These counts are independent: one immediate bearer does not imply one direct value. A zero-direct-value grouping can still have declared child Properties.

Exactly one outgoing Relation does not by itself establish acyclicity: two Properties could otherwise be each other's bearer. The cycle constraint forbids returning to the starting node along one or more directed IS_PROPERTY_OF Relations. It neither creates a transitive Relation fact nor requires a new formula notation.

A bearer may itself be a Property. Nested Property expressions such as `bearer.property.status` therefore remain permitted; each Property occurrence has its own immediate bearer. This definition imposes no blanket prohibition on a Status Property or another independently declared Property. It adds no generic lifecycle/update rule and no additional bearer-qualified-identity rule beyond the Relation meaning and existing admitted expression rules.

The no-separate-Carrier constraint concerns the Property itself. A Definition Atom describing the Property and an Entity referenced by its value remain distinct entities with their own applicable representation rules. Delivery policies determine the Property's location within its bearer's representation.

## Details

The Operator selected Property as the single canonical Term for this concept. This successor records the intended kind target `Entity/Property`; root, lexical-owner and consumer consolidation remains coordinated pending work. It does not silently promote this target or claim the whole packet is now consistent.

The Operator assigned exactly one immediate bearer to the Formal claim, no separate Carrier and direct-value Format/cardinality to Claim, and the ability for a Property to bear another Property to Semantics. The proposed extra identity and lifecycle clauses were not adopted. The former postfix `((IS_PROPERTY_OF)){1}` spelling is superseded by the later two-sided Relation cardinality decision: the Property-to-Bearer count now precedes the token, as `{1}((IS_PROPERTY_OF))`. The exactly-one-bearer constraint itself is unchanged. The Operator subsequently approved prohibiting IS_PROPERTY_OF cycles, including self-loops. This constrains the bearer Relation only; it adds no cycle prohibition for value references or other Relation Types.
