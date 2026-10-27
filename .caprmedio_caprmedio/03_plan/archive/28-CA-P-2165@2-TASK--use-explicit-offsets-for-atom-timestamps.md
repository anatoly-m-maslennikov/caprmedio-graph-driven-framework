---
atom_id: CA-P-2165@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 28
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Atom
  depends_on:
  - Subject
  - Carrier
  - Revision
  - Operator
  - Plan
version: 2
updated_at: 2026-10-11 18:29:23 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-2160
  - CA-P-2158
---
# Summary

Use explicit offsets for Atom timestamps

## Objective

The approved selector and metadata changes have the exact, verified effect assigned to this Task.

## Details

Own work: at most fifteen minutes; create bounded children if this own-work limit is exceeded. Align CA-D-390 with the approved quoted explicit-offset format while keeping local/UTC/IANA timezone configuration. Fix operative timestamp formatting if needed. Repair the two audited naive current timestamps as actual new updates with exact Version +1; preserve old naive bytes/history rather than guessing old offsets. Use simple ad-hoc repairs, not a general repair framework. Verify affected code/policies/carriers and record exact effects.

Root owns Git, Plan lifecycle and shared Journal recording. Workers are not alone; preserve unrelated release changes. Scratch and caches stay in `.caprmedio_tmp`; use uv. No unsupported MCP/FPF, general migration framework, runtime/release activation or Step 2 body sweep.

### Completion

Completed the3 approved source revisions, exact predecessors and9 actual Journal records, and the configured offset/quotation emitters. Independent source/static code checks and Root's171 targeted tests passed, including graph Settings and carrier edge cases. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2165.receipt.json`.

### Definition of Done

Not Done if the assigned effect is unverified, source pins are stale, Atom and atom are conflated, unrelated work changes, exact prior source history is lost, execution evidence is fabricated, or completion claims exceed the assigned increment.
