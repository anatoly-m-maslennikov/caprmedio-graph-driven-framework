---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom.ID"]
version: 21
updated_at: "2026-10-20 21:17:02 +0400"
relations: {}
atom_id: "CA-D-288"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary
Serialize Draft Atom Filenames with an Empty Number

## Scope
Project-owned Draft Atom filenames.

## Claim

**every** Project-owned Draft Atom filename **must** begin with `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>` **before** its mutable components. When `atom_id` is omitted, use the existing empty-number form `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>--`. When a Draft Atom ID is carried, the filename **must** carry that exact Draft-only marker in the identity segment before the mutable components, as specified by CA-D-378.

## Details

### Draft Atom Identity

Draft filenames follow the optional marker forms under CA-D-378 and CA-D-446; when `atom_id` is carried, the filename remains aligned with that exact Draft marker.
