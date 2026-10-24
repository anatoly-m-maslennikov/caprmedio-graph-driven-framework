---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Status
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Status
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom/Type
  - Subject/Engineering/Carrier.Canonical Address
version: 12
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-D-478
  - CA-D-480
  - CA-D-466
  - CA-D-461
atom_id: CA-D-483@12
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
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
