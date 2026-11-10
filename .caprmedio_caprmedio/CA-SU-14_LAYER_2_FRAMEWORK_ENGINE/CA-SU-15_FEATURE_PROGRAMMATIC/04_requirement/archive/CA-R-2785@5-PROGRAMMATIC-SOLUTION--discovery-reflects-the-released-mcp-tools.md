---
identity:
  atom_id: CA-R-2785
  ref_id: CA-R-2785
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  tier: 3
state:
  status: Archived
  version: 5
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-R-2785@5-PROGRAMMATIC-SOLUTION--discovery-reflects-the-released-mcp-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-678
  - CA-M-473
---

## Summary

Discovery reflects the released MCP tools

## Claim

### Prose Claim

The root discovery catalog must include the released MCP tools, their actual names, descriptions and input/output schemas, without inventing an executable capability. It keeps `discover_tools` at the root and groups Workspace tools under Workspaces, Query tools under Queries, View tools under Views and runtime maintenance under Service, including `workbench_reread`. Existing unrelated tools remain discoverable at the root; grouping does not remove them or change callable names.

Regenerate the catalog on each local release so added, removed and changed tools are reflected. A local release is not complete when its catalog generation fails. The catalog respects the exposed tool frontier, including its blacklist and quarantine decisions, and does not execute tools or Workflows. This generated catalog describes the released registry; it is not proof that every tool will succeed for every Project request.

## Details

### Retained catalog delivery support

Store the generated catalog at `.caprmedio_runtime/mcp/tools_catalog.json` in the selected Project. Its JSON has `updated_at`, `root` and `groups`. `root` is a list of tool descriptors. `groups` maps Workspaces, Views, Queries and Service to descriptor lists. The Service group includes the named `workbench_reread` tool. Each tool descriptor retains its actual MCP name, description, schemas and annotations; each descriptor occurs once.

Provide the host script `FEATURE_MCP/generate_tools_catalog.py --project-root <root> --mcp-url <url>` beneath PROGRAMMATIC. It obtains the complete native tool list from the new MCP without invoking a tool, groups it as specified here, writes the runtime catalog and exits nonzero on failure. Add this script after MCP replacement/readiness and before successful completion of the existing local-release command. Do not bypass its tests or create a second release command.

`discover_tools` with an empty `request` returns that generated catalog through its existing canonical provider. Keep the existing name and request wrapper; do not introduce `tools_discovery` as another tool or alias. Non-empty source-discovery selectors retain their existing contract.

#### Sources

CA-R-2785; this requirement.


#### Local release integration

Start the selected installed package through the existing Project bootstrap at `.caprmedio_runtime/start_mcp.py`. The bootstrap provisions its locked MCP dependencies in `.caprmedio_runtime/launcher-venv`; do not run the package launcher in an empty unsynchronized package environment. Keep the selected source package and no-build boundary, and require the running image to match the already tested candidate.

After MCP is ready, run its installed catalog generator with that provisioned launcher interpreter. Do not create a second virtual environment inside the copied package. A startup or catalog-generation failure stops release completion and keeps the useful diagnostic output available.

### Retained catalog generation procedure

After local release has started the new MCP and confirmed readiness, run one script that reads its complete native `tools/list` response, including any pagination, and regenerates the root discovery catalog. Use the existing MCP SDK and actual tool descriptors. Do not maintain a second list of tools or infer availability from source-folder names.

Use `discover_tools` for root discovery. An empty discovery request reads the generated catalog through the existing canonical provider; existing explicit query and Scope Unit selectors keep their declared source-discovery behavior. If the root catalog is missing or invalid, report an explicit error; do not silently rescan, repair, retry or invent a catalog.

Group `workspace_*` tools under Workspaces, `query_*` tools under Queries and `view_*` tools under Views. Group the existing MCP reload/status operations, `<service>_restart` maintenance tools and `workbench_reread` under Service. Put `discover_tools` first at the root; leave unclassified existing tools at the root, sorted by exact name. Every descriptor appears once. This is a discovery tree, not nested callable MCP names.

Preserve actual names, descriptions, schemas and annotations from the SDK. Write the generated JSON through the existing atomic writer, with temporary staging under the selected Project's `.caprmedio_tmp/` and a verified same-filesystem replacement boundary. Do not create a temporary file beside the runtime catalog. A failed write must not expose half JSON. Report generation failures to stderr and fail the release step. Do not add a watcher, another registry, a database, aliases, tool execution or a Business Journal event.

#### Sources

CA-R-2785.
