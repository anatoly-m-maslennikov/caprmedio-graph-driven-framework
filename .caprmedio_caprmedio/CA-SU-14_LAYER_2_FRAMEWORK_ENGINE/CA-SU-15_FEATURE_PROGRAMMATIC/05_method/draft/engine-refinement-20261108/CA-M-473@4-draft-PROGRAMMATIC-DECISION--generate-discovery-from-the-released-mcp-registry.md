---
identity:
  atom_id: CA-M-473
  ref_id: CA-M-473@4-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Decision
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  tier: 4
relations:
  method_for:
  - CA-R-2785
state:
  status: Draft
  version: 4
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-M-473@4-draft-PROGRAMMATIC-DECISION--generate-discovery-from-the-released-mcp-registry.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/draft/engine-refinement-20261108
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Generate discovery from the released MCP registry

## Claim

After local release has started the new MCP and confirmed readiness, run one script that reads its complete native `tools/list` response, including any pagination, and regenerates the root discovery catalog. Use the existing MCP SDK and actual tool descriptors. Do not maintain a second list of tools or infer availability from source-folder names.

Use `discover_tools` for root discovery. An empty discovery request reads the generated catalog through the existing canonical provider; existing explicit query and Scope Unit selectors keep their declared source-discovery behavior. If the root catalog is missing or invalid, report an explicit error; do not silently rescan, repair, retry or invent a catalog.

Group `workspace_*` tools under Workspaces, `query_*` tools under Queries and `view_*` tools under Views. Group the existing MCP reload/status operations, `<service>_restart` maintenance tools and `workbench_reread` under Service. Put `discover_tools` first at the root; leave unclassified existing tools at the root, sorted by exact name. Every descriptor appears once. This is a discovery tree, not nested callable MCP names.

Preserve actual names, descriptions, schemas and annotations from the SDK. Write the generated JSON through the existing atomic writer, with temporary staging under the selected Project's `.caprmedio_tmp/` and a verified same-filesystem replacement boundary. Do not create a temporary file beside the runtime catalog. A failed write must not expose half JSON. Report generation failures to stderr and fail the release step. Do not add a watcher, another registry, a database, aliases, tool execution or a Business Journal event.

## Sources

CA-R-2785.
