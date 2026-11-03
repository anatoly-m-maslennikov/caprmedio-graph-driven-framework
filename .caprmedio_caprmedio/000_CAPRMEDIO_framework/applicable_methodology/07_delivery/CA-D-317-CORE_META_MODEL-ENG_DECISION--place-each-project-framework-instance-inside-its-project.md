---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project
version: 28
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-D-317
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-317-CORE_META_MODEL-ENG_DECISION--place-each-project-framework-instance-inside-its-project.md
  source_atom_id: CA-D-317
  source_atom_revision: 28
  source_sha256: 12641f4d7fbc0ae94e255ba9623b49b58091911e6d5fd6cdce8dad8b0c6983a4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place each Project Framework Instance inside its Project

## Claim scope

CAPRMEDIO Framework Instances serving Projects.

## Claim

the Methodology **and** Tool governance of the CAPRMEDIO Framework Instance serving a Project **must** reside under that Project's `.caprmedio_<project_name>/000_CAPRMEDIO_framework/` Directory Carrier. this Carrier **must** contain that Project's Methodology Sources **and** Framework Instance Settings. another Project's Framework Instance **or** a repository-shared framework directory **must not** substitute for this Project's instance.

## Details

Applicable Methodology **is** a Projection; its delivered Carriers use the Project's `_projection/` root, **not** this source-governance Carrier.
