---
atom_id: CA-M-399@3
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Business Workflow Lifecycle Recording
  depends_on: []
relations:
  child_of: [CA-M-426]
  relates_to: [CA-M-414, CA-R-1095, CA-M-396, CA-M-397]
---
# Summary

Record business Workflow lifecycle separately from technical diagnostics

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Keep technical diagnosis on structured stdout/stderr streams and record actual business Workflow lifecycle events through the declared Journal owner, without turning a technical warning into a business event.

## Details

1. Emit technical diagnostics through the shared logger with the actual Project prefix and sanitized context. The Docker runtime captures these streams under its bounded retention/back-pressure configuration; use stderr when stdout carries MCP/Tool protocol or result data.
2. Apply CA-M-396 and CA-M-397 to severity: input and Project artifact issues use WARNING; ERROR is reserved for real blocking runtime failures. Do not confuse a response error or a failed business Workflow with ERROR-level logging.
3. For an actually admitted/started business Workflow, record its observed started, failed and completed lifecycle transitions, as applicable, through its executor and the shared Journal owner. A technical cause may explain a real business failure without copying technical log records or stack traces into the Journal.
4. A preflight rejection with no admitted/started business Workflow must not fabricate a Workflow, Run, started/failed event or completion event. Direct read-only Tool calls do not gain hidden Journal effects from logging or generic error handling.
5. Keep business records truthful and independent from Git and technical-log retention. Journal incompleteness is not an admission gate. Preserve existing historical Journal bytes and do not rewrite old technical entries as part of this Method.
