---
subjects:
  governs: TOOLS/Goal
  depends_on:
  - PROGRAMMATIC
version: 11
updated_at: "2026-10-18 05:15:32 +0400"
relations: {}
atom_id: CA-R-1186
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
type: Goal
---
# Summary

Own Independently Executable Framework Tools

## Scope

PROGRAMMATIC behavior governing TOOLS.

## Claim

TOOLS **must** own reusable framework capabilities through two unordered groups: CONNECTORS for adapters/connectors and CAPRMEDIO_TOOLS for reusable CAPRMEDIO action Tools and their declared Tool children. PROJECT_TOOLS is project-local and excluded. Tools remain classifiable as Hooks, Finders, or Doers; Checkers remain a Finder specialization.

## Details

Hooks emit triggers into Tool flows and have no read, classification or mutation authority beyond observing their registered boundary.
