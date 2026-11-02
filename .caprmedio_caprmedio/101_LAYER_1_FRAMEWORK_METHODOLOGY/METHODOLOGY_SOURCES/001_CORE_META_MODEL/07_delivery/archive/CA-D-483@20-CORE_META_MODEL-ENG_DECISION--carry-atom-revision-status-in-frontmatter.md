---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Status
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Status
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Governing Objects/Atom/Type
  - Entity/Carrier.Canonical Address
version: 20
updated_at: 2026-10-29 07:17:26 +0400
relations: {}
atom_id: CA-D-483@20
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
