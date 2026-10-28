---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Author
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Operator Registry
version: 27
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-274
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
