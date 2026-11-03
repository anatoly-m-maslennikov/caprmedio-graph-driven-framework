---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Directory
version: 25
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-D-318
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-318-CORE_META_MODEL-ENG_DECISION--place-project-owned-persistent-carriers.md
  source_atom_id: CA-D-318
  source_atom_revision: 25
  source_sha256: 695f208fbd3c737c421c10e7f2e380dfde97d791399bbb0a49f3455e047799a6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place Project-Owned Persistent Carriers

## Claim scope

persistent Carriers of Project governing Artifacts and project-control evidence.

## Claim

**every** governed Project **must** place its governing Artifacts **and** project-control evidence under `.caprmedio_<project_name>/`, **where** `<project_name>` is that Project's exact lowercase name.

## Details

Project-control Journal File Carriers use _journal and persistent view Projections use _projection under this root. Native Implementation follows its own governed Delivery location. Runtime technical and business Journal Carriers may instead use explicitly configured local databases, remote databases, or logging sinks; their Journal classification does not force their physical storage into the Project-control root.
