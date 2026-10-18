---
atom_id: CA-D-550
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Projection Carrier Root"
  depends_on: ["Entity/Continuant/Object/Project", "Entity/Continuant/Projection", "Entity/Carrier", "Entity/Continuant/Projection/Type: Applicable Methodology", "Entity/Continuant/History/Journal", "Entity/Continuant/Object/Atom", "Methodology Source", "Entity/Continuant/Object/Project.Settings", "Entity/Continuant/Object/Project.Structure"]
version: 6
updated_at: "2026-10-15 18:52:31 +0000"
relations: {}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-550-CORE_META_MODEL--centralize-project-projection-carriers.md
  source_atom_id: CA-D-550
  source_atom_revision: 6
  source_sha256: 890c80cab34a4ceaa1f11897be2f4fba3091f1524c555fda88fd30c983d70c39
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Centralize Project Projection Carriers

## Scope

persistent non-authoritative view Projection Carriers belonging to a Project.

## Claim

**all** persistent view Projection Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_projection/`, **except** Applicable Methodology, whose Carrier Root **must** remain `.caprmedio_<project_name>/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`.

## Details

- Graphs **and** derived Journal views use `_projection/` **or** named subdirectories beneath it.
- Applicable Methodology uses its separate Carrier Root; its Methodology Sources retain the `000_APPLICABLE_MTHD_sources/` subdirectory.
- Authoritative Atoms, Methodology Sources, Project Settings, and Project Structure retain their own authoritative locations.
- Temporary build stages **and** intermediate reports remain ephemeral; publication places the delivered view Projection under its declared Carrier Root.
- The derivation RMED → using O → I does not relocate native Implementation into _projection: native I uses its governed Delivery place and may supply actual-state source facts. Views subsequently generated from I use _projection.
