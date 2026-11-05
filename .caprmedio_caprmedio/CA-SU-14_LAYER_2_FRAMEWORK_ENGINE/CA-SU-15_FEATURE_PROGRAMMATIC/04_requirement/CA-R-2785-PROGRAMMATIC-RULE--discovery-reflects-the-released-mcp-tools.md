---
atom_id: CA-R-2785
ref_id: CA-R-2785
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
version: 3
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
carrier_destination:
  file:
    name: CA-R-2785-PROGRAMMATIC-RULE--discovery-reflects-the-released-mcp-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
updated_at: 2026-11-05 16:56:06 +0400
container:
  scope_unit: CA-SU-15
---

## Summary

Discovery reflects the released MCP tools

## Claim

The root discovery catalog must include the released MCP tools, their actual names, descriptions and input/output schemas, without inventing an executable capability. It keeps `discover_tools` at the root and groups Workspace tools under Workspaces, Query tools under Queries, View tools under Views and runtime maintenance under Service, including `workbench_reread`. Existing unrelated tools remain discoverable at the root; grouping does not remove them or change callable names.

Regenerate the catalog on each local release so added, removed and changed tools are reflected. A local release is not complete when its catalog generation fails. The catalog respects the exposed tool frontier, including its blacklist and quarantine decisions, and does not execute tools or Workflows. This generated catalog describes the released registry; it is not proof that every tool will succeed for every Project request.
