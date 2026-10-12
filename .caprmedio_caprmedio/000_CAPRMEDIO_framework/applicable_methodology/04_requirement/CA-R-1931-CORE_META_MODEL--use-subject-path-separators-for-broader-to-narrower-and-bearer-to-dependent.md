---
subjects:
  governs: "Subject Path"
  depends_on:
    - "Dependent Entity"
    - "IS_BORNE_BY"
    - "Entity"
version: 1
updated_at: "2026-10-11 03:56:26 +0400"
relations: {}
atom_id: "CA-R-1931"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1931-CORE_META_MODEL--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md
  source_atom_id: CA-R-1931
  source_atom_revision: 1
  source_sha256: f11bc913a0f7b31abc746a86599eaeaa76db8be412568ef4c34f68c7d01525c8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent

## Scope

a Subject Path.

## Claim

**in** a Subject Path, `/` **must** separate a broader component from its following narrower component; `.` **must** separate a bearer component from its following dependent component; `:` **must** separate a Property component from its following allowed-value component; **and** `@` is **not** Subject syntax. a Subject Path still resolves **`=1`** canonical target **and** does **not** create target identities. the mechanical native fact for `.` is Dependent IS_BORNE_BY Bearer; for `:` it is AllowedValue IS_ALLOWED_VALUE_OF Property. `/` admits **no** native Subject **or** Entity relation; any later Terms-Graph binding to NARROWER_THAN remains separately governed.

## Details
