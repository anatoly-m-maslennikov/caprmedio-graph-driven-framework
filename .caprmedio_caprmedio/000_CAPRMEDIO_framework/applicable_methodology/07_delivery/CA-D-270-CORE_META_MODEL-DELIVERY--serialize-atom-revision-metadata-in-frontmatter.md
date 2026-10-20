---
subjects:
  governs: "Entity/Node/Continuant/Atom"
  depends_on:
    ["Entity/Node/Continuant/Atom.Version Number", "Entity/Node/Continuant/Atom.Updated At"]
version: 17
updated_at: "2026-10-19 15:55:20 +0400"
relations: {}
atom_id: "CA-D-270"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter.md
  source_atom_id: CA-D-270
  source_atom_revision: 17
  source_sha256: 99a0cb4c6fe6bb1875f085a3726a1ab724df74c767d9e7d2333437710141f83a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Atom Revision Metadata **in** Frontmatter

## Scope

Markdown Atom Revision Carriers.

## Claim

**every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.

## Details

- `version` is a YAML integer **>=1**, **not** a Boolean **or** numeric string.
- `updated_at` is a quoted YAML string containing **=1** valid date, time **and** explicit UTC offset. accept the existing `YYYY-MM-DD HH:MM:SS +HHMM` form **and** the equivalent ISO 8601 `YYYY-MM-DDTHH:MM:SSZ` **or** `YYYY-MM-DDTHH:MM:SS+HH:MM` form, including optional fractional seconds. offset signs **may** be positive **or** negative; reject a missing timezone, impossible date, **or** invalid offset.
- lexical differences representing the same instant do **not** alone change Revision identity. this Delivery serializes Updated At; it does not classify whether an edit changes governed meaning.
