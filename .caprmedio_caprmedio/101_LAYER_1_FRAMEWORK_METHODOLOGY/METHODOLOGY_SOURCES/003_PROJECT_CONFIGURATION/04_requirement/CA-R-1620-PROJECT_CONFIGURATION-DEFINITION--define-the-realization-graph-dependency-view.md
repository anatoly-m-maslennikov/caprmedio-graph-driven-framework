---
atom_id: CA-R-1620
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Realization Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
version: 15
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
tier: 3
type: Definition
---
# Summary

Define the Realization Graph dependency view

## Scope

optional dependency views of Realization Graphs.

## Claim

the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.

## Details

- its specification identifies the selected population, Relation Types, source boundary, **and** limits of dependency traversal; recursive reachability does **not** establish complete coverage by itself.
- the view **must** derive from the same source-backed graph facts **without** another independently maintained dependency authority. cycles are represented **when** evidenced; their validity is checked against applicable Claims rather than assumed from the view name.
- this view does **not** require a second universal view.
