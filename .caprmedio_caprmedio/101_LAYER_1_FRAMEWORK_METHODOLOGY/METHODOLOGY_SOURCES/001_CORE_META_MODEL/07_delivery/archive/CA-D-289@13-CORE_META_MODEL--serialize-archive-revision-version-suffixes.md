---
subjects:
  governs: "Entity/Carrier.Canonical Address.Segment"
  depends_on:
    - "Entity/Node/Continuant/Atom.Version Number"
version: 13
updated_at: "2026-10-20 17:07:35 +0400"
relations: {}
atom_id: "CA-D-289@13"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Archive Revision Version Suffixes

## Scope

Archive Carrier basenames for Archived Atom versions.

## Claim

**every** Archived Atom Carrier basename **must** append `@<version>` immediately **before** its file extension **when** one exists; the suffix value is that Atom version's Version Number.

## Details
