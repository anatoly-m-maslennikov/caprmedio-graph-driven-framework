---
atom_id: CA-R-2224
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Subject Graph Dependency-only Subjects'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
relations:
  depends_on:
  - CA-R-2150
tier: 2
version: 1
updated_at: 2026-10-27 23:53:05 +0400
---
# Summary

Define Dependency-only Subjects Projection

## Claim

A Subject Graph Dependency-only Subjects Projection **means** the exact canonical Subject paths occurring in subjects.depends_on but not in subjects.governs within the same selected Current RMEDO source set. Apply the declared Subject-branch filter to those targets. List each path once with its referring Atom IDs, alphabetically. Governs references outside the selected sources do not remove a path from this view. Its entries describe selection-relative coverage, not proof of a project-wide missing definition.
