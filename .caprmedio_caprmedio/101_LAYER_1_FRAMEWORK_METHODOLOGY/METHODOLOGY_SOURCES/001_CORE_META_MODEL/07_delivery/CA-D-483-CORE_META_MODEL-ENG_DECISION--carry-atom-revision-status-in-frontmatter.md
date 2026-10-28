---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Type
  - Subject/CAPRMEDIO/Carrier.Canonical Address
version: 19
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-483
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
