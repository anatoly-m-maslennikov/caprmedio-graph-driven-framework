---
atom_id: CA-P-2119@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
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
  - Operator
version: 3
updated_at: 2026-10-24 06:04:11 +0400
relations:
  is_decomposition_of:
  - CA-P-2045
  depends_on:
  - CA-P-2112
  - CA-P-2113
  - CA-P-2114
  - CA-P-2115
  - CA-P-2116
  - CA-P-2117
tier: 3
---
# Summary

Verify accepted subject-family layers independently

## Objective

Independent checks reject wrong or missing subject-family layers while accepting exact prospective outputs.

## Details

Estimated own work: at most 15 minutes. Follow `_projection/core-entity-review/stage2/working-ledger.followups-2112-2117.contract.md`. Own only support/verify_working_mapping_ledger.py and support/test_working_mapping_ledger.py. Extend the existing independent one-off verifier and its focused tests for the six exact selected layers, without importing the producer. Enumerate current source origins and verify exact selected coverage, accepted report/receipt provenance, layer order, final target/confidence and complete quarantine/lineage preservation. Add valid-control adversarial cases for omitted layer, missing/extra or stale origin, wrong target and bad acceptance pins. No output replacement.

Workers are not alone. Root owns integration, lifecycle and a commit after completion. Preserve original Core, frozen/captured evidence, prior reports, unrelated work and later migration gates. No MCP/FPF/runtime/Tool/source/Git writes by workers. Use uv offline with --no-project; scratch/cache in .caprmedio_tmp. Compile in memory, not source-directory pycache. Decompose work exceeding the bound.

### Completion

The independent verifier admits exactly the third six-report group and rejects complete omission once live receipts exist. All current origins/supporting spans, accepted receipts/final-review hashes, proof fields and earlier gates are preserved. Twenty-three focused tests, a complete 33-layer prospective control and ten wrong-data controls pass. No derived draft or original Core was changed. Exact verification is recorded in `_projection/core-entity-review/stage2/task-2119.receipt.json`.

### Definition of Done

Not Done if exact coverage/provenance or independent checks fail, current source/evidence drift is hidden, authority changes, completion exceeds actual evidence, or own work exceeds the bound without decomposition.
