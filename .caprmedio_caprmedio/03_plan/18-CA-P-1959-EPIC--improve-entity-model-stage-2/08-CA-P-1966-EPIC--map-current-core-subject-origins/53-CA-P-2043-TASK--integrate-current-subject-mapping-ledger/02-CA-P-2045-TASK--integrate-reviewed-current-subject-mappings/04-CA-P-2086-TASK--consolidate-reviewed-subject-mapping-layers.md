---
atom_id: CA-P-2086
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Tool, Operator]
version: 1
updated_at: "2026-10-11 06:34:06 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
---
# Summary

Consolidate reviewed Subject mapping layers

## Objective

One complete working ledger incorporates actual reviewed progress and exposes every remaining gap.

## Details

Estimated own work: at most 15 minutes. Read and follow `_projection/core-entity-review/stage2/working-ledger.contract.md` and the latest parent Epic boundaries. Prepare the one-off consolidation script and a complete derived working ledger under the working-ledger contract. Reuse strict current-source parsing; do not repair carriers or build a reusable migration engine. Independent checker/evidence audits may run in parallel; consume fresh grammar re-review if ready, otherwise keep those changed-source rows null. Own only stage2/support/consolidate_reviewed_mappings.py and stage2/working-ledger/ generated drafts.

This is implementation/preparation evidence, not original Source writes, selector grammar adoption, native admission or final migration approval. Preserve Core Subjects and ordinary content, frozen baseline and raw reports, unrelated edits and existing guarded mutation route. No MCP/FPF/runtime. Root owns integration, independent acceptance, Plan lifecycle and a commit after completion; workers are not alone. Work beyond the bound gains child Tasks before continuation.

### Definition of Done

Not Done if assigned output/checks are missing, source/current-evidence pins or exact coverage fail, guesses or unresolved findings are hidden, priority/lineage is unsupported, any authority/captured output changes, or own work exceeds 15 minutes without decomposition.
