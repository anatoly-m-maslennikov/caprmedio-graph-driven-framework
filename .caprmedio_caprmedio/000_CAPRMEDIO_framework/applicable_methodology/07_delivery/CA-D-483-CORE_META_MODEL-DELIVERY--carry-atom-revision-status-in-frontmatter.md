---
subjects:
  governs: "Entity/Continuant/Node/Atom.Status"
  depends_on:
    ["Entity/Continuant/Node/Atom.Status", "Entity/Continuant/Node/Atom/Content Role", "Entity/Continuant/Node/Atom/Type", "Entity/Carrier.Canonical Address"]
version: 9
updated_at: "2026-10-18 03:34:52 +0400"
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
  source_atom_revision: 9
  source_sha256: 219491e0f20de4c3315723732506ca337f9482d9957e0178b1dec3dcb4fc35dc
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
