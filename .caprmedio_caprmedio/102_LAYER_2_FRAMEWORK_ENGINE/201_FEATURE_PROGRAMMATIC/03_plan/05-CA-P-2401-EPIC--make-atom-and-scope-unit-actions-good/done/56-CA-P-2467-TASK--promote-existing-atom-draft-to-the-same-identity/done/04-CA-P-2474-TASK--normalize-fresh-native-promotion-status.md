---
atom_id: CA-P-2474
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2467]
version: 3
updated_at: "2026-10-20T18:48:25.120Z"
---
# Summary

Normalize fresh native promotion Status

## Objective

Before complete-carrier validation, native role-only and ID-free Draft promotion must materialize Active Status together with its fresh canonical ID.

## Details

At most 15 minutes own work; split before extending. Independent validator diagnosis reproduced canonical atom_id with stale Draft status in prepare_draft_promotion, correctly rejected as DRAFT_ID_INVALID. Fix the shared native fresh-output boundary, never weaken the validator. Existing-marker destination/recovery work remains P2472 and no-op is mutation-free.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified execution checkpoint

P2472 focused destination/bundle and recovery checks passed, freeing the shared production-file owner. Normalize only fresh native promotion output to Active before complete-carrier validation; preserve strict Draft marker rules, allocator and Version/time behavior. P2470 final matrix follows this correction.

### Verified execution checkpoint

Native fresh role-only and ID-free promotions now materialize Active before complete-carrier validation through one fresh preparation helper. Root reviewed the narrow normalization/caller change; native 8/8 and owner promotion golden 20/20 passed, with strict validation unchanged. Parent acceptance still requires P2475 and the independent P2470 matrix.
