---
subjects:
  governs: "Artifact.Activity"
  depends_on:
    ["Artifact", "Artifact.Status", "Property", "Artifact.Activity: Active", "Artifact.Activity: Inactive"]
version: 11
updated_at: "2026-10-15 12:21:42 +0000"
relations: {}
atom_id: "CA-R-1394"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1394-CORE_META_MODEL-CORE--define-artifact-activity.md
  source_atom_id: CA-R-1394
  source_atom_revision: 11
  source_sha256: f8b582cda4b34f977dd0b93a30e49e6089d63385f5570bcff8bb865ca7426522
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Define Artifact Activity

## Scope
Artifact Activity derived from an Artifact's current Revision Status within the applicability defined by CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models, including absence of an applicable Status model.

## Claim

the Artifact Property Activity **means** the derived Property that classifies an Artifact as Active **or** Inactive from its current Revision Status within the applicability defined by CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models. absence of an applicable Status model **means** absence of Activity, **not** Activity Inactive.

## Details
