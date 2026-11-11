---
atom_id: CA-D-549
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Journal
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Journal
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Projection
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
version: 19
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-549-CORE_META_MODEL-ENG_DECISION--centralize-project-journal-carriers.md
  source_atom_id: CA-D-549
  source_atom_revision: 19
  source_sha256: ad3835f137a562fe815987f85166a84d416921dcf26933dea9d2b1b1207394b9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Centralize Project Journal Carriers

## Claim scope

persistent File Carriers of a Project's shared Work Journal and other project-control Journals.

## Claim

**all** persistent project-control Journal File Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.

## Details

- Journal segments use this root **or** its subdirectories.
- Artifact Change Log **and** Workflow Execution Log views **are** Projections, **not** separate authoritative Journals.
- Runtime locks, receipts, **and** pending-recording state remain runtime state, **not** canonical Journal Carriers.

Technical and business runtime logs are Journals too, but their configured local database, remote database, or logging sink Carriers are not required to reside in this Directory Carrier. Journal classification does not impose one physical storage technology.
