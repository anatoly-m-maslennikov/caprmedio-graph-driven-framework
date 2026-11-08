---
atom_id: CA-E-444
ref_id: CA-E-444
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Eval Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Runtime Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package <+ Module
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package <+ Module <+ Code Unit
  - CAPRMEDIO_MODEL <+ Term//Entity
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Project
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Requirement)/(.Header.Form: Entity Definition)'
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Entity
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Terms Graph)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 4
relations:
  evaluation_for:
  - CA-R-1318
  - CA-R-1319
  - CA-R-1320
  - CA-M-125
  - CA-M-113
status: Active
version: 36
updated_at: 2026-11-04 18:28:33 +0400
carrier_destination:
  file:
    name: CA-E-444-EVAL_CASE--validate-project-specific-term-meaning.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-444-CORE_META_MODEL-EVAL_CASE--validate-project-specific-term-meaning.md
  source_atom_id: CA-E-444
  source_atom_revision: 36
  source_sha256: 9974535da11aea3277a93042d40cba4baf0a2fd4781343d46261fddcb0332a7a
  original_relations_sha256: aedddb0c2e1e658dd8ba37ccf7c007a8772a73e688ebf1d07a325ce14a6e7db9
---
## Summary

Validate Project-specific Term meaning

## Claim

### Prose Claim


Project-specific Terms, complete canonical entity names **and** their authored occurrences **in** the selected source Atoms. Ordinary vocabulary without established Project-specific use does **not** require a Term Definition. The check reads source Atoms directly; no dictionary, lookup service **or** generated Projection is a prerequisite.


the Evaluation **must** check selected authoritative Method Atoms of Type Term Definition for well-formedness **and** exactly-one defining authority, **then** check the authored sources **in** this order: entity names, Claim including applicability in Prose Claim, Semantics, Details, **and** other authored fields. It **must** compare Term occurrences with the meaning established by their explicit authoritative Term Definition **and** compare complete entity names with their source-backed canonical entities. Agreement between several Semantics sections **must not** substitute for a Term Definition. The results **must** distinguish well-formedness, source consistency **and** checked coverage, preserve source Atom, Revision **and** exact field occurrence for **every** finding, **and** leave insufficient identity, authority **or** coverage evidence unresolved rather than passed.

## Details

### Source preparation and ordered stages

Before the authored-field stages, read the exact selected Method Atoms of Type Term Definition **and** the governing name/entity authority. A Term Definition is a Method Type for lexical meaning; Entity Definition remains a Requirement Type for entity structure; an Entity Definition **or** repeated descriptive wording alone does **not** own a reusable Term's meaning. Local well-formedness **and** cross-source defining-authority uniqueness are separate checks.

1. Entity names: check complete canonical name-to-entity **and** entity-to-complete-name binding against the explicitly evidenced entity population. Check full Entity expressions in admitted `/`, `//`, `.`, `:`, `+>`, `<+`, `>|` **and** `|<` constructs, qualified references to already declared Entities, **and** registered direct Relation tokens inside `((...))`. A token resolves through the Relation registry to one admitted Relation Type; its bare spelling is not the Relation Type entity's full canonical expression, which is compared separately. A qualified reference refers to an already declared Entity **without** declaring another target; parsing **does not** infer target **or** Relation admission.
2. Claim: compare its authored Term occurrences with the selected Term Definitions **and** its entity mentions with their complete canonical names.
3. Semantics: check the field **when** present. Its explanations cannot redefine a Term **or** replace its explicit Term Definition. An absent optional field is recorded as absent, **not** invented.
4. Details: check its authored occurrences **without** allowing explanatory examples to silently establish another meaning **or** name.
5. Other authored fields: check remaining authored content, including Summary **and** applicable reference fields, **without** skipping them because earlier stages passed. Preserve literal source quotations **and** code identifiers under their governing boundaries; do **not** silently rename them.

