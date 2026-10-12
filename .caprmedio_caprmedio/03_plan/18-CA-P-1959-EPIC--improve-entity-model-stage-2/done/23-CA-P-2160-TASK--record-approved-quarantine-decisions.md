---
atom_id: CA-P-2160
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Atom
  depends_on: [Subject, Revision, Carrier, Operator, Plan]
version: 1
updated_at: "2026-10-11 14:39:13 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  depends_on: [CA-P-2158]
---
# Summary

Record approved quarantine decisions

## Objective

The actual Operator choices for legacy Atom IDs and timestamp serialization are recorded without inventing selector approval.

## Details

Own work: at most fifteen minutes. Record the actual reply and exact audited input pins; update the current Epic checkpoint. Keep captured reports and original Core unchanged.

## Completion

Recorded the Operator's choice to migrate the six legacy IDs to new canonical IDs and to use quoted timestamps with explicit UTC offsets. The selector question remains open because the Operator requested an explanation. Evidence: `_projection/core-entity-review/stage2/operator.quarantine-decisions.2026-10-11.json`. This Task records decisions only; no successor ID was allocated, timestamp policy adopted, original source changed, or source migration performed.

### Definition of Done

Not Done if the recorded choices differ from the actual reply, selector approval is inferred, current input pins are stale, historical evidence or source contents change, or a decision record is presented as an execution receipt.
