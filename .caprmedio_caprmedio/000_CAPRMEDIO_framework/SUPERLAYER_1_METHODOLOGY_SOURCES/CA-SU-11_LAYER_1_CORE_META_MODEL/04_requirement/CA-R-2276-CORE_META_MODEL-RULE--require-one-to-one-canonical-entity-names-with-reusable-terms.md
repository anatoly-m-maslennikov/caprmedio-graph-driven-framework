---
atom_id: CA-R-2276
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Term
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
version: 6
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
tier: 1
role: Requirement
form: Rule
---
## Summary

Require one-to-one canonical entity names with reusable Terms

## Claim scope

Every entity represented in the Subject Graph, every declared Relation Type entity, and every authored occurrence mentioning one of those entities in CAPRMEDIO Controlled English.

## Claim

**every** entity represented **in** the Subject Graph **and** **every** declared Relation Type entity **must** have **`=1`** complete canonical name formed from reusable Terms **and** any applicable registered qualification syntax **and** used exactly **in** **every** authored occurrence that mentions it. **every** such complete name **must** identify **`=1`** entity, distinct complete names **must not** identify the same entity, **and** the same complete name **must not** identify distinct entities. Outside `Term`, the complete canonical name **must** be the full admitted expression, **not** a single registered Term; the Subject root `Entity` is the sole exception.

## Details

The Operator first requested no synonyms, then distinguished entities from their reusable lexical Terms and confirmed that complete canonical names map one-to-one to entities. `Package` is reusable across the lexical forms `Package`, `Eval Package`, and `Runtime Package`; `Unit` is reusable across `Scope Unit` and `Code Unit`. These are lexical forms and components, not assertions of complete canonical entity names outside `Term`. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties and reuse the Term `ID`; they are not alternative complete canonical Subject names or case-folded aliases. This latest distinction replaces the earlier Term/entity bijection. Shared components and terminal labels do not collide when the complete qualified expressions differ.

The naming domain includes all graph entities, including property, allowed-value, and named-instance entities and entities lacking a complete canonical name. A missing name fails the exactly-one condition. There is no bearer, scope, value-domain, or context exception for a distinct complete qualified name. A Relation token inside `((...))` resolves through the current direct Relation registry to exactly one admitted Relation Type under the registered named-Relation notation. The token is not an assertion that its bare spelling is that entity's complete canonical name; complete-entity-name comparison uses the full qualified expression. Writing a token does not admit an undefined Relation Type.

`Package <+ Module <+ Code Unit` connects three entities. Its labels are not assertions of the complete canonical names of entities outside `Term`; an authored reference to one specific entity uses that entity's full qualified expression admitted by its defining authority. The complete chain is not one Term or one entity name. Component reuse does not introduce a second entity named by each component or a separate `Unit` node.

Qualification belongs to the full admitted expression used for entity-name collision checks. The contextual spellings `atom.id` and `projection.id` remain unchanged; they are not renamed to `atom.atom_id` or other invented spellings. The dot remains an operator. `Atom/(.Content Role: X)/(.Type: X)` is a possible qualified expression: it reuses the registered Term `X` in separately qualified value contexts, and governing authority must admit `X` separately in each context. This does not make `X` the complete canonical name of an entity outside `Term` or transfer admission between contexts. Likewise, identical local instance labels under distinct source-established kind qualification do not imply identical complete names. An arbitrary composite expression is not automatically one entity name or one Term. This rule does not register grammar: operators, reference markers, cardinality, and relation notation retain the meanings adopted under CA-R-1931 and CA-R-2487.

Canonical identity is established by governing authority rather than spelling, path position, context, or display placement. Repeated references use the same complete canonical name and do not create duplicate entities. Literal source quotations and code identifiers are distinguishable from authored entity mentions and are not automatically renamed. Arbitrary instance names and IDs outside this modeled-entity naming role do not automatically become lexical definitions.

The dedicated Term Definition Method Atom owns a Governed Term's approved meaning. No dictionary Projection, extractor, lookup service, synthetic entity inference, or Terms Graph implementation is required. The accepted ID examples add no lifecycle identity semantics.
