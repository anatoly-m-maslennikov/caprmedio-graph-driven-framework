---
atom_id: CA-D-318
ref_id: CA-D-318
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
status: Active
version: 25
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-D-318-CORE_META_MODEL-DECISION--place-project-owned-persistent-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-318-CORE_META_MODEL-ENG_DECISION--place-project-owned-persistent-carriers.md
  source_atom_id: CA-D-318
  source_atom_revision: 25
  source_sha256: ccb04d19c98191cee6ae4b6c655d6ede73124e6c0df12b05f4fdc387b6b7c246
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place Project-Owned Persistent Carriers

## Claim

### Prose Claim


persistent Carriers of Project governing Artifacts and project-control evidence.


**every** governed Project **must** place its governing Artifacts **and** project-control evidence under `.caprmedio_<project_name>/`, **where** `<project_name>` is that Project's exact lowercase name.

## Details

Project-control Journal File Carriers use _journal and persistent view Projections use _projection under this root. Native Implementation follows its own governed Delivery location. Runtime technical and business Journal Carriers may instead use explicitly configured local databases, remote databases, or logging sinks; their Journal classification does not force their physical storage into the Project-control root.
