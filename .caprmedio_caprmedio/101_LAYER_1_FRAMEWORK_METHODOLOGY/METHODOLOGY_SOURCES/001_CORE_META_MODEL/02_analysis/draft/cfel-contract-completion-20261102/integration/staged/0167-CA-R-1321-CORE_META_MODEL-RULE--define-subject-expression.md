---
subjects:
  active: CFEL
  passive:
  - Entity
  - Term
  - Term//Property
  - Atom
  - Package
  - Entity/Object/Continuant/Package <+ Module
  - Entity/Object/Continuant/Package <+ Module <+ Code Unit
version: 35
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1321
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Define Subject Expression

## Claim scope

Subject Expressions formed from entity names, reusable Term components, and registered relation syntax.

## Claim



The following interpretation is required when this governed concept is used:

a Subject Expression **means** a reference **to** **`=1`** canonical Subject Target formed from entity names, registered relation syntax, **and** an optional registered Atom-owner selector. The case-significant lexical component `Atom` occurs **in** the full canonical Entity expression `Entity/Object/Continuant/Governing Objects/Atom`; lowercase `atom(...)` is a distinct case-significant selector keyword, **not** an alias **or** spelling of `Atom` **and not** another Entity kind. Only an approved-profile expression **may** begin with `atom(content_role="<exact Content Role>")` **or** `atom(content_role="<exact Content Role>",type="<exact Atom Type>")`; `type` has no standalone form. Selector literals are non-empty, double-quoted exact literals with no escaping, evaluation, wildcard, alias, or case folding. The reserved selector form is initial `atom(...)`; this does not reserve an ordinary noninitial Name `atom`.

Outside the Term branch, an Entity reference **must** use its exact complete canonical expression with every source-established qualifier; a bare Term is not that expression. The sole one-Term exception is the Subject root `Entity`. Ordinary lexical components **may** reuse Terms with consistent approved meanings; an instance's name is **not** automatically a lexical Term. Inside `((...))`, a registered direct Relation token resolves to **`=1`** admitted Relation Type under the named-Relation notation. Its bare spelling is not that Relation Type entity's complete canonical expression; naming comparison uses the full qualified expression separately. The selector keyword, keys, punctuation, **and** literals remain syntax, **not** entities **or** additional canonical names merely because they occur **in** an expression. A qualified Atom expression such as `Atom/(.Content Role: <exact Content Role>)/(.Type: <exact Atom Type>)` is available only when both exact values have independent source admission; its segments do not become admitted merely by appearing in selector syntax.

`/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, `@`, parentheses, the named-relation form `Source ((RELATION_TYPE)) Target`, **and** cardinality follow CA-R-1931 **and** CA-R-2487. `//` is one separator token between a kind **and** a named instance; its right operand is the instance's name, **not** an Atom ID. `@` calls an already declared Entity; it is **not** an Atom-version selector or kind-only reference. Parentheses provide logical grouping. `Part +> Whole` and `Whole <+ Part` are containment, not inheritance or sequence. `X >| Y` and `Y |< X` express the same HAS_CLASSIFICATION fact with Entity Y used as an applicable Classification axis, not membership or a new Entity kind. Relation counts use `Source {:forward}((RELATION)){:reverse} Target`; direct values use `Property{:occurrence}: [format]{:value count}`. Operators, calls, grouping, relation delimiters, Formats, **and** cardinality are **not** Terms.

The complete expression **must** resolve **to** **`=1`** canonical Subject Target that already exists **or** is explicitly introduced by applicable defining authority under CA-R-1194 **and** CA-R-1931. Syntax alone neither creates **nor** admits a target **or** native EntityGraph fact. Selector syntax neither enumerates Atom rows **nor** admits an Entity endpoint. The expression identifies the target, **not** the Atom's Subject Relation **to** it. An arbitrary composite expression is **not** one Term **or** automatically one entity name; an admitted qualified property name **may** identify **`=1`** entity.

## Details

Subjects do not carry Atom or Artifact IDs, whether bare, version-qualified, or embedded in an ID selector. Use typed Relations for links to those Atoms or Artifacts. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties, not particular identifier values. They are not alternative complete canonical Subject names or case-folded aliases; an authored Subject uses its full admitted expression. Their shared terminal label and reusable `ID` meaning do not collide. Dot remains an operator; these contextual spellings are not renamed to `atom.atom_id` or another invented spelling. Named-instance Subjects use names, not IDs. Source/provenance metadata outside Subjects is not prohibited.

`//` selects a named instance of a primary kind, not an instance of a dependent property. A following `.` can select that instance's property, including `Selection//Projection and Journal Authority Sources.updated_at`. Source-established kind or bearer qualification participates in the complete canonical name. Distinct modeled entities require distinct complete qualified names, while repeated references retain the same identity and name. Local instance labels may coincide across different kinds when their complete qualified names differ. Local names remain unique per entity kind within the project's Current source view across owning Scope Units under CA-R-2476. This grammar adds neither case folding nor a name registry. When `//` is mandatory remains deferred.

`Entity/Object/Continuant/Package`, `Entity/Object/Continuant/Package <+ Module`, and `Entity/Object/Continuant/Package <+ Module <+ Code Unit` identify three connected entities. The chain is not one Term or a fourth entity. `Package`, `Module`, and `Code Unit` are their reusable lexical components, not their complete Entity expressions. Likewise, `Package` and `Unit` are reusable Terms whose occurrence does not itself introduce an entity or Relation. The rule applies to exact full expressions in authored prose as well as Subjects. Literal source quotations and code identifiers remain distinguishable and are not automatically renamed. Arbitrary instance names and identifiers outside this modeled-entity naming role are not automatically lexical definitions.

Entity is the canonical expression root under CA-R-1194. The registered operators retain their meanings and native-fact admission boundaries. No new alias, parser, resolver grammar, formula, or unadopted syntax is introduced by this definition.
