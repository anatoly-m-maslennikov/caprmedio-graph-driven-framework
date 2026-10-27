---
atom_id: CA-P-2088@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Atom
  - Subject
  - Projection
  - Plan
  - Tool
  - Operator
version: 8
updated_at: 2026-10-24 06:04:11 +0400
relations:
  is_decomposition_of:
  - CA-P-2045
tier: 3
---
# Summary

Verify the working Subject ledger independently

## Objective

The complete derived working ledger is checked independently, with incorrect data rejected.

## Details

Estimated own work: at most 15 minutes. Read and follow `_projection/core-entity-review/stage2/working-ledger.contract.md` and the latest parent Epic boundaries. Prepare independent current-frontier/layer-priority verification and isolated wrong-output checks without importing the producer. Own only stage2/support/verify_working_mapping_ledger.py and its test_working_mapping_ledger.py. Test preparation is ready before the live output; later execute against the completed derived ledger. No producer/source/report/Plan/Git edits.

This is implementation/preparation evidence, not original Source writes, selector grammar adoption, native admission or final migration approval. Preserve Core Subjects and ordinary content, frozen baseline and raw reports, unrelated edits and existing guarded mutation route. No MCP/FPF/runtime. Root owns integration, independent acceptance, Plan lifecycle and a commit after completion; workers are not alone. Work beyond the bound gains child Tasks before continuation.

### Current integration task

[CA-P-2093 — Verify the accepted current grammar layer independently](../05-CA-P-2088@8-TASK--verify-the-working-subject-ledger-independently/done/02-CA-P-2093-TASK--verify-the-accepted-current-grammar-layer-independently.md) incorporates the now-accepted CA-P-2087 evidence. That child and its live checks passed; the earlier no-receipt draft remains only historical intermediate evidence.

### Completion

Independent full-frontier, baseline/current lineage, selected layer priority, final outcome and per-row provenance verification passes for the persisted working ledger. All child Tasks and 14 negative/control tests pass. This closes the working-ledger verification group, not complete semantic mapping or live source adoption. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2088.receipt.json`.

### Definition of Done

Own work is exhausted. This is now a group with no further own implementation. The remaining acceptance gap is delegated to [CA-P-2091 — Reject omitted mapping layers in independent verification](../05-CA-P-2088@8-TASK--verify-the-working-subject-ledger-independently/done/01-CA-P-2091-TASK--reject-omitted-mapping-layers-in-independent-verification.md). The child and independent checks are Done; earlier partial draft/test passes did not close this group.

Not Done if assigned output/checks are missing, source/current-evidence pins or exact coverage fail, guesses or unresolved findings are hidden, priority/lineage is unsupported, any authority/captured output changes, or own work exceeds 15 minutes without decomposition.
