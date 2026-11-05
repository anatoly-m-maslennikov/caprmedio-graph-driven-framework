---
atom_id: CA-D-678
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
version: 3
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 5
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
relations:
  delivery_for:
  - CA-R-2785
  depends_on:
  - CA-M-473
carrier_destination:
  file:
    name: CA-D-678-PROGRAMMATIC-ENG_DECISION--store-the-generated-mcp-discovery-catalog.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/07_delivery
updated_at: 2026-11-05 16:56:06 +0400
---

## Summary

Store the generated MCP discovery catalog

## Claim

Store the generated catalog at `.caprmedio_runtime/mcp/tools_catalog.json` in the selected Project. Its JSON has `updated_at`, `root` and `groups`. `root` is a list of tool descriptors. `groups` maps Workspaces, Views, Queries and Service to descriptor lists. The Service group includes the named `workbench_reread` tool. Each tool descriptor retains its actual MCP name, description, schemas and annotations; each descriptor occurs once.

Provide the host script `FEATURE_MCP/generate_tools_catalog.py --project-root <root> --mcp-url <url>` beneath PROGRAMMATIC. It obtains the complete native tool list from the new MCP without invoking a tool, groups it by the Method, writes the runtime catalog and exits nonzero on failure. Add this script after MCP replacement/readiness and before successful completion of the existing local-release command. Do not bypass its tests or create a second release command.

`discover_tools` with an empty `request` returns that generated catalog through its existing canonical provider. Keep the existing name and request wrapper; do not introduce `tools_discovery` as another tool or alias. Non-empty source-discovery selectors retain their existing contract.

## Sources

CA-R-2785; CA-M-473.
