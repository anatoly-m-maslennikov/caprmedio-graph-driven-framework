---
atom_id: CA-A-1323
ref_id: CA-A-1323
container:
  scope_unit: CA-SU-15
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
relations:
  depends_on:
  - CA-R-2729
  - CA-R-2776
  - CA-R-2727
  - CA-M-462
  - CA-M-470
  - CA-D-673
  - CA-D-674
  - CA-E-676
  - CA-E-678
  - CA-R-2785
  - CA-M-473
  - CA-D-678
  - CA-D-512
  - CA-E-525
  - CA-R-1804
  - CA-O-112
status: Done
version: 1
updated_at: 2026-11-05 13:04:02 +0400
carrier_destination:
  file:
    name: CA-A-1323-PROGRAMMATIC-SPECIFICATION_PROPOSAL--refine-mcp-discovery-and-query-execution.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/02_analysis_and_advisory/020_done
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Refine MCP discovery and query execution

## Proposal

Keep the existing callable name `discover_tools`. Show it at the root of a generated catalog with Queries, Worksheets and Service groups. Groups are catalog data; MCP callable names stay flat. Generate this data from the new server's actual `tools/list` as part of every local release, after readiness and before success. Added, removed and changed descriptors are refreshed without a hand-maintained list. Runtime data is `.caprmedio_runtime/mcp/tools_catalog.json`. Existing engine tools outside these groups stay at root. Details are in CA-R-2785, CA-M-473, CA-D-678 and the updated D512/E525 Drafts.

## Query execution

Use one MCP `query_run` call with optional `save=false`, optional non-negative integer `preview`, and optional query `name` when `save=true`. Remove the separate `query_save` tool and `/save` endpoint, without an alias.

Run the selected statement once. When preview is given, use DuckDB's native relation limit to return at most N rows, preserving existing limits, CTEs and graph semantics. Do not rewrite SQL text or replace an existing LIMIT. The exact original selected SQL remains the result's `sql` and the saved SQL; do not expose generated wrapper aliases. Counts and pages describe the previewed result, and preview never silently changes the saved SQL.

Only after successful execution and result delivery preparation may `save=true` append that original SQL through the existing saved-item Journal writer. Run errors create no saved entry. A later save failure returns the completed query result and ID with `outcome: partial` and `save_error`; do not invent a saved ID, claim aggregate success, retry or rollback. Successful combined calls add the existing saved identity and full URL to the ordinary Run response.

Default Run, Check and Page remain non-saving. Query saving in the UI becomes Run & Save through the same operation; there is no save-only query mode. Preserve the optional query name dialog, selected-statement behavior and full local Worksheet script. A save failure keeps the result visible and preserves the previous saved identity and dirty state. Save Worksheet remains the separate whole-script operation; it is not a query-save call. No new preview UI control is included.

## Implementation and verification

Update RMED first, review it against the latest Operator decisions, then adopt it. Compile the applicable Current PROGRAMMATIC M Policies into one implementation prompt. Implement the backend, MCP/HTTP/frontend integration, generated catalog and release hook within exclusive file ownership.

Verify successful/failed Run & Save, partial save failure, exact original SQL preservation, preview of ordinary SQL and GRAPH_TABLE, schema and blacklist behavior, removed query_save exposure, and actual UI Run & Save. Use real MCP/HTTP/browser flows where appropriate and focused native-DuckDB edge cases. Reuse one candidate image and the current test infrastructure; do not create a new query parser, registry, service or release command.

Execution is tracked by CA-P-2710. This proposal does not adopt the separate general Policy changes in CA-A-1322.

## RMED index

- CA-R-2729
- CA-R-2776
- CA-R-2727
- CA-M-462
- CA-M-470
- CA-D-673
- CA-D-674
- CA-E-676
- CA-E-678
- CA-R-2785
- CA-M-473
- CA-D-678
- CA-D-512
- CA-E-525
- CA-R-1804
- CA-O-112
