---
atom_id: CA-R-1186
ref_id: CA-R-1186@19
container:
  scope_unit: CA-SU-15
role: Requirement
form: Goal
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
tier: 3
status: Archived
version: 19
updated_at: 2026-10-27 19:59:51 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
destination:
  file:
    name: CA-R-1186@19-PROGRAMMATIC-GOAL-TOOLS--own-independently-executable-framework-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archived
---
# Summary

Own Independently Executable Framework Tools

## Scope

PROGRAMMATIC behavior governing TOOLS.

## Claim

TOOLS **must** own reusable framework capabilities through two unordered groups: CONNECTORS for adapters/connectors and CAPRMEDIO_TOOLS for reusable CAPRMEDIO action Tools and their declared Tool children. PROJECT_TOOLS is project-local and excluded. Tools remain classifiable as Hooks, Finders, or Doers; Checkers remain a Finder specialization.

## Details

Hooks emit triggers into Tool flows and have no read, classification or mutation authority beyond observing their registered boundary.
