---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//INSTALLED_EXTENSIONS
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
version: 21
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1220
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
