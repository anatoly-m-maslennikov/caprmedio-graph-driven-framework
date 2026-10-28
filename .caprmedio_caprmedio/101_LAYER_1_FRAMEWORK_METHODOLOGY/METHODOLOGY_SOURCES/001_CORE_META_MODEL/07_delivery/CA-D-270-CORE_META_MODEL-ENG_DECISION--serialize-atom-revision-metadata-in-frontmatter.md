---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Updated At
version: 24
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-270
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
