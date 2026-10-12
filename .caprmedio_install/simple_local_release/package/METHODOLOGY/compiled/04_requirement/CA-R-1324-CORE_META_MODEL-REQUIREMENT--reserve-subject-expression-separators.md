---
subjects:
  governs: "Term/name"
  depends_on:
    - "Subject Expression"
version: 12
updated_at: "2026-10-11 18:04:47 +0400"
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
  source_atom_revision: 12
  source_sha256: 33cbfee9844ba4dd895ae6745121fd5db5793a20aab27eb8b8d7b4591e7fb9a3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reserve Subject Expression Separators

## Scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain `/`, `.`, **or** `:`. the lowercase `atom` keyword **and** its parentheses, keys, commas, equals signs, **and** quoted literals are registered selector syntax under CA-R-1321, **not** Term characters **or** a broadened Term-name policy; that selector may occur only as the approved initial component. `@` is outside Subject syntax **and** is **not** a Subject Expression separator.

## Details
