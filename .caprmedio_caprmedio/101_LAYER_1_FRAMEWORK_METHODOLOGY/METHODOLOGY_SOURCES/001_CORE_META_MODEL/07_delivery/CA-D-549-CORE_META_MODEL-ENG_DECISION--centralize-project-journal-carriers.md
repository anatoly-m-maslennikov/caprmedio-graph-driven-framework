---
atom_id: CA-D-549
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
version: 16
updated_at: 2026-10-27 19:59:27 +0400
relations: {}
tier: 3
type: Eng Decision
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
