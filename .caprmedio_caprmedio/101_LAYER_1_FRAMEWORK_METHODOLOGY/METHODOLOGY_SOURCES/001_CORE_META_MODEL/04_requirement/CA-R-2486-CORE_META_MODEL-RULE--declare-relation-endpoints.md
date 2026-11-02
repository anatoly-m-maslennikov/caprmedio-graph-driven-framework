---
atom_id: CA-R-2486
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Requirement)/(.Form := Declaration)
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---

## Summary

Declare Relation endpoints

## Claim

Each named Relation, including each Derived Relation view, has exactly one Requirement / Declaration in the selected effective MODEL. Its Declaration states its meaning in Semantics, the allowed Host and Target, and its Direct or Derived Derivation classification. State the short notation when one exists and each source-backed counterpart Relation; otherwise use the full named Relation notation.

A Relation endpoint may be any declared model Entity or an instance of a declared model Entity, including Carrier and CFEL entities. Literal values are not Relation endpoints. Use the most specific admitted endpoint selectors and retain any further source-supported endpoint conditions in Semantics.

In a Relation Declaration endpoint signature, an untyped `$host` or `$target` ranges over declared model Entities and their instances in the selected effective MODEL. Other untyped variable names in that signature follow the same rule. These signature variables do not imply a Node root. A signature constrains which links are admissible; it does not create links or assert a link for every matching pair. An unresolved endpoint population cannot establish an empty or valid signature.

A Derived Relation Declaration identifies the source Relation using `IS_DERIVED_RELATION_OF`. When the derived Relation is an inverse, also bind the canonical Relation to its inverse using `HAS_INVERSE`; the inverse swaps Host and Target and describes the same fact, not a second authored fact. A derived direction has its own Declaration; its use still requires its own applicable permission and cardinality. Neither an inverse binding nor a displayed reverse view grants permission or a cardinality.

The bare `Host ((R)) Target` is the named forward view. `Target <((R)) Host` is the reverse written view of the same canonical fact. Counts remain attached to their written endpoints when the views are normalized to Host and Target. This notation does not create another Relation or authored fact.

When a Relation has an admitted short Subject notation, its Declaration states exactly one nonempty short-notation value using the Relation metadata binding. When no short notation is admitted, omit that value and use the full named Relation notation. The value is scalar; it does not create a separate Atom Content Property or nested Property. Equivalent directional written views do not constitute additional authored short-notation values.
