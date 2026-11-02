---
subjects:
  governs: "Framework Instance Settings/Carrier/Atom metadata exclusion"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings", "Entity/Node/Continuant/Atom", "Artifact/Revision"]
version: 11
updated_at: "2026-10-19 15:55:38 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-377"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-377-CORE_META_MODEL--exclude-atom-metadata-from-framework-instance-settings.md
  source_atom_id: CA-D-377
  source_atom_revision: 11
  source_sha256: 364facc89f074bfb5d51dc1fe6744ca2de665f3c216906cd97c9e94d3258de92
  original_relations_sha256: dbd41c990ca96026d80a7c6e36e3203724208ce3569ca634233af924bbbfab2f
---
# Summary

Exclude Atom metadata from Framework Instance Settings

## Scope

Atom metadata in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.

## Details
