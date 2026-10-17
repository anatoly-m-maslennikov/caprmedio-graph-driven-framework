---
subjects:
  governs: "Entity/Carrier/Directory Carrier"
  depends_on: []
version: 12
updated_at: "2026-10-16 12:09:19 +0000"
relations: {}
atom_id: "CA-D-318"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-318-CORE_META_MODEL--place-project-owned-persistent-carriers.md
  source_atom_id: CA-D-318
  source_atom_revision: 12
  source_sha256: 92ad5d4f11d2a618607479f5e4a0db76b8b852bd45de5acd31905973240ae304
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Project-Owned Persistent Carriers

## Scope

persistent Carriers of Project governing Artifacts and project-control evidence.

## Claim

**every** governed Project **must** place its governing Artifacts **and** project-control evidence under `.caprmedio_<project_name>/`, **where** `<project_name>` is that Project's exact lowercase name.

## Details

Project-control Journal File Carriers use _journal and persistent view Projections use _projection under this root. Native Implementation follows its own governed Delivery location. Runtime technical and business Journal Carriers may instead use explicitly configured local databases, remote databases, or logging sinks; their Journal classification does not force their physical storage into the Project-control root.
