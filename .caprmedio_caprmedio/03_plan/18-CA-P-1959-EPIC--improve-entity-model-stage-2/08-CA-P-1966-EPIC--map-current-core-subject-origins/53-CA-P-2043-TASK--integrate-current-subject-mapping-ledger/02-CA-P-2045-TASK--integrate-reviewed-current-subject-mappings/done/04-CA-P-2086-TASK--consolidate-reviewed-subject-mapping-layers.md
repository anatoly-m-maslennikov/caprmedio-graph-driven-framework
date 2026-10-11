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
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Tool, Operator]
version: 7
updated_at: "2026-10-11 07:08:35 +0400"
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

### Current integration task

[CA-P-2092 — Integrate the accepted current grammar review](../04-CA-P-2086-TASK--consolidate-reviewed-subject-mapping-layers/done/02-CA-P-2092-TASK--integrate-the-accepted-current-grammar-review.md) incorporates the now-accepted CA-P-2087 evidence. That child and its live checks passed; the earlier no-receipt draft remains only historical intermediate evidence.

### Completion

The complete non-executable working ledger consolidates frozen baseline, selected independently accepted reviews and current grammar re-review with exact current coverage and source lineage. All child Tasks and independent checks pass. This bounded integration is Done, but 1526 unresolved occurrences and eight quarantined sources remain for CA-P-1966 and the existing final migration gates. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2086.receipt.json`.

### Definition of Done

Own work is exhausted. This is now a group with no further own implementation. The remaining acceptance gap is delegated to [CA-P-2090 — Reject unexpected source drift in the working ledger](../04-CA-P-2086-TASK--consolidate-reviewed-subject-mapping-layers/done/01-CA-P-2090-TASK--reject-unexpected-source-drift-in-the-working-ledger.md). The child and independent checks are Done; earlier partial draft/test passes did not close this group.

Not Done if assigned output/checks are missing, source/current-evidence pins or exact coverage fail, guesses or unresolved findings are hidden, priority/lineage is unsupported, any authority/captured output changes, or own work exceeds 15 minutes without decomposition.
