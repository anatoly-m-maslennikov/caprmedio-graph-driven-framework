---
subjects:
  governs: Subject/Engineering/Extension
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit//INSTALLED_EXTENSIONS
  - Subject/Domain/Node/Continuant/Term//Artifact
version: 18
updated_at: 2026-10-24 22:06:39 +0400
relations: {}
atom_id: CA-R-1220@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Require Immutable Installed Extension Candidate Provenance

## Scope

Installed Extensions Catalog Entries and immutable Extension Candidates.

## Claim

**every** Installed Extensions Catalog Entry **must** identify **`=1`** immutable Extension Candidate by stable Identity, Version, Author, Source, Source Version, Origin, **and** Content Digest.

## Details
