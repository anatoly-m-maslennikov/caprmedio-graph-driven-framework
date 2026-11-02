---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Structure
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Name
  - Subject/Graph Node/Domain/Continuant/Scope Unit/Type
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Label
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Local Order
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Navigational Order Number
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations:
  child_of:
  - CA-D-441
atom_id: CA-D-442@18
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Encode Scope Unit declaration fields

## Scope

the field signatures and field order of `[[scope_units]]` tables.

## Claim

**every** `[[scope_units]]` table **must** use the following field signatures **and** field order for readable serialization. omission is permitted **only** **where** stated; an empty string **or** copied default **must not** substitute for omission.

| Field | TOML value **and** responsibility |
|---|---|
| `scope_unit_name` | required nonempty canonical Scope Unit Name string |
| `parent` | required string: `PROJECT` for the owning root, **otherwise** a declared Scope Unit Name **in** the same Project |
| `scope_unit_type` | required string **in** (`Ordered`, `Unordered`) |
| `scope_unit_label` | required nonempty canonical Label string, independent of Type |
| `local_order` | required integer **only** for Ordered units; absent for Unordered units |
| `navigational_order_number` | required nonnegative integer, independent of structural Local Order |
| `authority_path` | required nonempty repository-relative directory path string |
| `delivery_path` | required nonempty repository-relative Implementation Folder path string |
| `authority_mode` | optional explicit string **in** (`strict`, `casual`); absence inherits Framework Instance Settings |

both path fields use forward slashes **and** resolve from the repository root, **not** the TOML directory; a trailing slash does **not** establish another binding. absolute paths, parent traversal, escaping symlinks **and** paths resolving **to** another Project's control root are invalid. a native Carrier binding under admitted Delivery authority **may** differ from ordinary physical nesting. `structural_level`, `node_id`, `structural_parent`, `child_composition`, `project_boundary_position`, `authority_materialized`, **and** `numeric_prefix` are **not** authored row fields. Any readable ancestry/path display is derived from `parent` declarations under CA-R-2133 and is not another declaration.

## Details
