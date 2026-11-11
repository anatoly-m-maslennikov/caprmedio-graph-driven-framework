---
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  passive:
  - CAPRMEDIO <+ MODEL <+ Actor
  - CAPRMEDIO <+ MODEL <+ Atom.Content
version: 42
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-442
  - CA-M-112
  - CA-R-941
atom_id: CA-M-113
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-113-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-claims-in-caprmedio-controlled-english.md
  source_atom_id: CA-M-113
  source_atom_revision: 42
  source_sha256: 65ba8f7c3f0ae0e8dcaedf5a23020b9fb8dfcbc206e35aa9d0c11143a319ed73
  original_relations_sha256: 2701bc866cb6ded663ce6728ada8d5991d372b20fe3d8b0d795cc53ee044986b
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
- read **every** reusable component Term's explicit authoritative Method Atom of Type Term Definition directly **and** use its declared meaning consistently **in** **every** composition. agreement among Entity Definitions **or** their Semantics does **not** define a component Term. report a missing, ambiguous, **or** conflicting Term Definition **without** inventing its meaning. reuse of a Term **in** different full names is **not** a naming collision **when** its meaning remains consistent. outside the Term branch, a complete entity name **must** use the full admitted expression **and** **must not** be just one registered Term, except for the Subject root `Entity`; do **not** infer a new graph entity from a component Term alone.
- treat repeated references **to** the same entity as repeated uses of its canonical name, **not** duplicate entities. resolve an `@` call payload **to** that entity **without** creating an alias **or** a separate naming object. require source-defined Relation Type authority for a name inside `((...))`; successful parsing alone does **not** admit its meaning **or** Relation Type.
- keep syntax symbols, delimiters, **and** selector keywords distinct from entity names. resolve the separately named entities using the registered `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, **and** `|<` constructs, `@` calls to already declared Entities, logical grouping `()`, direct-value Format and count markers, the two independent Relation count positions, **and** the source-defined Relation Type named inside `((...))` under CA-R-1931 **and** CA-R-2244. preserve the contextual topic/code spellings `atom.id` **and** `projection.id` for their respective ID Properties. they are not alternative complete canonical Subject names **or** case-folded aliases; authored Subjects use their full admitted expressions. the dot remains syntax **and** does **not** create an entity by itself. under CA-R-1325, an arbitrary complete composite expression does **not** automatically become another full canonical name **or** entity.
- resolve the effective CCE Role Profile under CA-M-308-CORE_META_MODEL-CORE-METHOD--resolve-the-effective-cce-role-profile **and** satisfy that profile under CA-M-315-CORE_META_MODEL-CORE-METHOD--validate-claims-against-effective-cce-role-profiles.
- choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning.
- exclude ambiguous pronouns, anaphora, ellipsis, unstated defaults, **and** mixed logical groupings.
- make the content understandable under CA-M-444-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly **and** render Terms **and** CCE Operators under CA-M-229-CORE_META_MODEL-IMPLEMENTATION_METHOD--render-governed-terms-and-cce-operators-distinctly.

## Details

Every in-scope entity has exactly one full canonical expression formed from reusable Terms and admitted syntax, and every such expression identifies exactly one entity. Outside the Term branch, a complete entity name cannot be just one registered Term; Entity is the sole exception because it is the Subject root. Direct use of Entity Definitions and explicit Term Definitions requires no lookup table, generated dictionary, or semantic Projection. These authoring instructions do not establish implementation or naming-migration evidence.

The naming domain covers every authoritative Subject Graph entity and every declared Relation Type entity, named or unnamed. It is not restricted to primary kinds: property, value, bearer, context, and instance entities receive no naming exception. Full canonical names, not reusable component Terms, map one-to-one to entities. The graph connects entities; a component Term does not require another graph entity or a synthetic Term node. Existing collisions are not resolved merely by applying this authoring Method.

The lexical forms `Package`, `Eval Package` and `Runtime Package` illustrate reuse of the Term `Package`; `Scope Unit` and `Code Unit` illustrate reuse of the Term `Unit`. These forms are components of separately admitted full qualified expressions, not assertions of complete entity names outside the Term branch. Their reuse preserves the same component meanings and introduces no separately admitted entity from a component alone.

The schematic chain `Entity/Object/Continuant/Package <+ Module <+ Code Unit` connects three entities. For a specific authored entity reference, use its complete source-admitted qualified expression rather than one displayed component label. Do not substitute the word “component” as a stylistic alias for an admitted Module expression. A distinct entity requires its own admitted expression; different wording alone supplies neither identity nor synonym authority. The complete chain is a structured expression, not another entity or dictionary entry. No code identifier, path, or quoted external source text is renamed automatically.

The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties using the explicitly defined ID meaning: a unique identifier used to find an entity instance. These spellings do not substitute for full admitted Subject expressions. This meaning applies across Continuant and Occurrent instances, with uniqueness bounded by matching identifier prefixes. The distinct spellings `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` do not by themselves establish lifecycle state or other semantics. Their meaning comes from explicit defining authority.
