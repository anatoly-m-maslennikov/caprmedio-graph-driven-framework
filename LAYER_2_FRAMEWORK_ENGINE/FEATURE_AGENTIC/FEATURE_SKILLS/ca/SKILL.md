---
name: ca
description: "Query Project Atoms and use Workbench through the shared CAPRMEDIO MCP. Use for $ca, /ca, or CAPRMEDIO requests."
---

# CA

Use the host-configured shared CAPRMEDIO MCP as a thin client. Prefer its Workbench tools for querying and browsing. MCP owns schemas, execution and storage; keep implementations and connection configuration outside this Skill.

## Project binding

- Take `project_root` only from the explicit trusted Codex session Project context, and carry that value unchanged.
- Never infer the root from the Skill installation path (it may be shared or symlinked), a prefix, server working directory or Git ancestor. If a nested working folder has no exact trusted Project root, ask for clarification or use an explicit local Project declaration; never guess, silently switch or fall back.
- Every call, including Workbench queries and Workspace/View tools, carries the same outer `project_root`. Preserve the advertised payload shape: Workbench tools use their own top-level arguments, not a generic `request` wrapper. The server validates the binding; it grants no filesystem permission. A returned internal mount path is metadata, not a replacement for the trusted caller root.
- Pin the original `project_root` through pagination and Workspace operations, even if another Codex session changes its working folder. Do not mutate a global `currentProject`. On an unknown or mismatched root/binding, refuse without cross-Project fallback.

## Workbench queries and reads

- Use advertised `query_schema`, `query_check`, `query_run` and `query_page` directly. These data tools need no Workflow discovery, execution context or native Run. Verify actual responses before claiming success.
- Inspect `query_schema` before constructing SQL. Use its current table and column names; quote identifiers with spaces or dots. A saved query may use an older schema. On a column-binding error, inspect the schema and correct the query within the requested scope.
- Use `query_run` for read queries with explicit selection and bounded output. Set `save: false` unless saving is requested. Page with `query_page` using the returned `query_id`, `offset` and `page_size`. A preview can limit the selection; it does not prove full coverage.
- Check `workbench_status` when source freshness matters. Use `workbench_reread` when an index refresh is needed, then rerun the query: reread invalidates retained query IDs. An expired or unknown query ID requires a new read query, not replay of a source mutation.
- Use `query_saved_list` / `query_load` for saved SQL and `query_log_list` / `query_log_get` for prior query outcomes. Loading SQL does not execute it; a query log is not an Atom lifecycle Journal.

## Workspaces and Views

- Use `workspace_list`, `workspace_get`, `view_list` and `view_get` for existing Workspace/View metadata. Listing or reading a Workspace does not activate its UI.
- For requested Workspace UI work, use advertised `workspace_open` with the native session ID explicitly supplied by the host. Keep its returned Workspace binding. Never invent a session ID or reuse another chat's Workspace as the current chat's.
- Use the advertised View check, run, fetch and editing tools when needed for the requested View work. Check a View's SQL against the current schema; preserve expected revisions for edits. Keep unrelated Views unchanged.
- A successful tool bridge ping establishes connectivity only. Claim native UI rendering only when observed. Restart Workbench only for an explicit restart request or a necessary, authorized recovery; a SQL error alone does not call for a restart.

## Current boundary

The MCP interface is Workbench-only. Legacy discovery, Atom mutation and Workflow execution endpoints are retired. Do not substitute Workbench SQL or its row hashes for source mutation APIs or source-byte evidence.

Subject projection builders and local/public release remain separate host commands. Updating this file does not refresh an installed Skill or a running MCP server; verify the runtime's advertised tools before claiming availability.
