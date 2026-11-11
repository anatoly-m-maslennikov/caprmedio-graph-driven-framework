---
atom_id: CA-P-2400
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, "Atom/Status", Journal, Workflow, Operator]
version: 1
updated_at: "2026-10-15 20:33:37 +0000"
relations:
  is_decomposition_of: [CA-P-2387]
---
# Summary

Exclude concurrent native identity publication

## Objective

Keep fresh Atom ID allocation and publication collision-safe when native lifecycle calls run concurrently, without retained-history, Journal or pending-reservation admission prerequisites.

## Details

A threaded native review observed two ID-free Draft promotions both apply the same fresh CA-R-1876 to different carriers (created9901 and created9902). This is a native-path safety defect; the present connected MCP DBOS queue has concurrency one, so this observation does not establish a concurrent MCP exploit. CA-C-524 is reserved for the discovered Problem and will be authored/resolved only against truthful observed state.

Use project runtime identity exclusion for the actual allocation/publication interval and verify simultaneous native callers cannot publish one ID twice. Preserve source/currentness/permission/schema checks, fresh unused IDs, exact actual predecessor history and truthful partial failures. Do not reintroduce removed Draft-history/head/lineage or Journal gates, fabricate past records, add a second identity authority or replay effects.

Estimated own work: at most 15 minutes. Root owns integration; the native implementation owner and independent reviewer have distinct responsibilities. After the result, review the pending CA-P-2389/2390 verification inputs before continuing. This Task stays Active until the actual concurrency regression and independent acceptance are complete.

## Definition of Done

The final native identity path has observed positive/negative concurrency regression results and independent acceptance at exact code pins. Any OS restriction or remaining failure is recorded separately. Focused tests alone do not establish installed runtime activation, connected MCP concurrency, a full suite or parent completion.
