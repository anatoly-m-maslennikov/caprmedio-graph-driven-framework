---
version: 27
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-940
  - CA-R-941
  method_for:
  - CA-R-940
  - CA-R-941
  depends_on:
  - CA-R-1273
subjects:
  active: Atom.Content
  passive:
  - Actor
  - Atom.Content.Summary
  - Aspects <+ Engineering <+ Authoring <+ Controlled English
  - Term
atom_id: CA-M-294
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
---
## Summary

Use simpler words without losing meaning

## Claim scope

CAPRMEDIO content wording.

## Claim

**when** choosing wording for CAPRMEDIO content, the Author **must** choose words **and** phrases that are simpler **and** more familiar **to** the intended reader **when** they preserve the intended meaning **without** adding ambiguity.

## Details

- prefer clear everyday wording over unnecessary jargon **or** specialized wording.
- preserve who **or** what the statement concerns, its obligations **or** permissions, quantities, conditions, boundaries, **and** logical distinctions.
- prefer a clear longer phrase over a shorter obscure expression; fewer words do **not** necessarily make the content simpler.
- retain specialized wording **when** replacing it would lose a necessary distinction **or** make the meaning less precise.
- retain exact full canonical entity names, CCE Operators, **and** references. simpler wording does **not** authorize a synonymous alternate full name, another full canonical name for the same entity, use of one full canonical name for another entity, **or** a silent rename. property, value, bearer, context, **and** registered-synonym qualifications do **not** exempt a full-name collision from this prohibition.
- resolve the named entities of Subject Graph expressions **and** the source-declared Relation Types named inside `((...))` **to** their full canonical names **and** preserve those names **in** **all** authored mentions, including entity names, Claims, Claim Scope, Semantics, Details, instructions, descriptions, **and** explanations. repeated references **to** one entity remain repeated uses of its full name. an `@` call payload introduces no entity **or** full-name alias. parsing a named relation does **not** supply its defining authority.
- distinguish reusable component Terms from full canonical entity names. read each component Term's meaning directly from its explicit authoritative Method Atom of Type Term Definition **and** preserve that meaning across compositions; agreement among Entity Definitions **or** Semantics does **not** define the Term. its consistent reuse **in** different full names is **not** a naming collision. outside the Term branch, a complete entity name **must** use its full admitted expression **and** **must not** be just one registered Term; the Subject root `Entity` is the sole exception. do **not** replace a component **within** an established full canonical name for stylistic variation **or** invent a graph entity for that component alone. unknown **or** incomplete defining-source coverage remains unresolved, **not** evidence of a successful check.
- keep syntax symbols, delimiters, **and** selector keywords distinct from entity names. preserve the separate entity names using the registered `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, **and** `|<` constructs, `@` calls to already declared Entities, logical grouping `()`, direct-value Format and count markers, the two independent Relation count positions, **and** a source-defined Relation Type name inside `((...))` under CA-R-1931 **and** CA-R-2244. the contextual topic/code spellings `atom.id` **and** `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names **or** case-folded aliases. authored Subjects use their full admitted expressions; the dot remains syntax. under CA-R-1325, an arbitrary complete composite expression does **not** automatically become another full canonical name, entity, **or** separate Term node.

for a Summary, simplify its wording while preserving its source faithfulness under CA-R-1273; this does **not** require restating the complete Claim.

This Method does not prohibit ordinary English alternatives outside canonical entity naming when the Claim permits them. A Term is a reusable lexical component; the complete canonical word or phrase, not each component Term, has the one-to-one entity binding. Direct source-based use requires no lookup table, generated dictionary, or semantic Projection. These authoring instructions do not establish that existing naming collisions or missing definitions have been repaired.

The naming domain covers every authoritative Subject Graph entity and every declared Relation Type entity, named or unnamed, without property, value, bearer, context, or instance exceptions. The domain includes Relation Types whose names occur inside named-relation expressions.

The schematic chain `Entity/Object/Continuant/Package <+ Module <+ Code Unit` connects three entities. Use each entity's complete source-admitted expression: `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package <+ Module`, and `Entity/Object/Continuant/Package <+ Module <+ Code Unit`. Preserve those full expressions in authored references. Do not replace an admitted Module expression with “component” for simpler wording. A separately defined entity requires its own admitted expression and authoritative binding; do not infer one or treat the complete chain as a fourth entity or dictionary entry. No code identifier, path, or quoted external source text is renamed automatically.

The lexical forms `Package`, `Eval Package` and `Runtime Package` illustrate reuse of the Term `Package`; `Scope Unit` and `Code Unit` illustrate reuse of `Unit`. They are components of separately admitted full qualified entity expressions, not complete entity names outside the Term branch. Their consistent reuse does not make distinct full expressions synonyms or introduce another entity from a component alone.

The respective ID Properties distinguished by the contextual topic/code spellings `atom.id` and `projection.id` retain the explicitly defined ID meaning: unique identifier used to find an entity instance, across Continuant and Occurrent instances, with uniqueness bounded by matching identifier prefixes. These spellings do not substitute for full admitted Subject expressions. Do not infer lifecycle semantics solely from examples such as `CA-P-123`, `CA-P-123@1-draft`, or `CA-P-123@3`.
