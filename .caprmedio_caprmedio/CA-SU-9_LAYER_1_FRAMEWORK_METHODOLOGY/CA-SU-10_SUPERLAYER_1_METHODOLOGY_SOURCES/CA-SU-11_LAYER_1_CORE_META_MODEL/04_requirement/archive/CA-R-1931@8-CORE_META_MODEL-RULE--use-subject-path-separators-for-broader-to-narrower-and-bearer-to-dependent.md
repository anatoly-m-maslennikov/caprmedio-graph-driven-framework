---
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Term//Dependent Entity
  - 'Subject/Graph/Relation/Type: IS_BORNE_BY'
  - Subject/Domain/Node
version: 8
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
atom_id: CA-R-1931@8
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Use Subject Path Separators for Broader-to-Narrower and Bearer-to-Dependent

## Scope

a Subject Path.

## Claim

**in** a Subject Path, `/` **must** separate a broader component from its following narrower component; `//`, recognized as one separator token and **not** two `/` tokens, **must** separate an Entity kind component from the following named instance component; `.` **must** separate a bearer component from its following dependent component; `:` **must** separate a Property component from its following allowed-value component; **and** `@` is **not** Subject syntax. the complete Subject Path still resolves **to** **`=1`** existing canonical target **and** does **not** create target identities. `//` denotes the existing kind-to-named-instance connection, distinct from the Atom's outer Subject Relation. The intended EntityGraph fact is named instance INSTANCE_OF kind, but a projection may assert that fact only under separately authored Core authority; syntax alone does **not** admit it. the mechanical native fact for `.` is Dependent IS_BORNE_BY Bearer; for `:` it is AllowedValue IS_ALLOWED_VALUE_OF Property. `/` admits **no** native Subject **or** Entity relation; any later Terms-Graph binding to NARROWER_THAN remains separately governed.

## Details
