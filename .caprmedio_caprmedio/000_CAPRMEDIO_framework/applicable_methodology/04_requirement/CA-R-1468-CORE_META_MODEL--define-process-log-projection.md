---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Process Log"
  depends_on:
    ["Entity/Node/Occurrent/Execution/Step Run", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/History/Journal", "Entity/Node/Continuant/History/Journal.Record", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow"]
version: 10
updated_at: "2026-10-19 15:53:12 +0400"
relations: {}
atom_id: "CA-R-1468"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1468-CORE_META_MODEL--define-process-log-projection.md
  source_atom_id: CA-R-1468
  source_atom_revision: 10
  source_sha256: 69d6e3ac553796d36e61a2fb6c46c84d625d4bb996152fe939c50eaa3d08797e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Process Log Projection

## Scope

the Process Log Projection Type.

## Claim

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.

## Details
