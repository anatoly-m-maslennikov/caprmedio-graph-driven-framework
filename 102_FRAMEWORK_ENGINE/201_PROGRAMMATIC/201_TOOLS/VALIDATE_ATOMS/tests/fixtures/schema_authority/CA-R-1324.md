---
subjects:
  governs: "Term.Name"
  depends_on:
    - "Subject Expression"
version: 13
updated_at: "2026-10-15 12:23:50 +0000"
relations: {}
atom_id: "CA-R-1324"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Reserve Subject Expression Separators

## Scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain `/`, `.`, **or** `:`. the lowercase `atom` keyword **and** its parentheses, keys, commas, equals signs, **and** quoted literals are registered selector syntax under CA-R-1321, **not** Term characters **or** a broadened Term-name policy; that selector may occur only as the approved initial component. `@` is outside Subject syntax **and** is **not** a Subject Expression separator.

## Details
