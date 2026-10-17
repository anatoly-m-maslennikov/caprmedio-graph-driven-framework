---
subjects:
  governs: "Installed Extensions Catalog Entry"
  depends_on:
    ["Extension", "Artifact"]
version: 12
updated_at: "2026-10-15 12:21:13 +0000"
relations: {}
atom_id: "CA-R-1220"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1220-CORE_META_MODEL-REQUIREMENT--require-immutable-installed-extension-candidate-provenance.md
  source_atom_id: CA-R-1220
  source_atom_revision: 12
  source_sha256: 34cfc3327c21646ee737f20b4f6c26a85bb150f7a49b21a52031235384b29835
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require Immutable Installed Extension Candidate Provenance

## Scope

Installed Extensions Catalog Entries and immutable Extension Candidates.

## Claim

**every** Installed Extensions Catalog Entry **must** identify **`=1`** immutable Extension Candidate by stable Identity, Version, Author, Source, Source Version, Origin, **and** Content Digest.

## Details
