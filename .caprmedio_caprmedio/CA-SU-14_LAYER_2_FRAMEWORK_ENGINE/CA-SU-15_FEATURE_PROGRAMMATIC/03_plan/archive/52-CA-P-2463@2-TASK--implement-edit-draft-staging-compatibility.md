---
atom_id: CA-P-2463@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 52
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 2
updated_at: '2026-10-20T18:53:15.332Z'
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

### Verified execution checkpoint

ID-free, role-qualified/version-qualified emission and legacy reviewed-input compatibility are implemented with exact packet/source/Draft bindings and original Status restoration. P2471, P2473 and P2476 completed the reviewed optional-ID and all-format Version checks. Focused 16, contract 5, workflow 10, frozen-source 9 and manifest 4 checks passed; independent staging review reports no actionable defect. Complete child/history folder hierarchy moves with this Done Task. No held Drafts were staged or published.
