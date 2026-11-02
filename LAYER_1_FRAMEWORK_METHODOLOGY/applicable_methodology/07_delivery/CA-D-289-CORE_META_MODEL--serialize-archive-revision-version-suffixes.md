---
subjects:
  governs: "Entity/Carrier.Canonical Address.Segment"
  depends_on:
    - "Entity/Node/Continuant/Atom.Version Number"
version: 13
updated_at: "2026-10-20 17:07:35 +0400"
relations: {}
atom_id: "CA-D-289"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-289-CORE_META_MODEL--serialize-archive-revision-version-suffixes.md
  source_atom_id: CA-D-289
  source_atom_revision: 13
  source_sha256: 37825a9b828fe2015f2fa5eadf54f233091def0529cbf5c79060ec865403c8f0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Archive Revision Version Suffixes

## Scope

Archive Carrier basenames for Archived Atom versions.

## Claim

**every** Archived Atom Carrier basename **must** append `@<version>` immediately **before** its file extension **when** one exists; the suffix value is that Atom version's Version Number.

## Details
