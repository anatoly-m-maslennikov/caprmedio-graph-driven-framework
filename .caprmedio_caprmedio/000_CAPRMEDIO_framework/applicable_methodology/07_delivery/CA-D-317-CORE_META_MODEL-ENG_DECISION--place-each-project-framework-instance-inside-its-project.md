---
atom_id: CA-D-317
ref_id: CA-D-317
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project
tier: 3
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-D-317-CORE_META_MODEL-DECISION--place-each-project-framework-instance-inside-its-project.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-317-CORE_META_MODEL-ENG_DECISION--place-each-project-framework-instance-inside-its-project.md
  source_atom_id: CA-D-317
  source_atom_revision: 28
  source_sha256: 73b7f1bc4c3703ba0be9f1e24d02b81db6560533284073bcf7bf591bffd9398f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place each Project Framework Instance inside its Project

## Claim

### Prose Claim


CAPRMEDIO Framework Instances serving Projects.


the Methodology **and** Tool governance of the CAPRMEDIO Framework Instance serving a Project **must** reside under that Project's `.caprmedio_<project_name>/000_CAPRMEDIO_framework/` Directory Carrier. this Carrier **must** contain that Project's Methodology Sources **and** Framework Instance Settings. another Project's Framework Instance **or** a repository-shared framework directory **must not** substitute for this Project's instance.

## Details

Applicable Methodology **is** a Projection; its delivered Carriers use the Project's `_projection/` root, **not** this source-governance Carrier.
