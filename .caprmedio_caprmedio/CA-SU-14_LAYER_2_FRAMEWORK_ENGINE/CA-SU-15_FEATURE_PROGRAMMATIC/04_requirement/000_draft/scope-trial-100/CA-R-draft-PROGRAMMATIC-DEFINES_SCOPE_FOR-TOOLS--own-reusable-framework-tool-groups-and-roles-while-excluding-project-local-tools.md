---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit.Scope
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
atom_id: CA-R-draft
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: TOOLS
status: Draft
author: Anatoly Maslennikov
type: Scope Definition
tier: 3
---
## Summary

Own reusable framework Tool groups and roles while excluding project-local Tools

## Claim scope

PROGRAMMATIC behavior governing TOOLS.

## Claim

TOOLS **must** own reusable framework capabilities through two unordered groups: CONNECTORS for adapters/connectors and CAPRMEDIO_TOOLS for reusable CAPRMEDIO action Tools and their declared Tool children. PROJECT_TOOLS is project-local and excluded. Tools remain classifiable as Hooks, Finders, or Doers; Checkers remain a Finder specialization.

## Details

Hooks emit triggers into Tool flows and have no read, classification or mutation authority beyond observing their registered boundary.
