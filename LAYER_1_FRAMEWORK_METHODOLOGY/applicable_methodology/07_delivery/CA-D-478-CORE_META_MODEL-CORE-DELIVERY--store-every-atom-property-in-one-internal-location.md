---
subjects:
  governs: "Entity/Node/Continuant/Atom.Property"
  depends_on:
    ["Entity/Node/Continuant/Atom.Property", "Entity/Carrier/File Carrier", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Summary", "Entity/Relation"]
version: 9
updated_at: "2026-10-19 15:55:56 +0400"
relations: {"delivery_for": ["CA-R-1598"], "relates_to": ["CA-D-479", "CA-D-268", "CA-R-1470"]}
atom_id: "CA-D-478"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md
  source_atom_id: CA-D-478
  source_atom_revision: 9
  source_sha256: f0be16fa21b1cce785a8dacd55fd50ad2db63b0beee6bd1c96152c49e47b3483
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Store every Atom Property in one internal location

## Scope

applicable Atom Properties and their canonical internal locations.

## Claim

**every** applicable Atom Property **must** have **`=1`** canonical internal location assigned by its Delivery authority:

- use YAML Frontmatter **unless** that Property is assigned **to** a named Main Content section.
- use the named section as the sole value source **when** Main Content carries the Property; do **not** maintain the same Property again **in** frontmatter.
- names, filename tokens, **and** placement are representations checked against the internal value under CA-D-480, **not** alternative authority.
- Atom-to-Atom Relations follow their registered owning direction under CA-D-268; do **not** copy inverse **or** transitive Relations **to** make an Atom self-sufficient.
- the retired top-level fields `cce_version`, `cce_form`, **and** `llm_session_ids` are **not** admitted Atom Properties **and** **must not** be serialized **in** an Atom Carrier. their absence is conforming; their presence is a retired-field finding, **not** a reason **to** select legacy authority. this rule does **not** remove session provenance from its separately governed Journal Carrier.

## Details
