---
atom_id: CA-P-2101
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
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
updated_at: "2026-10-11 08:00:21 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  depends_on: [CA-P-2094, CA-P-2095, CA-P-2096, CA-P-2097, CA-P-2098, CA-P-2099]
---
# Summary

Verify accepted subject-family layers independently

## Objective

Independent checks reject wrong or missing subject-family layers while accepting exact prospective outputs.

## Details

Estimated own work: at most 15 minutes. Follow `_projection/core-entity-review/stage2/working-ledger.followups-2094-2099.contract.md`. Own only support/verify_working_mapping_ledger.py and support/test_working_mapping_ledger.py. Extend the existing independent one-off verifier and its focused tests for the six exact selected layers, without importing the producer. Enumerate current source origins and verify exact selected coverage, accepted report/receipt provenance, layer order, final target/confidence and complete quarantine/lineage preservation. Add valid-control adversarial cases for omitted layer, missing/extra or stale origin, wrong target and bad acceptance pins. No output replacement.

Workers are not alone. Root owns acceptance, lifecycle and a commit after completion. Preserve all unrelated work, original authority and frozen evidence. No MCP/FPF/runtime or source adoption.

### Completion

The independent ad-hoc verifier requires complete accepted research coverage, exact per-row provenance and final decisions/targets/confidence. Eighteen focused tests pass. Root's complete prospective live ledger and ten deliberately wrong variants confirm acceptance and fail-closed behavior, including omission of all six layers. Historical fixture roots without accepted receipts remain isolated; the real old draft correctly fails until rebuild. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2101.receipt.json`.

### Definition of Done

Not Done if assigned output/checks are missing or stale, selected ownership/provenance or meaning is lost, wrong data passes, original authority changes, completion exceeds actual evidence, or work exceeds the bound without decomposition.
