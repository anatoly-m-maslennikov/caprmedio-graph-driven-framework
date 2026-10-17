---
subjects:
  governs: "Entity/Continuant/Object/Atom.Status"
  depends_on:
    ["Entity/Continuant/Object/Atom.Status", "Entity/Continuant/Object/Atom/Content Role", "Entity/Continuant/Object/Atom/Type", "Entity/Carrier.Canonical Address"]
version: 8
updated_at: "2026-10-16 12:09:37 +0000"
relations: {"relates_to": ["CA-D-478", "CA-D-480", "CA-D-466", "CA-D-461"]}
atom_id: "CA-D-483"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-483-CORE_META_MODEL-DELIVERY--carry-atom-revision-status-in-frontmatter.md
  source_atom_id: CA-D-483
  source_atom_revision: 8
  source_sha256: e8994d2fff6bdc8fdf584ed9e9398c4e9ef1841d12ae7fd58412427e8ab3db3e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Carry Atom Revision Status in frontmatter

## Scope

the Status property carried by an Atom Revision.

## Claim

**every** Atom Revision **must** carry **`=1`** explicit `status` value **in** its own Markdown frontmatter.

- the value **must** belong **to** the applicable Content Role **and** Type Status model.
- placement **must** agree under CA-D-466 **and** its specific Delivery rules; it is **not** a second Status source.
- another Revision **or** a containing Hub **must not** override this Revision's carried Status.

- encode `status` as **=1** nonempty YAML string using the exact value admitted by the selected Status model. do **not** accept a list, null, **or** another Revision's value as this Revision's Status.

## Details
