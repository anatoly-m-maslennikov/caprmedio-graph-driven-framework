---
atom_id: CA-P-1609@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 65
current_scope_unit: caprmedio
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/MCP
  depends_on:
  - Subject/Engineering/Tool
  - Subject/Engineering/MCP
  - Subject/Engineering/Action
  - Subject/Engineering/Workflow
  - Subject/Engineering/Evaluation
version: 6
updated_at: 2026-10-25 00:53:45 +0400
relations:
  is_decomposition_of:
  - CA-P-1137
  blocks:
  - CA-P-1527
  - CA-P-1528
tier: 3
---
# Summary

Expose registered query routes in discovery

## Objective

Within <=15 minutes, align discovery availability with the two query MCP names already registered by selected_routes. Own implementation_server.py and the focused registration/discovery tests only. Preserve existing Tool schemas, route identities and the single server.

## Details

Read-only diagnosis found the current Service exposed set omits find_and_fetch_artifacts and find_and_fetch_journal_events. An isolated Service test with fabricated exposure is not sufficient; the implementation registration surface must be tested. Preserve parallel source-binding and query-proof edits. No live reload, runtime start, host dependency provisioning, denied-operation retry, FPF or harvesting. Root owns the receipt, mechanical commit and later live-generation check.

## Definition of Done

Focused tests verify the actual server exposure includes both already-registered query routes. Saved source pins and exact engine changes are retained without calling source tests immutable-image or client-cache acceptance.

## Result

Done: implementation_server.py reuses QUERY_ROUTE_NAMES from the existing selected route registry when constructing discovery's exposed set. No new Tool route, schema, manifest pin or acceptance frontier was introduced. The real stdio server test copies current active D551/D557 bindings into a disposable Project, opens a cacheless Client, confirms both read-only registered names and discovers exactly both as MCP-available. All 3 focused MCP workflow tests pass in the existing development worker with current mounted source.

Root accepted the minimal registry-derived source delta after reading its exact diff. py_compile and diff checks pass. Candidate gateway fingerprint is 677e2f34b80b3f6aa3637dcedea7cd0b8af05b633666fdfe2ec632c5d0d727b6. No live reload, current Codex client-cache acceptance or immutable-image test was performed by this Task; the earlier image build does not include this subsequent Engine integration change.
