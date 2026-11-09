---
atom_id: CA-R-1108
ref_id: CA-R-1108
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface
    Contracts
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-511
  - CA-M-170
status: Active
version: 22
updated_at: 2026-11-09 21:15:45 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1108-MCP-RULE--project-one-mcp-tool-per-active-tool.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Project one MCP tool per active Tool

## Claim

### Prose Claim

MCP must expose exactly one callable endpoint for each enabled public Tool name in the installed registration configuration, backed by its canonical code handler and request/result contract. Source-only providers have no public endpoint. Reject duplicate public identities and preserve canonical operation meaning. No current Atom declaration is required merely to register or list an implemented, configured Tool.

## Details

Expose one stable callable MCP identity for each enabled code-owned provider or selected-route entry in the generated registration asset. Preserve its validated contract without splitting, aliasing, or aggregating it, and reject duplicate public identities or missing configured entries before publication.
