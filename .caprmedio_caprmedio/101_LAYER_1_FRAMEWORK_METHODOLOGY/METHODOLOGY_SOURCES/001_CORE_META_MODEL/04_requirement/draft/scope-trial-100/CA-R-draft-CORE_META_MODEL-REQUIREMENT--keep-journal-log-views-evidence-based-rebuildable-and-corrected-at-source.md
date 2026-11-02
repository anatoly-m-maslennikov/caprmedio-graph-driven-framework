---
subjects:
  governs: Entity/Object/Continuant/Projection
  depends_on:
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/History/Journal > Event Record
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - 'Entity/Object/Continuant/Projection/Type: Artifact Change Log'
  - 'Entity/Object/Continuant/Projection/Type: Process Log'
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
atom_id: CA-R-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 2
type: Requirement
---
## Summary

Keep Journal log views evidence-based, rebuildable and corrected at source

## Claim scope

Artifact Change Log and Process Log Projection Types derived from the same Project Journal

## Claim

A read-only execution requires no fictitious Artifact change; membership and execution associations must come from recorded source evidence rather than invented events or inferred success. A view must remain rebuildable from its declared Journal selection, disclose known incomplete or stale source coverage without claiming complete current history, and obtain corrections through the owning source authority rather than independent log edits.
