---
atom_id: CA-R-1620@19
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: 'Entity/Object/Continuant/Projection/Type: Realization Graph'
  passive:
  - CFEL > Relation
  - Projection
version: 19
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Define the Realization Graph dependency view

## Claim scope

optional dependency views of Realization Graphs.

## Claim

the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.

## Details

- its specification identifies the selected population, Relation Types, source boundary, **and** limits of dependency traversal; recursive reachability does **not** establish complete coverage by itself.
- the view **must** derive from the same source-backed graph facts **without** another independently maintained dependency authority. cycles are represented **when** evidenced; their validity is checked against applicable Claims rather than assumed from the view name.
- this view does **not** require a second universal view.
