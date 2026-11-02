---
subjects:
  governs: "Artifact.Status"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step"]
version: 17
updated_at: "2026-10-19 15:52:47 +0400"
relations: {}
atom_id: "CA-R-1312"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1312-CORE_META_MODEL-CORE--separate-governed-transitions-from-status-values.md
  source_atom_id: CA-R-1312
  source_atom_revision: 17
  source_sha256: ddc02a475d703575c9d0647ba931aeac641e24d55c97e33749920aedbaf923a8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Separate Governed Transitions from Status Values

## Scope
Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

## Claim
an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
