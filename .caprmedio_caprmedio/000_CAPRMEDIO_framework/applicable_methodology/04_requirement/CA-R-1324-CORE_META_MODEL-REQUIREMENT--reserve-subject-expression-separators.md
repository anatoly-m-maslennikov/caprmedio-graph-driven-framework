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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-REQUIREMENT--reserve-subject-expression-separators.md
  source_atom_id: CA-R-1324
  source_atom_revision: 13
  source_sha256: 9fa9571ff5f6c6bc0d01c2b7724cd9ed197a4df82b3e66a53d3f0bb56781a866
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reserve Subject Expression Separators

## Scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain `/`, `.`, **or** `:`. the lowercase `atom` keyword **and** its parentheses, keys, commas, equals signs, **and** quoted literals are registered selector syntax under CA-R-1321, **not** Term characters **or** a broadened Term-name policy; that selector may occur only as the approved initial component. `@` is outside Subject syntax **and** is **not** a Subject Expression separator.

## Details
