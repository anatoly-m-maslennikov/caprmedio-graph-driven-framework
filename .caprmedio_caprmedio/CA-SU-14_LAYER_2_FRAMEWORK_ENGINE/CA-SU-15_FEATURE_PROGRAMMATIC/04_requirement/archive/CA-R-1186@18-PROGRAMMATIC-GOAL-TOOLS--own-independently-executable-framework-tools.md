---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Component Structure
  depends_on:
  - Subject/Graph Node/Engineering/Architecture/Component Structure
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1186@18
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
type: Goal
tier: 3
---
# Summary

Own Independently Executable Framework Tools

## Scope

PROGRAMMATIC behavior governing TOOLS.

## Claim

TOOLS **must** own reusable framework capabilities through two unordered groups: CONNECTORS for adapters/connectors and CAPRMEDIO_TOOLS for reusable CAPRMEDIO action Tools and their declared Tool children. PROJECT_TOOLS is project-local and excluded. Tools remain classifiable as Hooks, Finders, or Doers; Checkers remain a Finder specialization.

## Details

Hooks emit triggers into Tool flows and have no read, classification or mutation authority beyond observing their registered boundary.