Keep each stage's coverage visible. A later conflict remains a finding even **when** an earlier stage passed. A missing required field fails its applicable well-formedness check; the remaining accessible content can still be reviewed **without** claiming that the field exists.

### Test cases

- provide one well-formed authoritative Term Definition **and** consistent authored uses; one source with a different Content Role **or** Method Type; a missing Term Definition; two active Term Definitions for the same Term with agreeing meanings; **and** two with conflicting meanings. distinguish the local Atom-shape result from the cross-source authority result.
- place a contradictory Term use separately **in** entity names, Claim including applicability in Prose Claim, Semantics, Details **and** another authored field. Keep the other fields correct **so** each ordered stage is exercised. Include an error **in** a later field after earlier fields pass.
- include ordinary vocabulary **without** evidence of Project-specific meaning; a dictionary-only restatement of ordinary meaning; sentence-initial capitalization; names, identifiers, paths **and** syntax tokens; **and** a case whose classification **or** source coverage is uncertain. Include a missing definition outside a filtered source selection. Neither capitalization **nor** absence from that filter establishes missing defining authority.
- include two distinct complete canonical entity names for one evidenced entity; one complete canonical name for two distinct entities; an exact one-to-one mapping; repeated references to one name/entity binding; **and** a known entity with zero complete canonical names under complete naming-source coverage. Keep missing naming separate from missing Entity Definition **and** missing Term Definition.
- use full Entity expressions `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package/Eval Package`, and `Entity/Object/Continuant/Package/Runtime Package` with one consistent reusable Term `Package`; use `Entity/Object/Continuant/Structural Unit/Scope Unit` and `Entity/Object/Continuant/Package <+ Module <+ Code Unit` with one consistent reusable Term `Unit`. Outside the Term branch, only the root `Entity` may be expressed by one Term alone.
- use `Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package <+ Module`, and `Entity/Object/Continuant/Package <+ Module <+ Code Unit`: three connected entities with their three full expressions in graph Subjects and all authored mentions. Calling the same Module entity `component` merely for stylistic variation fails; a separately defined Component entity stays distinct.
- accept `Entity` as the complete expression only for the Subject root Entity, and keep its distinct lexical Term target `Term//Entity` separate when that Term is explicitly defined. Reject a single Term component such as `Package` as the complete expression for another Entity outside the Term branch.
- use the qualified Atom segment `Atom/(.Header.Role: X)/(.Header.Form: X)` as a fixture: component reuse passes only when governing authority independently admits exact `X` as the Role and as the Form in that qualified context. A companion fixture with missing Form-in-Role admission fails. The fixture text itself neither admits an `X` entity nor supplies either value's authority.
- use a registered direct Relation token inside `((...))`, an unregistered alternate token asserted to name that same Relation Type, **and** readable syntax for an unadmitted Relation. Verify the registered token's registry resolution separately from the Relation Type entity's full canonical expression. Do **not** infer Relation admission **or** endpoint permissions from the notation.
- use `atom.id` **and** `projection.id` as contextual topic/code spellings for distinct ID Properties with the explicitly defined ID meaning. They are not alternative complete canonical Subject names; authored Subjects use their full admitted expressions. The dot is syntax. The check **must not** require `atom.atom_id` **or** `projection.projection_id`, invent another entity for the dot **or** the component Term, **or** apply unspecified case folding.
- check an explicit ID Term Definition whose meaning is a unique identifier used to find an entity instance, including Continuant **and** Occurrent instances. Apply uniqueness **only** within matching identifier prefixes. Use `CA-P-123`, `CA-P-123@1-draft` **and** `CA-P-123@3` as carried strings **without** inventing their version-identity relationships. If such relationships **or** a prefix equivalence are needed but undeclared, retain an unresolved condition.
- include an exact source occurrence missing its Atom Revision, unsupported semantic certainty, an invented graph edge, **and** a faithful optional diagnostic that reports a source conflict. No graph **or** diagnostic is required to run these source checks.
- select one Current Method Atom **and** record its source Atom, exact Revision **and** actual GOVERNS target as the direct Subject-target fixture. Verify that exact target against its governing admission **and** classification evidence separately from component-Term meaning. The Method Role, carrier name **or** folder spelling **must not** establish the target's category **or** an independent lexical definition. Include a Term's wording substituted for an actual Subject reference **and** a complete composite Subject Path classified as one Term.

