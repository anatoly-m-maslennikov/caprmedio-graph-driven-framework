---
subjects:
  governs: "Entity/Node/Continuant/Project"
  depends_on: []
version: 18
updated_at: "2026-10-19 11:46:01 +0000"
relations: {}
atom_id: "CA-D-317@draft"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Place each Project Framework Instance inside its Project

## Scope

CAPRMEDIO Framework Instances serving Projects.

## Claim

the Methodology **and** Tool governance of the CAPRMEDIO Framework Instance serving a Project **must** reside under that Project's `.caprmedio_<project_name>/000_CAPRMEDIO_framework/` Directory Carrier. this Carrier **must** contain that Project's Methodology Sources **and** Framework Instance Settings. another Project's Framework Instance **or** a repository-shared framework directory **must not** substitute for this Project's instance.

## Details

Applicable Methodology **is** a Projection; its delivered Carriers use the Project's `_projection/` root, **not** this source-governance Carrier.
