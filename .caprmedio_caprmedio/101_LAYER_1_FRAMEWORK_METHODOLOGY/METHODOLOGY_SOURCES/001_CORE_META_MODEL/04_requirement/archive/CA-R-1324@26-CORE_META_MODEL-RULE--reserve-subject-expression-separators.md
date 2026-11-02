---
subjects:
  governs: Entity/Term.Name
  depends_on:
  - Entity
version: 26
updated_at: 2026-10-30 16:01:54 +0400
relations: {}
atom_id: CA-R-1324@26
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Reserve Subject Expression Separators

## Claim scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain unescaped `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, `((`, `))`, `@`, `(`, `)`, `[`, `]`, `{`, or `}`. These are reserved Subject Expression syntax for specialization or instances, Property and allowed-value qualification, containment, classification, named Relations, calls to already declared Entities, logical grouping, direct-value Format, or cardinality. A backslash escapes a literal operator character in a name; this Rule does not ban such escaped literal name characters or invent a quote DSL. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an instance that already exists or is explicitly introduced by applicable defining authority under its separate naming/source authority. Syntax alone neither creates nor admits the instance. The lowercase `atom` keyword and its selector punctuation remain registered initial-selector syntax under CA-R-1321, not a broadened Term-name policy.
