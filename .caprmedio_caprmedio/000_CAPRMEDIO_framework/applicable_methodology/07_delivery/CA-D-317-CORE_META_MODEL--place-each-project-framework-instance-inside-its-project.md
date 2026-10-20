---
subjects:
  governs: "Entity/Node/Continuant/Project"
  depends_on: []
version: 18
updated_at: "2026-10-19 15:55:28 +0400"
relations: {}
atom_id: "CA-D-317"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-317-CORE_META_MODEL--place-each-project-framework-instance-inside-its-project.md
  source_atom_id: CA-D-317
  source_atom_revision: 18
  source_sha256: bbd9ab71d24ea4206e891355507290b4367128ed6702332ded8d583990a1b8a2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place each Project Framework Instance inside its Project

## Scope

CAPRMEDIO Framework Instances serving Projects.

## Claim

the Methodology **and** Tool governance of the CAPRMEDIO Framework Instance serving a Project **must** reside under that Project's `.caprmedio_<project_name>/000_CAPRMEDIO_framework/` Directory Carrier. this Carrier **must** contain that Project's Methodology Sources **and** Framework Instance Settings. another Project's Framework Instance **or** a repository-shared framework directory **must not** substitute for this Project's instance.

## Details

Applicable Methodology **is** a Projection; its delivered Carriers use the Project's `_projection/` root, **not** this source-governance Carrier.
