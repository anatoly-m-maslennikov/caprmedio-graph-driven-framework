---
subjects:
  governs: Entity/Aspect/Engineering/Authoring/Controlled English
  depends_on:
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - Entity/Object/Continuant/Actor
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 37
updated_at: 2026-10-29 14:12:43 +0400
relations:
  child_of:
  - CA-M-111
  - CA-M-112
  - CA-R-941
atom_id: CA-M-113@37
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
---
## Summary

Write Claims in CAPRMEDIO Controlled English

## Claim scope

Claim authoring **in** CAPRMEDIO Controlled English **and** canonical naming **in** authored CAPRMEDIO content.

## Claim

**to** write one Claim **in** CAPRMEDIO Controlled English, the Author **must** satisfy **all** of the following:

- use the controlled English subset of the identified CCE version.
- name **every** necessary participant **and** relation explicitly.
- state **every** necessary modality, quantity, condition, **and** boundary explicitly.
- resolve the entity **and** its full canonical name for **every** named Subject Graph component **or** target **and** **every** source-declared Relation Type named inside `((...))` **before** authoring a mention of it; use the exact full word **or** phrase established by its active Entity Definition Atom. report an unresolved **or** conflicting binding rather than choose a synonym **or** infer an entity from matching spelling alone.
- use the same exact full canonical name **in** **all** authored mentions of the same entity, including entity names, Claims, Claim Scope, Semantics, Details, instructions, descriptions, **and** explanations. do **not** introduce another full name for stylistic variation **or** use the same full canonical name for a different entity. properties, values, bearers, contexts, **and** registered synonyms provide no exception **to** this rule.
- read **every** reusable component Term's explicit authoritative Requirement Atom of Type Term Definition directly **and** use its declared meaning consistently **in** **every** composition. agreement among Entity Definitions **or** their Semantics does **not** define a component Term. report a missing, ambiguous, **or** conflicting Term Definition **without** inventing its meaning. reuse of a Term **in** different full names is **not** a naming collision **when** its meaning remains consistent. a Term **may** also constitute a complete entity name; do **not** infer a new graph entity from a component Term alone.
- treat repeated references **to** the same entity as repeated uses of its canonical name, **not** duplicate entities. resolve an existing-kind reference payload **to** that entity **without** creating an alias **or** a separate naming object. require source-defined Relation Type authority for a name inside `((...))`; successful parsing alone does **not** admit its meaning **or** Relation Type.
- keep syntax symbols, delimiters, **and** selector keywords distinct from entity names. resolve the separately named entities using the registered `/`, `//`, `.`, `:`, **and** `>` constructs, the existing-kind reference `@(...)`, **and** the source-defined Relation Type named inside `((...))` under CA-R-1931 **and** CA-R-2244. preserve an admitted complete qualified property name, such as `atom.id` **or** `projection.id`; its dot remains syntax **and** does **not** create an entity by itself. under CA-R-1325, an arbitrary complete composite expression does **not** automatically become another full canonical name **or** entity.
- resolve the effective CCE Role Profile under CA-M-308-CORE_META_MODEL-CORE-METHOD--resolve-the-effective-cce-role-profile **and** satisfy that profile under CA-M-315-CORE_META_MODEL-CORE-METHOD--validate-claims-against-effective-cce-role-profiles.
- choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning.
- exclude ambiguous pronouns, anaphora, ellipsis, unstated defaults, **and** mixed logical groupings.
- make the content understandable under CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand **and** render Terms **and** CCE Operators under CA-M-229-CORE_META_MODEL-IMPLEMENTATION_METHOD--render-governed-terms-and-cce-operators-distinctly.

## Details

Every in-scope entity has exactly one full canonical word or phrase, and every such canonical name identifies exactly one entity. Direct use of Entity Definitions and explicit Term Definitions requires no lookup table, generated dictionary, or semantic Projection. These authoring instructions do not establish implementation or naming-migration evidence.

The naming domain covers every authoritative Subject Graph entity and every declared Relation Type entity, named or unnamed. It is not restricted to primary kinds: property, value, bearer, context, and instance entities receive no naming exception. Full canonical names, not reusable component Terms, map one-to-one to entities. The graph connects entities; a component Term does not require another graph entity or a synthetic Term node. Existing collisions are not resolved merely by applying this authoring Method.

The reusable Term `Package` occurs in the full names `Package`, `Eval Package`, and `Runtime Package`. The reusable Term `Unit` occurs in `Scope Unit` and `Code Unit`. These uses are permitted with consistent component meanings. They do not make the different full names synonyms or require a graph entity named `Unit`.

For `Package > Module > Code Unit`, the chain connects three entities whose canonical names are `Package`, `Module`, and `Code Unit`. Correct authored prose: “The Module contains a Code Unit.” Calling that same Module a “component” is incorrect. `Component` may name a separately defined different entity; its spelling alone does not establish that entity or a synonym. The complete chain is a structured expression, not another entity or dictionary entry. No code identifier, path, or quoted external source text is renamed automatically.

The complete qualified property names `atom.id` and `projection.id` use the same `id` component meaning: a unique identifier used to find an entity instance. This meaning applies across Continuant and Occurrent instances, with uniqueness bounded by matching identifier prefixes. The distinct spellings `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` do not by themselves establish lifecycle state or other semantics. Their meaning comes from explicit defining authority.
