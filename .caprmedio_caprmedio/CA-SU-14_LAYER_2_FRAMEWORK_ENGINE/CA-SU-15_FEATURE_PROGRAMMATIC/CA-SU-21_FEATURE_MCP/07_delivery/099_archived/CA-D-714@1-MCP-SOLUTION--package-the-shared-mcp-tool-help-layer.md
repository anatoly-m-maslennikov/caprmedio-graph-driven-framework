---
atom_id: CA-D-714
ref_id: CA-D-714@1
container:
  scope_unit: CA-SU-21
role: Delivery
form: Solution
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 3
relations:
  delivery_for:
  - CA-R-3065
  - CA-M-548
status: archived
version: 1
updated_at: 2026-11-11 00:16:05 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-D-714@1-MCP-SOLUTION--package-the-shared-mcp-tool-help-layer.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/099_archived
---

## Summary

Package the shared mcp tool help layer

## Claim

### Prose Claim

The installed MCP package carries the shared help layer and the canonical schema, short descriptions and examples generated with the same `tool_registry.json` used for public registration. The packaged layer provides tool-specific `help: true` output without normal business inputs or Tool execution, while preserving trusted Project binding and global and Project exclusions. Provider additions use the existing inventory and registry generation path, without a central Tool-name allowlist or duplicate per-Tool handcrafted help descriptions. Registry generation and help rendering do not execute capabilities, run queries or Workflows, write source, invoke business gates or create business Journal Runs; technical diagnostics may be recorded.

The generated public input schemas carried by the package admit the `help: true` shape and any required Project envelope without normal business-required fields, before protocol schema rejection and help dispatch.
