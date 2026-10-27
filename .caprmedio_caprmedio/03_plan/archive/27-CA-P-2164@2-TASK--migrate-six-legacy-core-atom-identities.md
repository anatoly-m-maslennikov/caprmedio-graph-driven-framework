---
atom_id: CA-P-2164@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 27
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
updated_at: 2026-10-11 18:01:19 +0400
relations:
  is_decomposition_of:
  - CA-P-1959
  depends_on:
  - CA-P-2160
  - CA-P-2158
---
# Summary

Migrate six legacy Core Atom identities

## Objective

The approved selector and metadata changes have the exact, verified effect assigned to this Task.

## Details

Own work: at most fifteen minutes; create bounded children if this own-work limit is exceeded. Use a small ad-hoc source-pinned migration to assign six fresh collision-free CA IDs to the six audited legacy originals. Preserve exact predecessors/history and explicit old/new lineage. Repair only current authored references genuinely affected; do not rewrite frozen reports, archived history or derived copies as authority. Keep Summary, Substance and Subjects unchanged apart from necessary identity references. Record actual effects, verify identity uniqueness and commit separately.

Root owns Git, Plan lifecycle and shared Journal recording. Workers are not alone; preserve unrelated release changes. Scratch and caches stay in `.caprmedio_tmp`; use uv. No unsupported MCP/FPF, general migration framework, runtime/release activation or Step 2 body sweep.

### Completion

Migrated all six approved legacy original IDs to fresh CA-R-1932 and CA-E-620–624, incrementing each Version exactly once; relinked the single live CA-R-1677 dependency. All seven exact prior carriers are preserved and independently checked. Bodies, Subjects and other metadata are unchanged; 21 actual Journal events record the effects. Current inventory has two remaining timestamp quarantines, not six legacy-ID quarantines. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2164.receipt.json`.

### Definition of Done

Not Done if the assigned effect is unverified, source pins are stale, Atom and atom are conflated, unrelated work changes, exact prior source history is lost, execution evidence is fabricated, or completion claims exceed the assigned increment.
