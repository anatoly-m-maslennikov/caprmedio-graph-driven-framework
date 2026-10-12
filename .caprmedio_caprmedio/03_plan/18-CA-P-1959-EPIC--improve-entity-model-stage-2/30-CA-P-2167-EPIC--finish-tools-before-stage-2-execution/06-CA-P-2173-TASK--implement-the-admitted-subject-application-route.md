---
atom_id: CA-P-2173
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Revision, Journal, Plan, Operator]
version: 2
updated_at: "2026-10-12 04:12:42 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2174]
---
# Summary

Implement the admitted Subject application route

## Objective

The existing governed mutation boundary can apply an exact sealed Subjects-only packet through its admitted route.

## Details

Own work: none. Required prerequisite: CA-P-2170's actual current application contract packet independently accepted under CA-P-2171; unrelated preview/graph packets need not delay it. CA-P-2177 binds the concrete implementation scope and creates bounded implementation/check children here. Those children and their actual isolated outputs must complete; preparation alone cannot finish this group.

The Operator chose extending the existing admitted MCP update action with Subjects-only application. Implement that route only after its actual current contract packet passes independent acceptance. No local transport exception, completed capability or live migration approval is inferred; the exact CA-P-1910 sealed packet still needs separate approval.

Implement only the accepted application contracts through the existing boundary. Retain the standalone apply guard until the intended admitted route enforces exact approval, pins, source eligibility, Subjects-only bytes, Version/time/history and truthful Journal effects. Do not create a raw internal bypass, broad repair engine or invented runtime/MCP binding. Root owns shared state and Git; one owner controls each mutation scope.

Use valid isolated fixture carriers only. Production Core application stays under CA-P-1910's separately approved exact sealed packet and CA-P-1911's sole execution. A working Tool is not that approval or a live effect receipt.

### Decomposing Plans

- [CA-P-2177 — Prepare bounded admitted application work](06-CA-P-2173-TASK--implement-the-admitted-subject-application-route/01-CA-P-2177-TASK--prepare-bounded-admitted-application-work.md)

### Definition of Done

The Plan is **not** Done if a direct child is not Done, actual implementation/check children are absent, only preparation is complete, admission is missing, a guard is bypassed, isolated effects diverge from contracts, or live approval/effects are inferred from Tool readiness.
