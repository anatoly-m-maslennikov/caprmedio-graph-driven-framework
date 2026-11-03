---
atom_id: CA-R-2486
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
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

### Prose Claim

Each graph Relation, direct or derived, has exactly one Requirement / Declaration in the selected effective MODEL. A direct Relation Declaration owns its shared meaning, allowed Host and Target signature, endpoint conditions, Direct classification and each declared inverse/counterpart binding. Each derived Relation retains its own Declaration. Infer its reversed endpoints, meaning, Derived classification and source binding from the direct Declaration; do not duplicate them on the derived side. Its Formal Claim contains the reverse written view of its counterpart binding and its own lexical alias when one exists. Relation-object endpoints use qualified addresses `Relation//NAME`; the middle `((HAS_INVERSE))` is the graph Relation operator. An endpoint reference does not execute that Relation as an operator.

A Relation endpoint is a declared model Entity or declared instance, including Carrier and CFEL descriptors. Literal values and operator glyphs are not graph endpoints. Untyped endpoint-signature variables range over this declared entity-or-instance universe and exclude literals. Typed selectors retain their declared populations and conditions. A signature constrains admissible links; it does not create links. An unresolved endpoint population is a diagnostic, not proof of an empty or valid signature. NARROWER_THAN is restricted to MODEL kinds; this rule introduces no further cross-layer endpoint restriction.

`alias(Relation//RELATION_NAME) == "token"` binds one declared Relation's exact name to one nonempty notation token. It is lexical metadata, not a graph Relation between a literal and a Node, and does not equate Relation identities. A Relation has at most one authored alias. No alias means full named notation. Resolve names exactly; case folding and undeclared name synonyms are not admitted. Reject unknown names, conflicting aliases and ambiguous token bindings in the selected effective MODEL. Directional reading follows the owning Declaration; an alias does not authorize a new direction.

The direct Declaration records `Relation//DIRECT ((HAS_INVERSE)) Relation//DERIVED`, equivalently `Relation//DIRECT <--> Relation//DERIVED`. A no-alias derived Declaration records `Relation//DERIVED <((HAS_INVERSE)) Relation//DIRECT`, the reverse written view of that same binding fact. Each side names a distinct declared Relation. After normalizing written direction, the canonical Host is the direct source and the canonical Target is its derived inverse. Infer inverse links only from admitted direct facts by swapping endpoints. Reject a self-pair, multiple direct sources for one inverse, a derived canonical Host and conflicting counterpart bindings. A qualified counterpart retains the qualification at its direct source and is derived only from matching facts.

`Host ((R)) Target` is the named forward view. `Target <((R)) Host` is reverse writing of that same fact. Normalize endpoint counts with the written endpoints. Neither reverse writing nor an inverse binding grants permission, cardinality or a second authored fact. Each direction still needs its own applicable outgoing permission and bounds. Matching and counting use exact Host, Relation, Target and model/instance selectors.
