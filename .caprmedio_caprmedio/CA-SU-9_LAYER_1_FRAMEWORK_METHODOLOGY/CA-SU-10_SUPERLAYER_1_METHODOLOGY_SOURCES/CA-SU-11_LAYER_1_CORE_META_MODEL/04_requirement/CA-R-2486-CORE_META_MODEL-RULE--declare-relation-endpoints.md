---
atom_id: CA-R-2486
ref_id: CA-R-2486
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
version: 6
updated_at: 2026-11-03 23:25:51 +0400
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2486-CORE_META_MODEL-RULE--declare-relation-endpoints.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Relation endpoints

## Claim

### Prose Claim

Each graph Relation, direct or derived, has exactly one Requirement / Declaration in the selected effective MODEL. A direct Relation Declaration owns its shared meaning, allowed Host and Target signature, endpoint conditions, Direct classification and each declared inverse/counterpart binding. Each derived Relation retains its own Declaration. For a derived inverse bound by HAS_INVERSE, infer its reversed endpoints, shared meaning, Derived classification and source binding from the direct Declaration. Its Formal Claim contains the reverse written view of that HAS_INVERSE binding and its own lexical alias when one exists; do not duplicate the shared meaning on the inverse side. A qualified or other non-inverse derived view instead retains its own source relation, endpoint transformation and qualification; IS_DERIVED_RELATION_OF alone does not imply endpoint reversal or an unconditional inverse. Relation-object endpoints use qualified addresses `Relation//NAME`; the middle `((HAS_INVERSE))` is the graph Relation operator. An endpoint reference does not execute that Relation as an operator.

A Relation endpoint is a declared model Entity or declared instance, including Carrier and CFEL descriptors. Literal values and operator glyphs are not graph endpoints. Untyped endpoint-signature variables range over this declared entity-or-instance universe and exclude literals. Typed selectors retain their declared populations and conditions. A signature constrains admissible links; it does not create links. An unresolved endpoint population is a diagnostic, not proof of an empty or valid signature. NARROWER_THAN is restricted to MODEL kinds; this rule introduces no further cross-layer endpoint restriction.

`alias(Relation//RELATION_NAME) == "token"` binds one declared Relation's exact name to one nonempty notation token. It is lexical metadata, not a graph Relation between a literal and a Node, and does not equate Relation identities. A Relation has at most one authored alias. No alias means full named notation. Resolve names exactly; case folding and undeclared name synonyms are not admitted. Reject unknown names, conflicting aliases and ambiguous token bindings in the selected effective MODEL. Directional reading follows the owning Declaration; an alias does not authorize a new direction.

The direct Declaration records `Relation//DIRECT ((HAS_INVERSE)) Relation//DERIVED`, equivalently `Relation//DIRECT <--> Relation//DERIVED`. A no-alias derived inverse Declaration records `Relation//DERIVED <((HAS_INVERSE)) Relation//DIRECT`, the reverse written view of that same binding fact. Each side names a distinct declared Relation. After normalizing written direction, the canonical Host is the direct source and the canonical Target is its derived inverse. Infer inverse links only from admitted direct facts by swapping endpoints. Reject a self-pair, multiple direct sources for one inverse, a derived canonical Host and conflicting counterpart bindings. A qualified non-inverse view retains the qualification and endpoint transformation in its own Declaration or its explicitly cited governing rule, and is derived only from source facts satisfying that qualification. Its source Relation keeps its general meaning; do not invent HAS_INVERSE for a qualified subset. IS_DECLARED_BY is such a view of GOVERNS qualified by the Requirement/Form Declaration ownership rule.

`Host ((R)) Target` is the named forward view. `Target <((R)) Host` is reverse writing of that same fact. Normalize endpoint counts with the written endpoints. Neither reverse writing nor an inverse binding grants permission, cardinality or a second authored fact. Each direction still needs its own applicable outgoing permission and bounds. Matching and counting use exact Host, Relation, Target and model/instance selectors.
