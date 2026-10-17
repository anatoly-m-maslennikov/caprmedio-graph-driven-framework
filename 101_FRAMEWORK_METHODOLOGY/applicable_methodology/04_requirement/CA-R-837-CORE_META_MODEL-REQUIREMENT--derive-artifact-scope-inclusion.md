---
subjects:
  governs: "scope-topology"
  depends_on:
    ["Entity/Continuant/Object/Atom.Author"]
version: 21
updated_at: "2026-10-15 18:46:38 +0000"
relations: {}
atom_id: "CA-R-837"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-837-CORE_META_MODEL-REQUIREMENT--derive-artifact-scope-inclusion.md
  source_atom_id: CA-R-837
  source_atom_revision: 21
  source_sha256: 4a4e3b0666f895e7022a8390c945c536f6629f7a4fb4af43576bb586fc3e350d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Artifact scope inclusion

## Scope

Artifacts contained **in** a Scope Unit.

## Claim

the resolver **must** resolve **`=1`** direct Scope Unit from the Atom's internally carried ownership, checked against its canonical Carrier address, **or** from the registered canonical Carrier authority for a non-Atom Artifact **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.

## Details

an Atom with no containing Scope Unit uses the external-Atom Author fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter; a failed Scope Unit resolution does **not** establish that no containing Scope Unit exists.
