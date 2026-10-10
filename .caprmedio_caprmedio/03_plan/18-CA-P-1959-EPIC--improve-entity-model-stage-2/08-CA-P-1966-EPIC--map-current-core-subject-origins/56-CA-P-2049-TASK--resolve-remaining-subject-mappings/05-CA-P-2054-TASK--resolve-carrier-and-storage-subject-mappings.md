---
atom_id: CA-P-2054
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-11 03:20:22 +0400"
relations:
  is_decomposition_of: [CA-P-2049]
---
# Summary

Resolve carrier and storage Subject mappings

## Objective

Determine candidate targets for the 114 assigned unresolved Subject occurrences from current evidence.

## Details

Estimated own work: 15 minutes. Read the supplement contract and the exact carriers ownership entry in current-subjects.research-ownership.json. Scope: 114 occurrences, 90 source files, 63 distinct old values. Pin and read the applicable definitions and every source span supporting a proposed mapping. Resolve repetitive fields using common confirmed rules plus source-specific meaning, not display-string availability. Preserve all qualifiers and source identities. Output .caprmedio_caprmedio/_projection/core-entity-review/stage2/supplements/carriers.review.json. Full assigned coverage includes explicit unresolved rows; unresolved research must remain tracked. If all mapping work cannot fit 15 minutes, return verified partial results and exact remainder for decomposition; do not mark this Task Done or overrun. No Core, Plan, frozen report, Git, MCP/FPF or runtime writes.

### Definition of Done

Not Done if assigned coverage or evidence is missing/stale, a meaning is guessed, unresolved work is hidden, Core or frozen evidence changes, an approval is inferred, tests fail, or own work exceeds 15 minutes without decomposition.
