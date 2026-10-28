---
version: 30
updated_at: 2026-10-27 20:00:02 +0400
relations:
  child_of:
  - CA-M-005
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Minimum Model
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/caprmedio/Product: CAPRMEDIO Framework'
atom_id: CA-R-1772
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Minimal default project model

## Scope

Project models.

## Claim

CAPRMEDIO **must** use Project-scope Requirement authority plus its real Implementation as the minimum Project model, **must not** require an Implementation Atom, **and** **may** enable other Atom roles, applicability tiers, descendant scopes, **or** automation **only** **when** necessary. Scope Unit ancestry remains parent-declaration data; no Structural Level property is required.

## Details
