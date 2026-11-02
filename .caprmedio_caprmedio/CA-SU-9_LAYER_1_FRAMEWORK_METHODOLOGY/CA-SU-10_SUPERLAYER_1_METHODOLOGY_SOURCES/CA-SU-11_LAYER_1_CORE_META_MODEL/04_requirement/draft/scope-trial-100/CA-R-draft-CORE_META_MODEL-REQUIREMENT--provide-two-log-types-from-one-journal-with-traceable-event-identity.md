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

Provide two log types from one Journal with traceable event identity

## Claim scope

Artifact Change Log and Process Log Projection Types derived from the same Project Journal

## Claim

The Core Meta-Model must provide Artifact Change Log and Process Log as exactly two log Projection Types derived from the same Project Journal, under CA-R-1467-CORE_META_MODEL-DEFINITION--define-artifact-change-log-projection and CA-R-1468-CORE_META_MODEL-REQUIREMENT--define-process-log-projection. These Types organize recorded history without introducing independent Journals; additional Projection Types remain governed by the open Projection model. Every represented historical fact must remain traceable to its canonical source event record and Event identity. The same source event may appear in both views without becoming two authoritative records.
