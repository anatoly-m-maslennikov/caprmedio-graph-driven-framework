---
atom_id: CA-P-1956
content_role: Plan
type: Plan
label: Task
work_sequence_number: 16
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Atom, Plan]
version: 2
updated_at: "2026-10-10 04:39:00 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1937]
---
# Summary

Repair captured frontier and Metamodel meaning

## Objective

Correct two further false missing-meaning findings while preserving the historical joined review.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Input receipts: CA-P-1928 and CA-P-1931 are already Done. Use only captured Core commit `a971d0e00c33c779f485fc8cad63194894d440fb` through `nodes/support/snapshot_sources.py`; the Operator selected this snapshot, not live Core.

Correct Source Frontier Digest in batch 0 from CA-O-153@2 lines 42 onward and CA-O-155@2 lines 42–44. Correct CAPRMEDIO Metamodel in batch 3 from CA-R-917@17 line 29, which constrains recursive Scope Unit governance. Meaningful bounded constraints support retaining these unchanged identities; do not require universal definitions, native taxonomy admission or replacement proof. Preserve any separate owner/display question as unresolved presentation context, not absence of meaning.

Own only these two corrected rows and added evidence/provenance in `nodes/nodes.batch-0.review.json` and `nodes/nodes.batch-3.review.json`, the nonempty-quote guard in `nodes/support/verify_node_reviews.py`, and a temporary helper. Preserve every other authored row and exact raw quotation. Batch 3 is a post-join review revision: the original join output and its child-row fidelity receipt remain in immutable Git history. Record its exact prior SHA/commit and row correction; do not pretend that the corrected packet still reproduces the historical join verbatim. Do not revise the completed child Plans or split review files.

All five corrected checks need distinct target-specific findings and exact captured evidence. Reject whitespace-only evidence quotations so a blank source line cannot substantiate a positive decision. Validate the two batches and the corrected guard; root keeps all Git mutations exclusive.

No Core, Subjects, baseline, design, history, runtime, MCP or FPF changes, deletions, adoption or native relation inference. You are not alone; preserve others. Use uv only and apply_patch for authored edits. Below 90% confidence, keep a specific unresolved question rather than deciding.

### Completion receipt

Final review: nodes/nodes.batch-0.review.json; SHA-256: ddf86b359ce07e59966d94d16540b9013fbb303a02420acefa6542b5009d8b7d.

Final review: nodes/nodes.batch-3.review.json; SHA-256: 127d2eccd6477057f251178c73604c9b884c8ae72183cbba4b87c894b40ec800.

Both bounded corrected identities passed independent captured Main Content review by fact_contract. Batch 0: 62 identities, 54 retain, 3 consolidation proposals, 2 generalization proposals, 3 questions and 58 exact evidence spans. Batch 3: 80 identities, 75 retain, 5 questions and 97 spans. All other authored rows and prior evidence remain unchanged. Batch-3 historical child provenance remains exact; its explicit post-join correction does not claim unchanged join reproduction. The new whitespace-only quote guard passed a negative probe, rejecting an empty quotation before source evidence could substantiate a decision. No source, Subject, baseline or native fact change occurred.

### Definition of Done

the Plan is **not** Done **if** ((either named row falsely describes evidenced meaning as absent) **or** (any corrected retain lacks exact nonempty captured evidence and five substantive checks) **or** (an original identity, unaffected row, source pin or genuine display uncertainty is lost) **or** (post-join correction is presented as unchanged historical join reproduction) **or** (batch checks, quote-guard check or independent meaning review fail) **or** (the bounded scope is exceeded)).
