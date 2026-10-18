---
subjects:
  governs: "Entity/Continuant/Node/Atom.Updated At"
  depends_on:
    ["Entity/Continuant/Node/Atom", "Entity/Continuant/Node/History/Revision/Type: Atom", "Entity/Carrier", "Entity", "Entity/Continuant/Node/Atom.Status", "Entity/Carrier.Canonical Address"]
version: 7
updated_at: "2026-10-18 03:33:57 +0400"
claim_target_scope_unit: "CORE_META_MODEL"
relations:
  child_of:
    - CA-R-1416
atom_id: "CA-R-1788"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1788-CORE_META_MODEL--refresh-updated-at-whenever-an-atom-changes.md
  source_atom_id: CA-R-1788
  source_atom_revision: 7
  source_sha256: ef2a15c9bd25b790131c93511cf443bac661884d4dcfd2d6d4720c0b2f3d0024
  original_relations_sha256: 4847fb4582248044a24be63c7b8943ad429a2717d1a91a92e578a6a7656a08d0
---
# Summary

Refresh Updated At whenever an Atom changes

## Scope

accepted Markdown Atom Carrier edits.

## Claim

**every** actual accepted edit **to** an Atom Carrier **must** refresh that Atom Revision's `updated_at` **to** the actual Project-time edit instant, including a formatting, lossless serialization, Entity-name, Status, direct-owner, **or** current-Atom local-placement edit. an exact no-op **must** retain Updated At. retaining exact predecessor bytes as history **must not** change that predecessor's Updated At.

## Details

an ancestor-only move that changes an Atom's repository locator **without** changing its own bytes, metadata, direct owner **or** placement relative **to** that owner is **not** an edit **to** that Atom. retain its Updated At **and** Version under CA-R-1432. this applies **to** **every** Atom, regardless of Content Role; it does **not** exempt an actual Status, filename, ownership **or** local-placement change. preserve exact older Revision bytes.

changing the current Atom's Status **to** Archived is an actual update governed by CA-R-1432. preserving an earlier Version **in** history is a different operation: copy its exact prior bytes, including Version, Status **and** Updated At, **without** another metadata update. timestamp encoding follows `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`.
