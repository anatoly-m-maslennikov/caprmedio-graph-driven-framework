---
subjects:
  governs: Subject
  depends_on:
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Atom
version: 25
updated_at: 2026-10-24 14:40:49 +0400
relations: {}
atom_id: CA-R-1321@25
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary
Define Subject Expression

## Scope
Subject Expressions formed from Term references **and** registered relation syntax.

## Claim

a Subject Expression **means** a reference **to** **`=1`** Subject Target formed from Term references, registered relation syntax, **and** an optional registered Atom-owner selector. `Atom` remains the case-significant Entity type **and** ordinary Term component; lowercase `atom(...)` is a distinct case-significant selector keyword, **not** an alias **or** spelling of `Atom` and **not** another Entity kind. Only an approved-profile expression may begin with `atom(content_role="<exact Content Role>")` **or** `atom(content_role="<exact Content Role>",type="<exact Atom Type>")`; `type` has no standalone form. Selector literals are non-empty, double-quoted exact literals with no escaping, evaluation, wildcard, alias, or case folding. **every** ordinary named component other than the RHS instance name following `//`, including `Atom`, Property names, and named allowed values, references a Term; that RHS is the existing instance's name under its separately governed naming/source authority, not automatically a Term. the selector keyword, keys, punctuation, and literals are syntax, **not** Terms. `/`, `//`, `.`, and `:` are registered syntax; `@` is outside Subject syntax. `//` is recognized as one separator token and separates a kind component from the following named-instance component. Its right operand is the existing instance's name, not an Atom ID. The complete expression must still resolve **to** **`=1`** existing canonical Subject Target; syntax neither creates nor admits that target or any EntityGraph relation fact. Selector syntax neither enumerates Atom rows nor admits an Entity endpoint; the canonical Subject target rule remains separate. the expression identifies the target, **not** the Atom's Subject Relation **to** it.

## Details

Subjects do not carry Atom or Artifact IDs, whether bare, version-qualified,
or embedded in an ID selector. Use typed Relations for links to those Atoms
or Artifacts. A property topic such as `Atom.ID` or `Projection.ID` remains
valid: it names the property, not a particular identifier value. Named-instance
Subjects continue to use names, not IDs. Source/provenance metadata outside
Subjects is not prohibited by this rule.
