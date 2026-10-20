---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom.ID"]
version: 20
updated_at: "2026-10-20 17:07:25 +0400"
relations: {}
atom_id: "CA-D-288"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number.md
  source_atom_id: CA-D-288
  source_atom_revision: 20
  source_sha256: 7f90e0c94b2a190c02704b00563b1350f3753e2fae5ea18c366803f11058f236
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Serialize Draft Atom Filenames with an Empty Number

## Scope
Project-owned Draft Atom filenames.

## Claim

**every** Project-owned Draft Atom filename **must** use `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>--` **before** its mutable components **and** **must not** carry an Atom ID.

## Details

### Existing temporary-ID exception

Draft identity rules have no temporary-ID exception. Existing source validation, permissions and exact history preservation still apply.
