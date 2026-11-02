---
subjects:
  governs: "Term.Name"
  depends_on:
    - "Subject Expression"
version: 14
updated_at: "2026-10-20 04:49:22 +0400"
relations: {}
atom_id: "CA-R-1324"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md
  source_atom_id: CA-R-1324
  source_atom_revision: 14
  source_sha256: 7c7c14e77cef21fe267fcdb4bfb64d1d835bf42f4d595367e41edc4773ac9c52
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reserve Subject Expression Separators

## Scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain `/`, `.`, **or** `:`; `//` is a reserved Subject Expression separator and cannot occur inside a Term name. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an existing instance under its separate naming/source authority. the lowercase `atom` keyword **and** its parentheses, keys, commas, equals signs, **and** quoted literals are registered selector syntax under CA-R-1321, **not** Term characters **or** a broadened Term-name policy; that selector may occur only as the approved initial component. `@` is outside Subject syntax **and** is **not** a Subject Expression separator.

## Details
