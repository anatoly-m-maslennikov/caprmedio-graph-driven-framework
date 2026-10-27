---
atom_id: CA-P-2172@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-24 06:12:24 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2174
tier: 3
---
# Summary

Align Subject preview and public graph Tools

## Objective

The existing preview and public graph entry point follow their independently verified updated contracts.

## Details

Own work: none. Each child requires its corresponding actual current contract packet independently accepted under CA-P-2171; it need not wait for an unrelated application packet. Complete the two disjoint implementation children and their focused checks; preparation or historical parser tests do not finish this group. Reuse existing mechanisms. Preserve source pins, graph ownership, legacy/default behavior, case and the standalone apply guard. No original Core write occurs.

### Decomposing Plans

- [CA-P-2175 — Select current originals in Subject preview](../05-CA-P-2172@6-TASK--align-subject-preview-and-public-graph-tools/done/01-CA-P-2175-TASK--select-current-originals-in-subject-preview.md)
- [CA-P-2176 — Bind the public graph notation profile](../05-CA-P-2172@6-TASK--align-subject-preview-and-public-graph-tools/done/02-CA-P-2176-TASK--bind-the-public-graph-notation-profile.md)

### Implementation checkpoint

Both children are Done. [Independent preview/graph verification](../../../_projection/core-entity-review/stage2/tools-first/preview-graph-verification.md), committed at `980ab9371`, records the exact tested snapshot. The final preview implementation/independent fixture pins are `cc67263b7e91650c42e95a7bd933b8af45b03f072176bdfd0e81e7f8391c01e4` / `089c2015dc678f14b036f0eb8cd4a94c749c497604ba2c248f72e30617306a0e`; their changes were captured in concurrent commit `9a40b76e3`. `tools_first_verifier` passed the final review and Root's complete UPDATE suite passed 49 checks. Public graph commit `a8da9b50b` passed independent review, 245 graph checks and four MCP descriptor checks.

This completes the bounded preview/graph increment, not CA-P-2174, application implementation or live migration/runtime readiness. Later intent/materialization edits must be independently verified; this receipt preserves the accepted snapshot.

### Definition of Done

The Plan is **not** Done if a child is not Done, implementation predates independent contract acceptance, contracts/implementation pins differ, focused checks fail or safeguards/legacy behavior regress.
