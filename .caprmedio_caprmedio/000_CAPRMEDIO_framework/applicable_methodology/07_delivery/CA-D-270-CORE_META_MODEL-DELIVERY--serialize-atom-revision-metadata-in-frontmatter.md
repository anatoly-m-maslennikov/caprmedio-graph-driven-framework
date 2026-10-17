---
subjects:
  governs: "Entity/Continuant/Object/Atom"
  depends_on:
    ["Entity/Continuant/Object/Atom.Version Number", "Entity/Continuant/Object/Atom.Updated At"]
version: 15
updated_at: "2026-10-15 18:50:45 +0000"
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
  source_atom_revision: 15
  source_sha256: e7de622b7bacc8caca4c68225c5c8e6a6334a06ae60a0c2becae662aacb16768
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
