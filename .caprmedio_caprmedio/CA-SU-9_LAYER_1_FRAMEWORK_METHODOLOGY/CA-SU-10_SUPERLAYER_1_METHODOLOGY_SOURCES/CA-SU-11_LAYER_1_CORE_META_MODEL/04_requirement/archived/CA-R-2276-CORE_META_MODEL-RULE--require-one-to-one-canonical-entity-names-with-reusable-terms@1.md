---
atom_id: CA-R-2276
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity
  depends_on:
  - Entity/Object/Continuant/Term
  - Entity/Aspect/Engineering/Authoring/Controlled English
version: 1
updated_at: 2026-10-29 14:12:43 +0400
relations: {}
tier: 1
---
## Summary

Require one-to-one canonical entity names with reusable Terms

## Claim scope

Every entity represented in the Subject Graph, every declared Relation Type entity, and every authored occurrence mentioning one of those entities in CAPRMEDIO Controlled English.

## Claim

**every** entity represented **in** the Subject Graph **and** **every** declared Relation Type entity **must** have **`=1`** complete canonical name formed from reusable Terms **and** any applicable registered qualification syntax **and** used exactly **in** **every** authored occurrence that mentions it; **every** such complete name **must** identify **`=1`** entity, distinct complete names **must not** identify the same entity, **and** the same complete name **must not** identify distinct entities.

## Details

The Operator first requested no synonyms, then distinguished entities from their reusable lexical Terms and confirmed that complete canonical names map one-to-one to entities. `Package` is reused in `Package`, `Eval Package`, and `Runtime Package`; `Unit` is reused in `Scope Unit` and `Code Unit`. The later accepted `atom.id` and `projection.id` are distinct complete qualified property names with the reusable Term `ID`. This latest distinction replaces the earlier Term/entity bijection. Shared components and terminal labels do not collide when the complete qualified names differ.

The naming domain includes all graph entities, including property, allowed-value, and named-instance entities and entities lacking a complete canonical name. A missing name fails the exactly-one condition. There is no bearer, scope, value-domain, or context exception for a distinct complete qualified name. A relation name inside `((...))` is the exact complete canonical name of its declared Relation Type entity; writing a name does not admit an undefined Relation Type.

`Package > Module > Code Unit` connects three entities whose complete names are `Package`, `Module`, and `Code Unit`. These exact names recur in every authored mention of the respective entities. The complete chain is not one Term or one entity name. A Term can coincide with an entity's complete name; composition need not introduce a second entity named by each component or a separate `Unit` node.

Qualification belongs to the complete name used for collision checks. Thus `atom.id` and `projection.id` are not renamed to `atom.atom_id` or other invented spellings. The dot remains an operator. Likewise, identical local instance labels under distinct source-established kind qualification do not imply identical complete names. An arbitrary composite expression is not automatically one entity name or one Term. This rule does not register grammar: operators, reference markers, cardinality, and relation notation retain the meanings adopted under CA-R-1931 and CA-R-2244.

Canonical identity is established by governing authority rather than spelling, path position, context, or display placement. Repeated references use the same complete canonical name and do not create duplicate entities. Literal source quotations and code identifiers are distinguishable from authored entity mentions and are not automatically renamed. Arbitrary instance names and IDs outside this modeled-entity naming role do not automatically become lexical definitions.

The dedicated Term Definition Requirement Atom owns a Governed Term's approved meaning. No dictionary Projection, extractor, lookup service, synthetic entity inference, or Terms Graph implementation is required. The accepted ID examples add no lifecycle identity semantics.
