---
atom_id: CA-P-2463
content_role: Plan
type: Plan
label: Task
work_sequence_number: 52
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T17:34:49.405Z"
---
# Summary

Implement edit Draft staging compatibility

## Objective

Emit proposed-version markers and accept legacy @draft in the existing source-pinned Subjects workflow. Acceptance: exact source/predecessor preservation, candidate digest, stale/tamper denial and no-op coverage.

## Details

At most 15 minutes own work; split before extending. Follow the current PROGRAMMATIC M projection and Core07 D276@21, D288@21, D378@16, D446@16, D568@8, D570@12. Preserve unrelated work. Review dependent successors before execution.

### Definition of Done

Emit proposed-version markers and accept legacy @draft in the existing source-pinned Subjects workflow. Acceptance: exact source/predecessor preservation, candidate digest, stale/tamper denial and no-op coverage.

No deployment, live migration/staging, held-batch replay or Methodology map update. Use synthetic golden Projects and nonproduction test instances only.
