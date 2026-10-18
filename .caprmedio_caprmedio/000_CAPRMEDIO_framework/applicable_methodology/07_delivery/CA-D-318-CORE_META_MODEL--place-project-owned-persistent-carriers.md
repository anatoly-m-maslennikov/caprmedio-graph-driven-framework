---
subjects:
  governs: "Entity/Carrier/Directory Carrier"
  depends_on: []
version: 14
updated_at: "2026-10-18 07:36:52 +0400"
relations: {}
atom_id: "CA-D-318"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-318-CORE_META_MODEL--place-project-owned-persistent-carriers.md
  source_atom_id: CA-D-318
  source_atom_revision: 14
  source_sha256: da5e97a02251d5d74a9f8ab8dda60af18184d27126993bbf165bf0290a1b89f6
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
