---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Projection/Type: Artifact Change Log'
  - 'Subject/Domain/Node/Continuant/Projection/Type: Process Log'
version: 14
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1463@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Summary

Derive log views from the shared Journal

## Scope

Artifact Change Log and Process Log log Projection Types derived from the same Project Journal.

## Claim

the Core Meta-Model **must** provide Artifact Change Log **and** Process Log as **`=2`** log Projection Types derived from the same Project Journal, under CA-R-1467-CORE_META_MODEL--define-artifact-change-log-projection **and** CA-R-1468-CORE_META_MODEL-REQUIREMENT--define-process-log-projection. these Types organize recorded history **without** introducing independent Journals; additional Projection Types remain governed by the open Projection model.

**every** represented historical fact **must** remain traceable **to** its canonical source event record **and** Event identity. the same source event **may** appear **in** both views **without** becoming two authoritative records. a read-only execution requires no fictitious Artifact change; membership **and** execution associations **must** come from recorded source evidence rather than invented events **or** inferred success. a view **must** remain rebuildable from its declared Journal selection, disclose known incomplete **or** stale source coverage **without** claiming complete current history, **and** obtain corrections through the owning source authority rather than independent log edits.

## Details
