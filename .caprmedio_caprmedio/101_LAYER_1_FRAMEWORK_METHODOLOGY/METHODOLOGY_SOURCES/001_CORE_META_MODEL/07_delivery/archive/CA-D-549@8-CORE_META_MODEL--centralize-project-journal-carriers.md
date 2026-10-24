---
atom_id: CA-D-549@8
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/History/Journal"
  depends_on: ["Entity/Node/Continuant/Project", "Entity/Node/Continuant/History/Journal", "Entity/Carrier", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow"]
version: 8
updated_at: "2026-10-19 15:56:00 +0400"
relations: {}
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
