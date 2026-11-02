---
atom_id: CA-M-439
content_role: Method
type: Implementation Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
  depends_on:
  - Entity/Object/Continuant/Term
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Term Definition'
  - Entity/Object/Continuant/Actor
version: 1
updated_at: 2026-10-29 13:50:05 +0400
relations: {}
tier: 3
---
## Summary

Write Term Definition Content

## Claim scope

Authoring the content of a Requirement Atom of Type Term Definition for a reusable lexical Term.

## Claim

**to** write a Term Definition, the Author **must** identify **`=1`** reusable word **or** phrase as its Term **and** write an explicit Claim that establishes that Term's meaning. state the Term's applicable meaning directly; do **not** substitute an inventory of entity uses, agreement among Entity Definitions **or** Semantics, a generated dictionary, **or** an inferred common substring for the defining Claim.

write Claim Scope **to** state the definition's applicability **without** introducing an alternative meaning for the same Term **or** an exception **to** canonical full-name uniqueness. write Semantics **to** explain the declared meaning, necessary distinctions, **and** its consistent composition **when** clarification is needed; do **not** make Semantics the sole carrier of a missing defining Claim. write Details **to** record source support **and** explanatory examples **without** inventing a second authoritative meaning **or** an entity for a lexical component.

express permitted reuse with the same Term meaning across different full canonical entity names. distinguish the reusable Term from the complete name that identifies **`=1`** canonical entity. a Term **may** also constitute an entire full name. preserve exact complete canonical names **in** **all** authored references **to** their entities; repeated references do **not** create entities **or** naming collisions.

use the existing body headings **and** Requirement authoring conventions. write only the definition content **and** its source-backed explanations; this Method **must not** allocate an entity identity, admit a Relation Type by parsing, invent a part-of-speech schema, require a lookup table **or** Projection, **or** redefine identifier lifecycle semantics from example spelling.

## Details

Term Definition is the Requirement Type reserved by CA-R-2229. This Method explains how to write definition content; separate Evaluation authority determines how to check definition well-formedness and Term usage. Authoring instructions alone do not prove implementation, source admission, or successful validation.

The reusable Term `Package` occurs in the full names `Package`, `Eval Package`, and `Runtime Package`; `Unit` occurs in `Scope Unit` and `Code Unit`. Write each component Term's meaning explicitly in its own authoritative Term Definition rather than infer it from those entity names. `Package` can also be a complete entity name. The lexical Term `Unit` does not by itself require a graph entity named `Unit`.

For `Package > Module > Code Unit`, preserve the three complete entity names in authored prose. “The Module contains a Code Unit” preserves them; calling that same Module a “component” as a stylistic variation does not. A separately defined different Component entity requires its own source binding. The complete chain is a structured expression, not automatically another full name or entity.

For the identifier example, write the `ID` / `id` Term's meaning as a unique identifier used to find an entity instance. It applies across Continuant and Occurrent instances; the uniqueness boundary uses matching identifier prefixes. The complete qualified property names `atom.id` and `projection.id` use that same component meaning, while the dot remains syntax. `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` are spelling examples, not proof of lifecycle semantics. No new case-normalization or alias mechanism is specified by this example.

Existing naming conflicts, missing definitions, unknown coverage, and actual validation outcomes are not resolved by authoring instructions. No automatic code identifier, path, or quoted external source rewrite is authorized.
