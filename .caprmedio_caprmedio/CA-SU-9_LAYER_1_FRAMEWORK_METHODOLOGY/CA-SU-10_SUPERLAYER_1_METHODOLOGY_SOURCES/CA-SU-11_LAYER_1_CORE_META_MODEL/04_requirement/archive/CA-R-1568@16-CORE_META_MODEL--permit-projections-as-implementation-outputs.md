---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Engineering/Implementation
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Projection.Authority
version: 16
updated_at: 2026-10-24 10:48:25 +0400
relations:
  relates_to:
  - CA-R-1548
  - CA-R-1703
atom_id: CA-R-1568@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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

This permission concerns delivered views, not a permanent loss of actual-state authority for native Implementation. RMED → using O → I derives a realization of intent; that native I can then be source truth for what actually exists. I → using O → a dependency graph or another view produces a non-authoritative Projection.
