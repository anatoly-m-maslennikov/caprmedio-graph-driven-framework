---
atom_id: CA-P-2048
content_role: Plan
type: Plan
label: Task
work_sequence_number: 55
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 2
updated_at: "2026-10-11 03:45:48 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
  depends_on: [CA-P-2047]
---
# Summary

Apply the Substance decision to Subject mappings

## Objective

Align the exact legacy Claim field with the Operator-confirmed shared Substance field.

## Details

Estimated own work: 15 minutes. Required prerequisites: CA-P-2047 and persisted current ledger. Use the supplement contract. Recheck all 143 exact Atom/Claim occurrences across 142 source files and preserve source-specific evidence. Produce supplements/substance.review.json and a small ad-hoc support script with isolated tests. All 143 proposed values are Atom.Substance; 137 baseline candidates change and 6 were already aligned. Preserve every other occurrence, compound Claim path, source Content Role, quarantine finding and original byte. No live source write. Root independently accepts and commits the Task.

### Definition of Done

Not Done if assigned coverage or evidence is missing/stale, a meaning is guessed, unresolved work is hidden, Core or frozen evidence changes, an approval is inferred, tests fail, or own work exceeds 15 minutes without decomposition.

### Completion evidence

Created and independently accepted the exact 143-row bare Claim overlay from 142 pinned sources: all targets are Atom.Substance; 137 baseline candidates change and six were already aligned. The other 63 Claim-bearing rows remain excluded. Six isolated tests and live structural/evidence checks pass; a second write refuses overwrite. Independent meaning review confirms source roles and Operations body labels are preserved. The real receipt is `_projection/core-entity-review/stage2/task-2048.receipt.json`. Original Subjects, bodies and frozen evidence remain unchanged.
