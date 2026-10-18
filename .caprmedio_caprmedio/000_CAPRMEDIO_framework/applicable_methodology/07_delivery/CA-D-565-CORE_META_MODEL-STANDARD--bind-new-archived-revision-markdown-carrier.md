---
subjects:
  governs: "Entity/Continuant/Node/History/Revision"
  depends_on:
    ["Entity/Continuant/Node/Atom.Status", "Entity/Continuant/Node/Atom.Status: Archived", "Entity/Carrier.Canonical Address"]
version: 5
updated_at: "2026-10-18 03:34:54 +0400"
relations: {"relates_to": ["CA-D-289", "CA-D-466"]}
atom_id: "CA-D-565"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-565-CORE_META_MODEL-STANDARD--bind-new-archived-revision-markdown-carrier.md
  source_atom_id: CA-D-565
  source_atom_revision: 5
  source_sha256: e1fafc6f9a845084a4e20e8ee8a946830ecc0bb613ff0a810609048d102992a1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Bind new archived Revision Markdown Carrier

## Scope

The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.

## Claim

**when** an Atom Revision newly attains its model-admitted `Archived` Status **and** no more-specific applicable Delivery mapping exists for its Artifact Type, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed at `archived/<basename>@<version>.md`: `archived/` follows CA-D-466's Status fallback **and** `@<version>` follows CA-D-289.

## Details

This is a binding of the existing generic Status-placement and Archive-basename rules, not a universal placement override. A more-specific admitted Delivery mapping takes precedence. It neither relocates nor reclassifies an existing immutable legacy `archive/` Carrier, and it does not settle placement for a Revision without the stated newly archived Markdown Carrier.
