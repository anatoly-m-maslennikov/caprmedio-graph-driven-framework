---
atom_id: "CA-D-635@draft"
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Projection"
  depends_on: ["Entity/Continuant/Projection.ID", "Entity/Continuant/Projection/Type", "Entity/Continuant/Selection", "Entity/Continuant/Object/Scope Unit"]
version: 3
updated_at: "2026-10-16 12:03:44 +0000"
relations:
  depends_on: [CA-R-1943, CA-D-310, CA-D-550]
---
# Summary

Serialize Projection identity and filenames

## Scope

Projection Markdown File Carriers.

## Claim

Use this filename:

`<PROJECT_PREFIX>-PROJ-<ID>-<CURRENT_SCOPE_NAME>--<PROJECTION_TYPE>--<NAMED_SELECTION>.md`

Store the full Projection ID as `projection_id` in YAML frontmatter. The filename and frontmatter must identify the same Projection.

## Details

For this Project, the prefix is `CA`. For example:

`CA-PROJ-001-CORE_META_MODEL--Entities-Graph--Current-Atoms.md`

Its full Projection ID is `CA-PROJ-001`; `001` is the ID segment in the filename. Use the current Scope Unit name, not its label.

The YAML frontmatter carries:

- `artifact_form: Projection`
- `projection_id`: the full Projection ID.
- `type`: Projection Type.
- `named_selection`: the named source selection.
- `source_of_truth`: an unambiguous reference to the authoritative source set.
- `updated_at`: the latest completed rebuild time under CA-D-310.
- `sources`: contributing Atom references with Versions, such as `CA-R-123@3`. Identify contributing non-Atom sources separately; do not invent Atom IDs for them.

Keep the ID under CA-R-1943 when rebuilding or changing only the Scope Unit name or Carrier path. Filename changes do not by themselves create a new Projection.

Type-specific Delivery rules define the body and any additional source evidence. Store the Carrier under the applicable Projection root under CA-D-550.
