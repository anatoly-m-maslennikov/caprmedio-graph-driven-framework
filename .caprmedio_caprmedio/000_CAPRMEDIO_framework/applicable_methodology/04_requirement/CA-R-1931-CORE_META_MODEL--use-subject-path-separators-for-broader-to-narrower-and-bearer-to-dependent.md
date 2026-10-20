---
subjects:
  governs: "Subject Path"
  depends_on:
    - "Dependent Entity"
    - "IS_BORNE_BY"
    - "Entity"
version: 2
updated_at: "2026-10-20 04:48:53 +0400"
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
  source_atom_revision: 2
  source_sha256: dde1a6691f7cdc554d7d09ea749cb85b5979bcad0f39e3ee83c8a9d9b03a81a4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent

## Scope

a Subject Path.

## Claim

**in** a Subject Path, `/` **must** separate a broader component from its following narrower component; `//`, recognized as one separator token and **not** two `/` tokens, **must** separate an Entity kind component from the following named instance component; `.` **must** separate a bearer component from its following dependent component; `:` **must** separate a Property component from its following allowed-value component; **and** `@` is **not** Subject syntax. the complete Subject Path still resolves **to** **`=1`** existing canonical target **and** does **not** create target identities. `//` denotes the existing kind-to-named-instance connection, distinct from the Atom's outer Subject Relation. The intended EntityGraph fact is named instance INSTANCE_OF kind, but a projection may assert that fact only under separately authored Core authority; syntax alone does **not** admit it. the mechanical native fact for `.` is Dependent IS_BORNE_BY Bearer; for `:` it is AllowedValue IS_ALLOWED_VALUE_OF Property. `/` admits **no** native Subject **or** Entity relation; any later Terms-Graph binding to NARROWER_THAN remains separately governed.

## Details
