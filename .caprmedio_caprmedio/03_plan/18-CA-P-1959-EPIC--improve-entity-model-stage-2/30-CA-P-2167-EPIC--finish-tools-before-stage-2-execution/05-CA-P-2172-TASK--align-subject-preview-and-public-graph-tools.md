---
atom_id: CA-P-2172
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Projection, Plan]
version: 1
updated_at: "2026-10-12 04:02:18 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2174]
---
# Summary

Align Subject preview and public graph Tools

## Objective

The existing preview and public graph entry point follow their independently verified updated contracts.

## Details

Own work: none. Each child requires its corresponding actual current contract packet independently accepted under CA-P-2171; it need not wait for an unrelated application packet. Complete the two disjoint implementation children and their focused checks; preparation or historical parser tests do not finish this group. Reuse existing mechanisms. Preserve source pins, graph ownership, legacy/default behavior, case and the standalone apply guard. No original Core write occurs.

### Decomposing Plans

- [CA-P-2175 — Select current originals in Subject preview](05-CA-P-2172-TASK--align-subject-preview-and-public-graph-tools/01-CA-P-2175-TASK--select-current-originals-in-subject-preview.md)
- [CA-P-2176 — Bind the public graph notation profile](05-CA-P-2172-TASK--align-subject-preview-and-public-graph-tools/02-CA-P-2176-TASK--bind-the-public-graph-notation-profile.md)

### Definition of Done

The Plan is **not** Done if a child is not Done, implementation predates independent contract acceptance, contracts/implementation pins differ, focused checks fail or safeguards/legacy behavior regress.
