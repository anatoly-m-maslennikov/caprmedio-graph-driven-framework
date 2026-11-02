---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Type
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Label
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Local Order
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Carrier
version: 24
updated_at: 2026-10-31 19:26:58 +0400
relations:
  child_of:
  - CA-D-441
atom_id: CA-D-442@24-draft
content_role: Delivery
form: Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 3
---
## Summary

Encode Scope Unit declaration fields

## Claim scope

The proposed fields and shared Markdown Atom carrier mapping of a Scope Unit Declaration.

## Claim

A Scope Unit Declaration is carried in a Markdown Atom file. The proposed shared Carrier mapping encodes logical Role as `role`, Form as `form`, and the active Subject as `subjects.active`. These keys are proposed adoption targets, not a claim that Current readers have migrated. Normalize the legacy control headers before promotion and coordinate reader cutover separately.

The table preserves facts from the legacy non-root TOML rows. Its names identify the old source fields; it does not prescribe new frontmatter keys, a Markdown layout or duplicate structural properties. Instance Drafts may state these facts in prose. The root Project has no Parent; its identity is sourced from Project Settings. Do not infer missing root Label, order or paths from this non-root table.

| Legacy source field | Non-root Declaration fact and responsibility |
|---|---|
| `scope_unit_name` | required nonempty canonical Scope Unit Name string |
| `parent` | immediate containing Scope Unit; the legacy `PROJECT` sentinel resolves to the named Project root, otherwise use the declared Scope Unit Name in the same Project |
| `scope_unit_type` | required string in (`Ordered`, `Unordered`) |
| `scope_unit_label` | required nonempty canonical Label string, independent of Type |
| `local_order` | required integer only for Ordered units; absent for Unordered units |
| `authority_path` | required nonempty repository-relative directory path string |
| `delivery_path` | required nonempty repository-relative Implementation Folder path string |
| `authority_mode` | optional explicit string in (`strict`, `casual`); absence inherits Framework Instance Settings |

Both path fields use forward slashes and resolve from the repository root, not the carrier location. A trailing slash does not establish another binding. Absolute paths, parent traversal, escaping symlinks, and paths resolving to another Project's control root are invalid. A native Carrier binding under CA-D-445-CORE_META_MODEL-ENG_DECISION--admit-explicit-scope-unit-carrier-bindings may differ from ordinary physical nesting. `structural_level`, `node_id`, `structural_parent`, `child_composition`, `project_boundary_position`, `authority_materialized`, and `numeric_prefix` are not authored fields. Any readable ancestry/path display is derived from `parent` declarations under CA-R-2133 and is not another declaration.

`project_structure.toml` remains the current governing source until an authorized cutover; this Draft neither performs migration nor changes that file.
