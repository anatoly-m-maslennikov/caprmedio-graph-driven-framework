---
subjects:
  governs: "Entity/Node/Continuant/Atom.Property"
  depends_on:
    ["Entity/Node/Continuant/Atom.Property", "Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/Atom.ID", "Entity/Node/Continuant/Atom.Status", "Entity/Carrier/File Carrier"]
version: 8
updated_at: "2026-10-19 15:55:57 +0400"
relations: {"relates_to": ["CA-D-478", "CA-D-282", "CA-D-466"]}
atom_id: "CA-D-480"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-480-CORE_META_MODEL--keep-atom-addresses-consistent-with-carried-properties.md
  source_atom_id: CA-D-480
  source_atom_revision: 8
  source_sha256: 426d921dc6ee566de5bdb8a1808706d3713bf9ffb8db350dfbce9ffdefc3addc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Atom addresses consistent with carried Properties

## Scope

Atom Properties represented by a filename, matching directory name, or placement.

## Claim

**every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.

- compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
- a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
- agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.

## Details
