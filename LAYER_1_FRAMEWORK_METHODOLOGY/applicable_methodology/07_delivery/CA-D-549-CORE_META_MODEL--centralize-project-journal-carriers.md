---
atom_id: CA-D-549
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/History/Journal"
  depends_on: ["Entity/Node/Continuant/Project", "Entity/Node/Continuant/History/Journal", "Entity/Carrier", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow"]
version: 8
updated_at: "2026-10-19 15:56:00 +0400"
relations: {}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-549-CORE_META_MODEL--centralize-project-journal-carriers.md
  source_atom_id: CA-D-549
  source_atom_revision: 8
  source_sha256: f8d359f18cbe0c6736d959b300cc1d2737758550f7418d96462e7143016b4ce0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Centralize Project Journal Carriers

## Scope

persistent File Carriers of a Project's shared Work Journal and other project-control Journals.

## Claim

**all** persistent project-control Journal File Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.

## Details

- Journal segments use this root **or** its subdirectories.
- Artifact Change Log **and** Workflow Execution Log views **are** Projections, **not** separate authoritative Journals.
- Runtime locks, receipts, **and** pending-recording state remain runtime state, **not** canonical Journal Carriers.

Technical and business runtime logs are Journals too, but their configured local database, remote database, or logging sink Carriers are not required to reside in this Directory Carrier. Journal classification does not impose one physical storage technology.
