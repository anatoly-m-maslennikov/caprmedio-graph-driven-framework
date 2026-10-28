---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Scope Unit Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
version: 36
updated_at: 2026-10-27 20:00:10 +0400
relations:
  child_of:
  - CA-R-960
  - CA-R-961
  - CA-R-962
atom_id: CA-R-626
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Project the current Scope Unit Graph without owning authority

## Scope

Project Scope Unit Graph Projections.

## Claim

**every** Project Scope Unit Graph Projection **must** distinguish declared Scope Unit facts from Project Structure, derived structural values, effective Settings, **and** observed Carrier materialization. a discrepancy, missing Goal, undeclared candidate directory, **or** declared unit with no existing Carrier **must** remain visible as a separate finding **without** silently changing the declaration **or** inventing source authority.

## Details
