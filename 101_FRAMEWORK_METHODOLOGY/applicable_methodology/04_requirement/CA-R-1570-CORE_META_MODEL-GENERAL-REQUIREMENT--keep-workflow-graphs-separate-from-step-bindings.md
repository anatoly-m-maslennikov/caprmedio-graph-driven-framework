---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Relation/Type: On Result"]
version: 6
updated_at: "2026-10-16 12:08:31 +0000"
relations: {"relates_to": ["CA-R-1508", "CA-R-1509", "CA-R-1513", "CA-R-1563", "CA-R-1569"]}
atom_id: "CA-R-1570"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-workflow-graphs-separate-from-step-bindings.md
  source_atom_id: CA-R-1570
  source_atom_revision: 6
  source_sha256: 3167c7288515afa1b31ed64d582894dac4edf13ec5447dae479e0173685149a6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Workflow graphs separate from Step bindings

## Scope

Workflow graph schemes and Step bindings.

## Claim

a Workflow Atom **must** own **only** its graph scheme: Step references, typed directed Relations, entry points, transition conditions, **and** terminal outcomes.

- the referenced Step Atoms own Action references, parameters, **and** input bindings.
- reusable Action Atoms own Action behavior.
- the graph **must not** independently repeat those Step bindings **or** Action definitions; folder nesting **and** file order **must not** replace its declared control flow.

## Details
