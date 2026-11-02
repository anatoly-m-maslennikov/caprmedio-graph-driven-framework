---
subjects:
  governs: "Entity/Node/Continuant/Atom"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Entity/Carrier", "Entity/Carrier/File Carrier", "Entity/Node/Continuant/Atom.Property", "Entity/Node/Continuant/Project"]
version: 10
updated_at: "2026-10-19 15:55:52 +0400"
relations: {"relates_to": ["CA-R-1957", "CA-R-1956", "CA-D-416"]}
atom_id: "CA-D-463"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-463-CORE_META_MODEL-CORE--give-every-atom-revision-one-authoritative-carrier-bundle.md
  source_atom_id: CA-D-463
  source_atom_revision: 10
  source_sha256: 818848212a67fa829578e6b991059c41bbe4ad962e67220f300c9c5402a664c2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Give Every Atom Revision One Authoritative Carrier Bundle

## Scope

Atom Revision Authoritative Carrier Bundles.

## Claim

**every** Atom Revision **must** have **`=1`** authoritative Carrier Bundle on the Project filesystem containing **`=1`** Markdown File Carrier **and** **`>=0`** additional Carriers admitted by its applicable Delivery authority.

the Markdown file carries the Atom's own Properties under CA-D-478 **and** CA-D-479. additional Carriers represent that same Revision **without** replacing the mandatory file **or** independently redefining its Properties.

## Details
