---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection//PROJECT_SCOPE_UNIT_GRAPH
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 15
updated_at: 2026-10-24 01:18:03 +0400
relations:
  child_of:
  - CA-R-1430
atom_id: CA-D-391@15
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Encode project scope authority modes in the Scope Unit Graph

## Scope

the `authority_mode` of a retained Project Scope Unit Graph Projection.

## Claim

**if** a Project Scope Unit Graph Projection is retained for compatibility, its `authority_mode` **must** be a derived effective value: an explicit unit override from Project Structure, **otherwise** the applicable Framework Instance Settings selection. it **must not** select **or** own that mode, become a required input **to** a direct Project Structure consumer, **or** require creation of a separate structural Projection.

## Details
