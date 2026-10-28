---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection.Authority
version: 21
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1568
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Permit Projections as Implementation outputs

## Scope

non-authoritative view Projections delivered as Implementation outputs.

## Claim

a view Projection **may** be delivered as an Implementation output of its governing RMED **without** becoming an Atom **or** another source of truth for the facts it represents.

- its output contribution is I; its Artifact kind remains Projection **and** its content remains derived from its declared sources.

## Details

This permission concerns a derived view delivered as an Implementation output, not Implementation as a whole. Directly edited native Implementation realizes RMED and can be a source of truth for what actually exists; it is not a Projection. A generated dependency graph or another derived view of Implementation remains a Projection: update its sources, then rebuild the view through its Workflow.
