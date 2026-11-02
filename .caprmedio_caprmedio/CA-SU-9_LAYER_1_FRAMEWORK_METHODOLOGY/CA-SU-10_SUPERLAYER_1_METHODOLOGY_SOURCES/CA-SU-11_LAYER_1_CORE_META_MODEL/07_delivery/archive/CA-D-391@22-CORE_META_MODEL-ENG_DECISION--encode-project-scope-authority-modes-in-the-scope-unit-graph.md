---
subjects:
  governs: Entity/Object/Continuant/Projection//PROJECT_SCOPE_UNIT_GRAPH
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 22
updated_at: 2026-10-29 10:13:50 +0400
relations:
  child_of:
  - CA-R-1430
atom_id: CA-D-391@22
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Encode project scope authority modes in the Scope Unit Graph

## Claim scope

the `authority_mode` of a retained Project Scope Unit Graph Projection.

## Claim

**if** a Project Scope Unit Graph Projection is retained for compatibility, its `authority_mode` **must** be a derived effective value: an explicit unit override from Project Structure, **otherwise** the applicable Framework Instance Settings selection. it **must not** select **or** own that mode, become a required input **to** a direct Project Structure consumer, **or** require creation of a separate structural Projection.
