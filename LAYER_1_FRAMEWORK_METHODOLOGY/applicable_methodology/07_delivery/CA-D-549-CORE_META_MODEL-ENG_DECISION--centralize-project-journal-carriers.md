---
atom_id: CA-D-549
ref_id: CA-D-549
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
tier: 3
status: Active
version: 19
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-549-CORE_META_MODEL-DECISION--centralize-project-journal-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-549-CORE_META_MODEL-ENG_DECISION--centralize-project-journal-carriers.md
  source_atom_id: CA-D-549
  source_atom_revision: 19
  source_sha256: 32dcb188ba87c91591e162635810e7ad53d2bf7d4087730bea123f3422c9c24f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Centralize Project Journal Carriers

## Claim

### Prose Claim


persistent File Carriers of a Project's shared Work Journal and other project-control Journals.


**all** persistent project-control Journal File Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.

## Details

- Journal segments use this root **or** its subdirectories.
- Artifact Change Log **and** Workflow Execution Log views **are** Projections, **not** separate authoritative Journals.
- Runtime locks, receipts, **and** pending-recording state remain runtime state, **not** canonical Journal Carriers.

Technical and business runtime logs are Journals too, but their configured local database, remote database, or logging sink Carriers are not required to reside in this Directory Carrier. Journal classification does not impose one physical storage technology.
