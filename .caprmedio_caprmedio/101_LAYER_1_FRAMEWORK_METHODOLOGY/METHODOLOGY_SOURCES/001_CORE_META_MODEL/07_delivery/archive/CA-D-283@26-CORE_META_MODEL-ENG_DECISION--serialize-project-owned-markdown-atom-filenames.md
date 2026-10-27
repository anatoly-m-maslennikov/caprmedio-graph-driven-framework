---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier.Filename
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Node/Domain/Continuant/Atom.Local Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Node/Domain/Continuant/Atom.Label
version: 26
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-283@26
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
type: Eng Decision
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Project-Owned Markdown Atom Filenames

## Scope

Identified Project-owned Markdown Atom filenames other than Plan filenames governed by CA-D-469.

## Claim

**every** identified Project-owned Markdown Atom filename other than a Plan filename governed by CA-D-469 **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<TIER>][-<LABEL>][-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. When present, the `LABEL` segment uses the Atom's effective Label: its explicit Label when present, otherwise its Type name under CA-R-1594. Normalize that token under CA-D-284; an explicit Label replaces the Type name there and does not change the Atom's Type. **every** same-identity Atom Version **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename **and** serialize its retained Summary under CA-D-282. A Draft filename uses the Draft marker as its Atom-ID segment as specified by CA-D-650. An Archived predecessor uses `<canonical-ID>@<old-version>` exactly once in that segment under CA-D-289; do not append a duplicate version suffix. Existing legacy archive filenames are not normalized automatically. a replacement filename **must** contain the successor Atom ID **and** the successor's Summary Slug; a Summary Slug **must not** be edited independently of its source Summary.

## Details

When present, `TIER` serializes the Atom's stored integer `tier`, without a named rank or semantic class. Omitting this optional filename token does not omit, default or change the mandatory stored Tier. Do not encode `PRINCIPLE`, `CORE`, `GENERAL`, `STANDARD` or another legacy Tier name as the numeric `TIER` token. A legacy filename remains nonconformant until its affected Carrier and references have an explicit migration disposition; old names are not grandfathered by this rule.

This generic Project-owned Carrier rule does not replace the dedicated filename rules for an Operator-owned Project Goal. It does not invent a default numeric Tier or revive the retired named/default-Tier rules.
