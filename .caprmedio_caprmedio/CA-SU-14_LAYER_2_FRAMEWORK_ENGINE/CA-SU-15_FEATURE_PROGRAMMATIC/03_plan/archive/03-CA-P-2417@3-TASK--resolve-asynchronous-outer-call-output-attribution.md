---
atom_id: CA-P-2417@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Scope Unit
  - Property
  - Tool
  - Workflow
relations:
  is_decomposition_of:
  - CA-P-2402
version: 3
updated_at: 2026-10-24 06:04:41 +0400
tier: 3
---
# Summary

Resolve asynchronous outer-call output attribution

## Objective

Complete one bounded evidence/safety prerequisite for the scoped five-day MCP audit without treating incomplete evidence as a completed operation.

## Details

Review the immutable release-v1 exec candidates and raw source references. Follow functions.exec Script running cell IDs through actual functions.wait invocations and terminal outputs, preserving one-to-many/ambiguous associations rather than counting intermediate notices as completion. Correlate direct MCP event IDs when proven, distinguish nested loops/dynamic invocations and quoted/read-only wrapper text, and emit a bounded association table under async-pairs/**. No MCP execution or effect replay is allowed. Return exact attribution gaps to the direct-event collector.

Use a Luna worker and at most15minutes own work. Split any longer responsibility into a separately recorded bounded subtask before continuing. Historical analysis is MCP-call-only; this Task does not authorize implementation fixes, deployment or production tests. Manual permission covers planning records only, not Concern/source writes. All actual runtime reproductions require the verified disposable nonproduction harness.

### Definition of Done

The assigned evidence or fixture result has reproducible source references, exact observed outcomes and honest gaps; independent acceptance checks pass or blockers are recorded without effects being replayed. Production remains untouched. Planning checkpoint: Completed async attribution for 90 outer calls with 124 embedded candidates: 28 terminal and 62 explicitly ambiguous, zero pending. Only 24 outer calls have uniquely proven direct-event associations; 240 native events are observed. These are associations, not 240 extra canonical calls or proof of effects. Reports: .caprmedio_tmp/mcp-audit-20261020/async-pairs/. No MCP execution or replay occurred.
