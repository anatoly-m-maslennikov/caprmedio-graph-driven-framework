---
subjects:
  governs: "Structural Entity Direct Containment"
  depends_on:
    ["Containment Relation Pair", "Directory Carrier Nesting"]
version: 16
updated_at: "2026-10-20 00:10:46 +0400"
relations: {}
atom_id: "CA-D-264"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-264-CORE_META_MODEL-DELIVERY--derive-direct-containment-from-the-nearest-directory-carrier.md
  source_atom_id: CA-D-264
  source_atom_revision: 16
  source_sha256: 70b1dc6ef553ed18970e1e2b5ff49eb5a7f53046e811608aadd498b2af5cdf4b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Direct Containment from the Nearest Directory Carrier

## Scope

Artifact Revisions whose canonical Carriers are nested below Directory Carriers.

## Claim

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive **`=1`** direct `IS_CONTAINED_BY` connection to the Structural Entity Revision carried by its nearest ancestor Directory Carrier **and** the reverse `CONTAINS` view from that connection.

## Details

For this Carrier-derived view, canonical nesting supplies the fact; the view does not create a second authored relation declaration. IS_CONTAINED_BY is the child-to-parent direction, and CONTAINS is its derived inverse. Reading or refreshing the inverse view does not edit the containing entity's carrier; when that entity is an Atom, it does not create a new Version for it. Physical nesting does not silently replace the logical parent declared by Project Structure under CA-R-1660. Existing Revision/Structural Entity wording is retained for the separate content migration.
