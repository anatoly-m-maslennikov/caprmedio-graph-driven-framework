---
atom_id: CA-D-550
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Directory
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
version: 16
updated_at: 2026-10-27 19:59:27 +0400
relations: {}
tier: 3
type: Eng Decision
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
