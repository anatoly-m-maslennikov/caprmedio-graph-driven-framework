---
identity:
  atom_id: CA-D-678@5
  ref_id: CA-D-678@5
context:
  container:
    scope_unit: CA-SU-15
  role: Delivery
  form: Decision
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  tier: 5
relations:
  delivery_for:
  - CA-R-2785
  depends_on:
  - CA-M-473
state:
  status: Archived
  version: 5
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-D-678@5-PROGRAMMATIC-DECISION--store-the-generated-mcp-discovery-catalog.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/07_delivery/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Store the generated MCP discovery catalog

## Claim

Store the generated catalog at `.caprmedio_runtime/mcp/tools_catalog.json` in the selected Project. Its JSON has `updated_at`, `root` and `groups`. `root` is a list of tool descriptors. `groups` maps Workspaces, Views, Queries and Service to descriptor lists. The Service group includes the named `workbench_reread` tool. Each tool descriptor retains its actual MCP name, description, schemas and annotations; each descriptor occurs once.

Provide the host script `FEATURE_MCP/generate_tools_catalog.py --project-root <root> --mcp-url <url>` beneath PROGRAMMATIC. It obtains the complete native tool list from the new MCP without invoking a tool, groups it by the Method, writes the runtime catalog and exits nonzero on failure. Add this script after MCP replacement/readiness and before successful completion of the existing local-release command. Do not bypass its tests or create a second release command.

`discover_tools` with an empty `request` returns that generated catalog through its existing canonical provider. Keep the existing name and request wrapper; do not introduce `tools_discovery` as another tool or alias. Non-empty source-discovery selectors retain their existing contract.

## Sources

CA-R-2785; CA-M-473.


## Local release integration

Start the selected installed package through the existing Project bootstrap at `.caprmedio_runtime/start_mcp.py`. The bootstrap provisions its locked MCP dependencies in `.caprmedio_runtime/launcher-venv`; do not run the package launcher in an empty unsynchronized package environment. Keep the selected source package and no-build boundary, and require the running image to match the already tested candidate.

After MCP is ready, run its installed catalog generator with that provisioned launcher interpreter. Do not create a second virtual environment inside the copied package. A startup or catalog-generation failure stops release completion and keeps the useful diagnostic output available.
