---
subjects:
  governs: Term.Name
  depends_on:
  - Subject Expression
version: 15
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1324@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Reserve Subject Expression Separators

## Scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain `/`, `.`, **or** `:`; `//` is a reserved Subject Expression separator and cannot occur inside a Term name. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an existing instance under its separate naming/source authority. the lowercase `atom` keyword **and** its parentheses, keys, commas, equals signs, **and** quoted literals are registered selector syntax under CA-R-1321, **not** Term characters **or** a broadened Term-name policy; that selector may occur only as the approved initial component. `@` is outside Subject syntax **and** is **not** a Subject Expression separator.

## Details
