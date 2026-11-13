---
atom_id: CA-R-2486
ref_id: CA-R-2486
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form
    := Declaration)
tier: 3
status: active
version: 7
updated_at: '2026-11-13T01:37:28.860798+00:00'
carrier_destination:
  file:
    name: CA-R-2486-CORE_META_MODEL-RULE--declare-relation-endpoints.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Relation endpoints

## Claim

### Prose Claim

Each canonical Relation and each qualified derived Relation has exactly one Requirement Declaration in the effective MODEL. The canonical Declaration owns its shared meaning, allowed Host and Target signature, endpoint conditions, Direct classification and any inverse alias binding. The inverse alias uses that Declaration as its source. Its Derived classification, reversed endpoints and lexical alias follow from the declared binding. A qualified derived Relation keeps its own Declaration for its source, endpoint transformation and qualification.

A Relation endpoint is a declared model Entity or declared instance, including Carrier and CFEL descriptors. Literal values and operator glyphs are not graph endpoints. Untyped endpoint-signature variables range over this declared entity-or-instance universe and exclude literals. Typed selectors retain their declared populations and conditions. A signature constrains admissible links; it does not create links. An unresolved endpoint population is a diagnostic, not proof of an empty or valid signature. NARROWER_THAN is restricted to MODEL kinds; this rule introduces no further cross-layer endpoint restriction.

`alias(Relation//RELATION_NAME) == "token"` binds one declared Relation's exact name to one nonempty notation token. It is lexical metadata, not a graph Relation between a literal and a Node, and does not equate Relation identities. A Relation has at most one authored alias. No alias means full named notation. Resolve names exactly; case folding and undeclared name synonyms are not admitted. Reject unknown names, conflicting aliases and ambiguous token bindings in the selected effective MODEL. Directional reading follows the owning Declaration; an alias does not authorize a new direction.

The canonical Declaration records the reverse alias. `Relation//DIRECT ((HAS_INVERSE)) Relation//REVERSE` and `Relation//DIRECT <--> Relation//REVERSE` state that binding. `Relation//REVERSE ((IS_INVERSE_ALIAS_FOR)) Relation//DIRECT` states it from the alias address. Reject self-pairs, multiple canonical sources for one alias, a derived canonical Host and conflicting bindings. A qualified derived Relation keeps its qualification and endpoint transformation in its own Declaration or cited governing Rule. IS_DECLARED_BY is such a view of GOVERNS, qualified by Requirement Declaration ownership.

`Host ((R)) Target` is the named forward view. `Target <((R)) Host` is reverse writing of that same fact. Normalize endpoint counts with the written endpoints. Neither reverse writing nor an inverse binding grants permission, cardinality or a second authored fact. Each direction still needs its own applicable outgoing permission and bounds. Matching and counting use exact Host, Relation, Target and model/instance selectors.