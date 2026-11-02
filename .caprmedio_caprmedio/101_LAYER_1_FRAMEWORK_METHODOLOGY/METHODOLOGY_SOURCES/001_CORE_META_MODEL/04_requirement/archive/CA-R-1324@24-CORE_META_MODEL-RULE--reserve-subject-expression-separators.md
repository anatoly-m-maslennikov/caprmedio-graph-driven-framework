---
subjects:
  governs: Entity/Object/Continuant/Term.Name
  depends_on:
  - Entity
version: 24
updated_at: 2026-10-29 09:55:37 +0400
relations: {}
atom_id: CA-R-1324@24
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

a Term name **must not** contain `/`, `.`, **or** `:`; `//` is a reserved Subject Expression separator and cannot occur inside a Term name. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an existing instance under its separate naming/source authority. the lowercase `atom` keyword **and** its parentheses, keys, commas, equals signs, **and** quoted literals are registered selector syntax under CA-R-1321, **not** Term characters **or** a broadened Term-name policy; that selector may occur only as the approved initial component. `@(...)` is the existing-kind reference operator in the adopted Entity syntax; it is not part of a Term name and does not declare another Term.

## Details
