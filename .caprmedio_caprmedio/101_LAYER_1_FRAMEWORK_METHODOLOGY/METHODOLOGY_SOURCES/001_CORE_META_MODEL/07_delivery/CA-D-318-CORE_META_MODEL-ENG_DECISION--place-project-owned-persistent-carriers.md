---
subjects:
  governs: Subject/Graph Node/Carrier/Directory
  depends_on: []
version: 20
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-318
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Place Project-Owned Persistent Carriers

## Scope

persistent Carriers of Project governing Artifacts and project-control evidence.

## Claim

**every** governed Project **must** place its governing Artifacts **and** project-control evidence under `.caprmedio_<project_name>/`, **where** `<project_name>` is that Project's exact lowercase name.

## Details

Project-control Journal File Carriers use _journal and persistent view Projections use _projection under this root. Native Implementation follows its own governed Delivery location. Runtime technical and business Journal Carriers may instead use explicitly configured local databases, remote databases, or logging sinks; their Journal classification does not force their physical storage into the Project-control root.
