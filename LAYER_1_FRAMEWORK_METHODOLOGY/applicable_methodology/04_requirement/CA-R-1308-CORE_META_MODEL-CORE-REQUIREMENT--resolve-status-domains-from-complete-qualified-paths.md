---
subjects:
  governs: "Artifact.Status"
  depends_on:
    - "Artifact/Type"
    - "Atom/Content Role"
    - "Type"
version: 13
updated_at: "2026-10-17 12:53:00 +0000"
relations: {}
atom_id: "CA-R-1308"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1308-CORE_META_MODEL-CORE-REQUIREMENT--resolve-status-domains-from-complete-qualified-paths.md
  source_atom_id: CA-R-1308
  source_atom_revision: 13
  source_sha256: f4fe12fd727cd7a42e110ac7090ddc2a2d7f71852abdcacead6a22c251e67ff0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Resolve Status Domains from Complete Qualified Paths

## Scope

Status domains resolved from complete qualified paths.

## Claim

a global Status value domain **must not** override the Status domain resolved from the complete qualified path of an Artifact Type **or** Atom Content Role **and** Type.

## Details

for Atoms, resolution from the complete qualified Content Role and Type path includes the allowed values inherited from Atom.Status and the additional values admitted for that path. Inheritance does **not** replace the qualified model with a flat global domain or remove its additions. A narrower Atom kind **must not** remove inherited Status values.

