---
atom_id: CA-P-2046
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
updated_at: "2026-10-11 03:01:46 +0400"
relations:
  is_decomposition_of: [CA-P-2043]
---
# Summary

Prepare the current Subject ledger script

## Objective

Prepare one small ad-hoc script that combines independently accepted reviews without changing their decisions or source Atoms.

## Details

Estimated own work: 15 minutes. This preparation is independent of unfinished review Tasks; actual ledger integration remains CA-P-2045's work and requires all 51 review Tasks Done. Own only stage2/support/integrate_current_subject_reviews.py and its isolated tests. Reuse verify_current_inventory.py and verify_current_subject_reviews.py. Check all input pins, report and receipt pins, exact source/finding/occurrence coverage, Done Plan identities and decomposition, confidence and no-executable invariants. Retain quarantines and unresolved rows. Refuse stale, missing, duplicate, conflicting or incomplete evidence; no semantic mapping is inferred.

Default is read-only preview. Explicit persistence creates only the derived ledger below stage2, refuses overwrite or symlinks, and never touches authority. Root owns actual integration, Plan lifecycle and Git. No reusable Tool registration, migration framework, Core/body/grammar/native changes, MCP, FPF or runtime work. Tests must reject an unfinished Plan, stale receipt, missing or duplicate occurrence, and overwrite attempts. Use uv and .caprmedio_tmp scratch. Keep the frozen candidate and captured snapshot unchanged.

Completion: nine isolated failure/success tests passed; independent read-only code review found no blocking gate defect. The live default preview verified all 51 Done review Tasks, 907 sources, 4534 occurrences and all receipt/source/evidence pins. Eight quarantined sources and 2097 unresolved rows remain visible. No real ledger or source was written. Receipt: stage2/task-2046.receipt.json. Actual integration remains CA-P-2045's work.

### Definition of Done

Not Done if the script or required checks are missing, fail to expose incomplete evidence, write authority, bypass a later gate, or exceed 15 minutes without decomposition.
