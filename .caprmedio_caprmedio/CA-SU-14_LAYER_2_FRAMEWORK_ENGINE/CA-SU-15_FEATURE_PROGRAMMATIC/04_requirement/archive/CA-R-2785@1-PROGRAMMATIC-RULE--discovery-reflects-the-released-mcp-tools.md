---
atom_id: CA-R-2785
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
updated_at: 2026-11-05 13:04:02 +0400
carrier_destination:
  file:
    name: CA-R-2785@1-PROGRAMMATIC-RULE--discovery-reflects-the-released-mcp-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
---

## Summary

Discovery reflects the released MCP tools

## Claim

The root discovery catalog must include the released MCP tools, their actual names, descriptions and input/output schemas, without inventing an executable capability. It keeps `discover_tools` at the root and groups Query tools under Queries, Worksheet tools under Worksheets and runtime maintenance under Service. Existing unrelated tools remain discoverable at the root; grouping does not remove them or change callable names.

Regenerate the catalog on each local release so added, removed and changed tools are reflected. A local release is not complete when its catalog generation fails. The catalog respects the exposed tool frontier, including its blacklist and quarantine decisions, and does not execute tools or Workflows. This generated catalog describes the released registry; it is not proof that every tool will succeed for every Project request.
