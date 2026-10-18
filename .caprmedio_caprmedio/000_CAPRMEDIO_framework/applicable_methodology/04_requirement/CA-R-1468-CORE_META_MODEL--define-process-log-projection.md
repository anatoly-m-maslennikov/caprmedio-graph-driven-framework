---
subjects:
  governs: "Entity/Continuant/Node/Projection/Type: Process Log"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Node/Projection", "Entity/Continuant/Node/History/Journal", "Entity/Continuant/Node/History/Journal.Record", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Workflow"]
version: 9
updated_at: "2026-10-18 03:33:34 +0400"
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
  source_atom_revision: 9
  source_sha256: 47899acaec5c6393d82f7b96d1bff633955f189f07e61d485e253c61a9560d07
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Process Log Projection

## Scope

the Process Log Projection Type.

## Claim

a Process Log **means** a non-authoritative Projection of the Project Journal that presents recorded Workflow Runs, Step Runs, **and** Action executions using their recorded execution associations, progress, **and** outcomes. it includes recorded executions **without** Artifact changes **and** does **not** infer an unrecorded execution association **or** successful outcome.

## Details
