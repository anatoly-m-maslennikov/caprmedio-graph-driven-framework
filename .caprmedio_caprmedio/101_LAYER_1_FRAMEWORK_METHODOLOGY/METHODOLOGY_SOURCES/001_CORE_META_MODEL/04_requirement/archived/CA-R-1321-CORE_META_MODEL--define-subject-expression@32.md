---
subjects:
  governs: Entity/Graph Syntax
  depends_on:
  - Entity
  - Entity/Object/Continuant/Term
  - Entity/Object/Continuant/Term//Property
  - Entity/Object/Continuant/Governing Objects/Atom
version: 32
updated_at: 2026-10-29 17:09:47 +0400
relations: {}
atom_id: CA-R-1321
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Define Subject Expression

## Claim scope

Subject Expressions formed from entity names, reusable Term components, and registered relation syntax.

## Claim



The following interpretation is required when this governed concept is used:

a Subject Expression **means** a reference **to** **`=1`** canonical Subject Target formed from entity names, registered relation syntax, **and** an optional registered Atom-owner selector. `Atom` remains the case-significant Entity type **and** its canonical name; lowercase `atom(...)` is a distinct case-significant selector keyword, **not** an alias **or** spelling of `Atom` **and not** another Entity kind. Only an approved-profile expression **may** begin with `atom(content_role="<exact Content Role>")` **or** `atom(content_role="<exact Content Role>",type="<exact Atom Type>")`; `type` has no standalone form. Selector literals are non-empty, double-quoted exact literals with no escaping, evaluation, wildcard, alias, or case folding.

**every** named component identifying a modeled entity, including `Atom`, Property names, named allowed values, **and** an RHS named instance following `//`, references that entity's exact complete canonical name with applicable source-established qualification. Ordinary lexical components **may** reuse Terms with consistent approved meanings; an instance's name is **not** automatically a lexical Term. A name within `((...))` references its declared Relation Type entity's exact complete canonical name. The selector keyword, keys, punctuation, **and** literals remain syntax, **not** entities **or** additional canonical names merely because they occur **in** an expression.

`/`, `//`, `.`, `:`, `>`, `@(...)`, the named-relation form `Source ((RELATION_TYPE)) Target`, **and** cardinality follow CA-R-1931 **and** CA-R-2244. `//` is one separator token between a kind **and** a named instance; its right operand is the instance's name, **not** an Atom ID. `@(...)` references an existing kind; it is **not** an Atom-version selector. `>` denotes structural containment, **not** inheritance **or** sequence. Operators, reference markers, relation delimiters, **and** cardinality are **not** Terms.

The complete expression **must** resolve **to** **`=1`** canonical Subject Target that already exists **or** is explicitly introduced by applicable defining authority under CA-R-1194 **and** CA-R-1931. Syntax alone neither creates **nor** admits a target **or** native EntityGraph fact. Selector syntax neither enumerates Atom rows **nor** admits an Entity endpoint. The expression identifies the target, **not** the Atom's Subject Relation **to** it. An arbitrary composite expression is **not** one Term **or** automatically one entity name; an admitted qualified property name **may** identify **`=1`** entity.

## Details

Subjects do not carry Atom or Artifact IDs, whether bare, version-qualified, or embedded in an ID selector. Use typed Relations for links to those Atoms or Artifacts. The accepted property topics `atom.id` and `projection.id` name distinct qualified property entities, not particular identifier values. Their shared terminal label and reusable `ID` meaning do not collide. Dot remains an operator; neither complete name is changed to `atom.atom_id` or another invented spelling. Named-instance Subjects use names, not IDs. Source/provenance metadata outside Subjects is not prohibited.

`//` selects a named instance of a primary kind, not an instance of a dependent property. A following `.` can select that instance's property, including `Selection//Projection and Journal Authority Sources.updated_at`. Source-established kind or bearer qualification participates in the complete canonical name. Distinct modeled entities require distinct complete qualified names, while repeated references retain the same identity and name. Local instance labels may coincide across different kinds when their complete qualified names differ. Local names remain unique per entity kind within the project's Current source view across owning Scope Units under CA-R-2002. This grammar adds neither case folding nor a name registry. When `//` is mandatory remains deferred.

`Package > Module > Code Unit` connects three entities named `Package`, `Module`, and `Code Unit`; the complete chain is not one Term or one entity name. `Package` and `Unit` are reusable lexical components whose occurrence does not itself introduce entities or Relations. The rule applies to exact full names in authored prose as well as expressions. Literal source quotations and code identifiers remain distinguishable and are not automatically renamed. Arbitrary instance names and identifiers outside this modeled-entity naming role are not automatically lexical definitions.

Entity is the canonical expression root under CA-R-1194. The registered operators retain their meanings and native-fact admission boundaries. No `::` operator, new alias, parser, formula, or unadopted syntax is introduced by this definition.
