---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom.ID", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/Atom.Owning Scope Unit"]
version: 18
updated_at: "2026-10-19 15:55:21 +0400"
relations: {}
atom_id: "CA-D-283"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-283-CORE_META_MODEL-DELIVERY--serialize-project-owned-markdown-atom-filenames.md
  source_atom_id: CA-D-283
  source_atom_revision: 18
  source_sha256: a30fd3b3232eee4677b858f975c0eae45d4823a9579c3980547a22358da1f808
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Project-Owned Markdown Atom Filenames

## Scope

Identified Project-owned Markdown Atom filenames other than Plan filenames governed by CA-D-469.

## Claim

**every** identified Project-owned Markdown Atom filename other than a Plan filename governed by CA-D-469 **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<LOCAL_TIER>][-<ATOM_TYPE>][-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. serialize the `ATOM_TYPE` segment **only** **when** the Atom carries a Type under CA-D-276; an omitted Type has no filename segment. **every** same-identity Atom Revision **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename **and** serialize its retained Summary under CA-D-282. a replacement filename **must** contain the successor Atom ID **and** the successor's Summary Slug; a Summary Slug **must not** be edited independently of its source Summary.

## Details
