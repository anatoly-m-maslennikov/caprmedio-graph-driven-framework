---
atom_id: CA-M-439
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  - CAPRMEDIO_MODEL <+ Actor
version: 4
updated_at: 2026-11-04 18:28:33 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Method
form: Implementation Method
carrier_destination:
  file:
    name: CA-M-439-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-term-definition-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-439-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-term-definition-content.md
  source_atom_id: CA-M-439
  source_atom_revision: 4
  source_sha256: d6026f499bd935f031882daf17964cd00b30425ded370f1d625819d202db4302
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Write Term Definition Content

## Claim

### Prose Claim


Authoring the content of a Method Atom of Type Term Definition for a reusable lexical Term.


**to** write a Term Definition, the Author **must** identify **`=1`** reusable word **or** phrase as its Term **and** write an explicit Claim that establishes that Term's meaning. state the Term's applicable meaning directly; do **not** substitute an inventory of entity uses, agreement among Entity Definitions **or** Semantics, a generated dictionary, **or** an inferred common substring for the defining Claim.

write Claim Scope **to** state the definition's applicability **without** introducing an alternative meaning for the same Term **or** an exception **to** canonical full-name uniqueness. write Semantics **to** explain the declared meaning, necessary distinctions, **and** its consistent composition **when** clarification is needed; do **not** make Semantics the sole carrier of a missing defining Claim. write Details **to** record source support **and** explanatory examples **without** inventing a second authoritative meaning **or** an entity for a lexical component.

express permitted reuse with the same Term meaning across different full canonical entity names. distinguish the reusable Term from the complete name that identifies **`=1`** canonical entity. outside the Term branch, a Term **must not** alone constitute the complete entity name; the Subject root `Entity` is the sole exception. use the complete admitted expression for every other such entity. preserve exact complete canonical names **in** **all** authored references **to** their entities; repeated references do **not** create entities **or** naming collisions.

use the existing body headings **and** Method authoring conventions. write only the definition content **and** its source-backed explanations; this Method **must not** allocate an entity identity, admit a Relation Type by parsing, invent a part-of-speech schema, require a lookup table **or** Projection, **or** redefine identifier lifecycle semantics from example spelling.

## Details

Term Definition is the dedicated Method Type for lexical meaning and requires its own admitted Type declaration; CA-R-2468's Requirement Type declaration does not establish it. This Method explains how to write definition content; separate Evaluation authority determines how to check definition well-formedness and Term usage. Authoring instructions alone do not prove implementation, source admission, or successful validation.

The lexical forms `Package`, `Eval Package` and `Runtime Package` illustrate reuse of the Term `Package`; `Scope Unit` and `Code Unit` illustrate reuse of `Unit`. They are components of separately admitted full qualified entity expressions, not complete entity names outside the Term branch. Write each component Term's meaning explicitly in its authoritative Term Definition. A component alone does not introduce another entity.

The schematic chain `Entity/Object/Continuant/Package <+ Module <+ Code Unit` connects three entities. Preserve each entity's full source-admitted qualified expression in authored references; a short displayed component alone is not its complete name. Do not replace an admitted Module expression with “component” for stylistic variation. A separately defined entity requires its own full expression and source binding. The complete chain is a structured expression, not automatically another full name or entity.

For the identifier example, write the Term `ID`'s meaning as a unique identifier used to find an entity instance. It applies across Continuant and Occurrent instances; the uniqueness boundary uses matching identifier prefixes. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties using that same meaning. They are not alternative complete canonical Subject names or case-folded aliases; authored Subjects use their full admitted expressions. The dot remains syntax. `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` are spelling examples, not proof of lifecycle semantics. No new case-normalization or alias mechanism is specified by this example.

Existing naming conflicts, missing definitions, unknown coverage, and actual validation outcomes are not resolved by authoring instructions. No automatic code identifier, path, or quoted external source rewrite is authorized.
