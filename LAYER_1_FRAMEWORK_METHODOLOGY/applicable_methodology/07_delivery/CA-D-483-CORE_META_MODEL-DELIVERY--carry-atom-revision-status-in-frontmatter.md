---
subjects:
  governs: "Entity/Node/Continuant/Atom.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom.Status", "Entity/Node/Continuant/Atom/Content Role", "Entity/Node/Continuant/Atom/Type", "Entity/Carrier.Canonical Address"]
version: 10
updated_at: "2026-10-19 15:55:58 +0400"
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
  source_atom_revision: 10
  source_sha256: 9b03493d8cc669da7aaad704b8250a5846a1e3205e709c97c3f56137b34fbfb6
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