### Acceptance criteria and outcomes

A well-formed Term Definition with exactly one active authoritative owner supports the checked Term meaning. Duplicate active Term Definitions fail defining-authority uniqueness even **when** their Claims agree; conflicting meanings additionally fail source consistency. Agreement among Semantics sections, consistent use, spelling **or** capitalization alone does **not** establish a Term Definition. An evidence-backed Project-specific use with missing defining authority fails **only** with complete checked definition coverage for its declared authority boundary; incomplete **or** filtered coverage leaves that claim unresolved. Ordinary vocabulary is **not** failed merely because it lacks a Term Definition.

Consistent reuse of component Terms passes. Source evidence of two full names for one entity **or** one full name for distinct entities fails canonical naming; property, value, bearer **or** context qualification does **not** excuse reuse of the same complete name for distinct entities. Repeated references to one established entity are **not** collisions. A known entity with no complete canonical name fails missing naming **when** population **and** naming-source coverage are established. Unknown population, entity identity **or** required coverage remains unresolved. Do **not** fabricate a Term, name, Definition **or** entity distinction to obtain a pass.

`Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package <+ Module`, and `Entity/Object/Continuant/Package <+ Module <+ Code Unit` identify three entities. Operators, delimiters and selector syntax are not Terms. Under CA-R-1325, a complete composite Subject Expression is not one lexical Term; this does not prohibit an explicitly admitted qualified Entity expression. Outside the Term branch, only root `Entity` may be expressed by one Term alone. Parsing an arbitrary composite expression does not automatically establish a complete Entity expression or another Entity. The three-target chain introduces no fourth Entity or fourth complete expression. Naming checks must not reify component labels or shared words into new graph entities. The respective ID Properties distinguished by the contextual topic/code spellings `atom.id` and `projection.id` stay distinct and retain the explicitly defined ID meaning; these spellings do not substitute for full admitted Subject expressions. An Atom Content Role/Type expression requires independent source admission of both exact values. A Term occurrence is checked against its dedicated Term Definition, not inferred agreement of other fields.

A direct GOVERNS **or** DEPENDS_ON Subject Relation **must** resolve its canonical source-backed target; the Relation **and** its target remain distinct. Term wording cannot substitute for that exact reference. The selected Method fixture preserves its actual GOVERNS target **and** exact source Revision; target classification follows governing target authority, **not** the Method Role **or** carrier spelling. A source target's admission does **not** by itself establish a component Term's meaning authority; these checks retain their separate outcomes.

Every finding identifies source Atom, exact Revision, logical field, occurrence span **or** exact passage, governing Term Definition **and** relevant compared source. A missing required source **or** unperformed stage is a coverage gap, **not** a pass. Well-formedness, source consistency **and** coverage remain separate; the combined result cannot pass **if** a required check fails **or** remains unresolved. A faithful optional diagnostic **may** accurately report failed **or** unresolved source conditions, but its fidelity does **not** establish source validity. No independent generated vocabulary authority, extra lookup operation **or** special Projection is needed.

### Failure disposition

retain the precise conflicting **or** missing source evidence **and** report the affected Term, canonical entity name, source Atom, Revision **and** authored field. distinguish a malformed Term Definition, duplicate defining authority, a conflicting use, missing naming **and** incomplete coverage. Do **not** rename sources, merge entities, invent a definition **or** treat a diagnostic's faithful output as a source pass.

