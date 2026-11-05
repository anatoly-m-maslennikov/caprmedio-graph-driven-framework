---
atom_id: CA-R-2276
ref_id: CA-R-2276@7-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL
  dependencies:
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
version: 7
updated_at: 2026-11-04 18:25:15 +0400
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2276@7-draft-RULE--require-one-to-one-canonical-entity-names-with-reusable-terms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Require one-to-one canonical entity names with reusable Terms

## Claim

### Prose Claim

Every entity represented in the Subject Graph, every declared Relation Type entity, and every authored occurrence mentioning one of those entities in CAPRMEDIO Controlled English.

**every** entity represented **in** the Subject Graph **and** **every** declared Relation Type entity **must** have exactly one complete canonical name formed from reusable Terms and any applicable registered qualification syntax, and every authored occurrence **must** use that name consistently. Each complete name **must** identify exactly one entity; distinct complete names **must not** identify the same entity, and the same complete name **must not** identify distinct entities.

A complete name is the exact source-admitted expression for its entity. It may be short, including a single Term spelling, only when governing authority admits that exact expression as the complete name of exactly one entity. Being a reusable Term alone does not make it an entity name. No special root exception applies.

## Details

The naming domain includes every named Subject Graph entity, including Properties, allowed-value entities, named instances, and Relation Type entities. A missing complete name fails the exactly-one condition. No bearer, scope, value-domain, or context exception permits two distinct complete names for one entity.

Reusable Terms may appear in different complete names. `Package` appears in `Package`, `Eval Package`, and `Runtime Package`; `Unit` appears in `Scope Unit` and `Code Unit`. Reuse does not create another entity or make the complete expressions synonymous. `Package <+ Module <+ Code Unit` connects three entities; check the complete name and source Declaration for each endpoint entity. The whole chain is not a fourth entity name.

A Relation token inside `((...))` resolves through the Current direct Relation registry to one admitted Relation Type. Its bare token spelling is not necessarily that Relation Type's complete canonical name; compare the full admitted expression separately. Writing a token does not admit an undefined Relation Type.

Qualified expressions and contextual spellings such as `atom.id` and `projection.id` retain their admitted meanings. The dot and Relation operators are syntax, not Terms. Qualification must be admitted for its exact context; admission in one context does not transfer to another. Literal quotations and code identifiers are not automatically renamed.

Canonical identity comes from governing source authority, not spelling, path position, or display placement. Repeated references to one entity use its same complete name and do not create duplicate entities. A dedicated Method Term Definition remains the authority for a reusable Term's lexical meaning; no dictionary, lookup service, synthetic inference, or Terms Graph implementation is required.
