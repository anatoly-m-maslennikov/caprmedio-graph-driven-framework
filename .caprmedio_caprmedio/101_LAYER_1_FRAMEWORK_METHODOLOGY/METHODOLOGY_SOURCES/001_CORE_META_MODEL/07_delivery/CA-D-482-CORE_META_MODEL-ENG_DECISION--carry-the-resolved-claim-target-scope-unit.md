---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Target Scope Unit
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Atom.Author
  - Subject/Graph Node/Domain/Continuant/Atom.Target Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Local Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom
version: 20
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-D-482
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Carry the resolved Claim Target Scope Unit

## Scope

the frontmatter representation of an Atom's resolved Claim Target Scope Unit.

## Claim

a Markdown Atom Carrier **must** carry its resolved Claim Target Scope Unit **in** frontmatter, including a Current-scope Atom whose target is its own Scope Unit.

- choose the current Scope Unit as the default during authoring, **not** by relying on the file's later location.
- a carried target equal **to** the current Scope Unit does **not** make the Atom Relational. a different target still requires the applicable Relational Atom admission.
- Claim Scope restrictions use the body sections under CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections; the RMED Scope section does **not** replace **or** duplicate `claim_target_scope_unit`.

- encode this Property as the top-level nonempty YAML string `claim_target_scope_unit`, resolving **to** **=1** registered Scope Unit. null, lists, **and** a duplicated `claim_scope` field are **not** this encoding.
- an external Requirement of Type Project Goal carries its Operator Actor owner using the existing Author fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter **in** `current_scope_unit`, **and** the Project **in** `claim_target_scope_unit`. This is the explicit Actor-owner exception, not a Project-owned Atom with incidental Actor provenance. Do **not** register the Operator as a Scope Unit **or** infer either value from the filename.

## Details
