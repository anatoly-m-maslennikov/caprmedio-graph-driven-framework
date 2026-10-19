---
atom_id: CA-D-635
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Projection"
  depends_on: ["Entity/Continuant/Node/Projection.ID", "Entity/Continuant/Node/Projection/Type", "Entity/Continuant/Node/Selection", "Entity/Continuant/Node/Scope Unit"]
version: 4
updated_at: "2026-10-18 03:34:55 +0400"
relations:
  depends_on: [CA-R-1943, CA-D-310, CA-D-550]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-635-CORE_META_MODEL-DELIVERY--serialize-projection-identity-and-filenames.md
  source_atom_id: CA-D-635
  source_atom_revision: 4
  source_sha256: 550fb842398210ea5d1fd403ef2d2aa7841ea7fda9dcba411b2cfad0cd4d29de
  original_relations_sha256: b5600af6064319d3ce4bed60f7437c75d9f047b27d3f1c84464f1aab541f0863
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
