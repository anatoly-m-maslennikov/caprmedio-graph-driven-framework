---
atom_id: CA-P-2119
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-11 09:17:26 +0400"
relations:
  is_decomposition_of: [CA-P-2045]
  depends_on: [CA-P-2112, CA-P-2113, CA-P-2114, CA-P-2115, CA-P-2116, CA-P-2117]
---
# Summary

Verify accepted subject-family layers independently

## Objective

Independent checks reject wrong or missing subject-family layers while accepting exact prospective outputs.

## Details

Estimated own work: at most 15 minutes. Follow `_projection/core-entity-review/stage2/working-ledger.followups-2112-2117.contract.md`. Own only support/verify_working_mapping_ledger.py and support/test_working_mapping_ledger.py. Extend the existing independent one-off verifier and its focused tests for the six exact selected layers, without importing the producer. Enumerate current source origins and verify exact selected coverage, accepted report/receipt provenance, layer order, final target/confidence and complete quarantine/lineage preservation. Add valid-control adversarial cases for omitted layer, missing/extra or stale origin, wrong target and bad acceptance pins. No output replacement.

Workers are not alone. Root owns integration, lifecycle and a commit after completion. Preserve original Core, frozen/captured evidence, prior reports, unrelated work and later migration gates. No MCP/FPF/runtime/Tool/source/Git writes by workers. Use uv offline with --no-project; scratch/cache in .caprmedio_tmp. Compile in memory, not source-directory pycache. Decompose work exceeding the bound.

### Definition of Done

Not Done if exact coverage/provenance or independent checks fail, current source/evidence drift is hidden, authority changes, completion exceeds actual evidence, or own work exceeds the bound without decomposition.
