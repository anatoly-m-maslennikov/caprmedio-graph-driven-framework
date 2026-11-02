---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Author
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Operator Registry
version: 28
updated_at: 2026-10-29 07:17:24 +0400
relations: {}
atom_id: CA-D-274@28
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Explicit Atom Revision Author

## Scope

Markdown Atom Carriers.

## Claim

a Markdown Atom Carrier **must** serialize **`=1`** resolved Author as the top-level frontmatter Property `author`; apply the applicable Author default during authoring rather than leaving the accepted Revision dependent on an omitted Author.

- encode `author` as **=1** nonempty YAML string equal **to** a name **in** the Project's Operator registry under CA-D-494, **not** a list **or** a null value.
- validate Author by exact registry membership. an unlisted name fails membership; unavailable **or** invalid registry context leaves the check incomplete. do **not** require an additional Actor identity lookup **or** copy the registered role into Atom frontmatter.

## Details
