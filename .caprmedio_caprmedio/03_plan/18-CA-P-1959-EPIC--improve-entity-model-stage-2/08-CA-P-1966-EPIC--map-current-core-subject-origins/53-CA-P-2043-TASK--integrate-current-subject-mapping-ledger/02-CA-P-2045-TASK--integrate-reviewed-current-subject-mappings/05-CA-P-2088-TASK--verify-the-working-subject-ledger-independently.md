---
atom_id: CA-P-2088
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
  depends_on: [Atom, Subject, Projection, Plan, Tool, Operator]
version: 2
updated_at: "2026-10-11 06:46:55 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
---
# Summary

Verify the working Subject ledger independently

## Objective

The complete derived working ledger is checked independently, with incorrect data rejected.

## Details

Estimated own work: at most 15 minutes. Read and follow `_projection/core-entity-review/stage2/working-ledger.contract.md` and the latest parent Epic boundaries. Prepare independent current-frontier/layer-priority verification and isolated wrong-output checks without importing the producer. Own only stage2/support/verify_working_mapping_ledger.py and its test_working_mapping_ledger.py. Test preparation is ready before the live output; later execute against the completed derived ledger. No producer/source/report/Plan/Git edits.

This is implementation/preparation evidence, not original Source writes, selector grammar adoption, native admission or final migration approval. Preserve Core Subjects and ordinary content, frozen baseline and raw reports, unrelated edits and existing guarded mutation route. No MCP/FPF/runtime. Root owns integration, independent acceptance, Plan lifecycle and a commit after completion; workers are not alone. Work beyond the bound gains child Tasks before continuation.

### Definition of Done

Own work is exhausted. This is now a group with no further own implementation. The remaining acceptance gap is delegated to [CA-P-2091 — Reject omitted mapping layers in independent verification](05-CA-P-2088-TASK--verify-the-working-subject-ledger-independently/01-CA-P-2091-TASK--reject-omitted-mapping-layers-in-independent-verification.md). It remains Active until the child and independent live checks pass; an earlier partial draft/test pass is not completion.

Not Done if assigned output/checks are missing, source/current-evidence pins or exact coverage fail, guesses or unresolved findings are hidden, priority/lineage is unsupported, any authority/captured output changes, or own work exceeds 15 minutes without decomposition.
