---
subjects:
  governs: Entity/Node/Continuant/Atom.Property
  depends_on:
  - Entity/Node/Continuant/Atom.Property
  - Entity/Node/Continuant/Atom.Summary
  - Entity/Node/Continuant/Atom.ID
  - Subject/Domain/Node/Continuant/Atom.Status
  - Entity/Carrier/File Carrier
version: 9
updated_at: 2026-10-23 03:06:32 +0400
relations: {"relates_to": ["CA-D-478", "CA-D-282", "CA-D-466"]}
atom_id: CA-D-480@9
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 11
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
