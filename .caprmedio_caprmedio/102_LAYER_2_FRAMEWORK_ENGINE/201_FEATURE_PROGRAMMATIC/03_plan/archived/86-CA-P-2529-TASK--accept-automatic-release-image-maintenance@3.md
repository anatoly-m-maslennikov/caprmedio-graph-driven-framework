---
atom_id: CA-P-2529
content_role: Plan
type: Plan
label: Task
work_sequence_number: 86
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-21T10:46:47Z"
---
# Summary

Accept automatic release image maintenance

## Objective

Accept automatic release image maintenance.

## Details

Review the frozen cleanup/caller/test/contract closure independently and run focused release/image functional checks in Project Temporary State. Cover negative cases and canonical version/date naming. Record exact results and retained-image reasons, then update dependent work. At most 15 minutes own work; split before extending. No actual Docker deletion, build/start, deployment, full release, version bump, push, new Workflow or duplicate historical-retag implementation.

### Current reviewed checkpoint

P2528's post-green ordering and positive-launcher proof are accepted with root59/59 checks and independent APPROVE. Retention policy code/active contracts are still held by C563's host-wide versus selected-Project scope decision. Keep this final retention acceptance Backlog until P2526/P2527 complete; no whole-feature or runtime completion claim.

### Acceptance activated after implementation freeze

P2530/P2531 implementation checks and root integrated102/102 gate pass16.084s. P2527 caller/helper integration is frozen; final independent code review and final frozen focused rerun belong here. Review Project-only complete ownership, exact candidate rather than fingerprint retention, selected exact-prior replacement, reference protection, green-suite/verified-smoke ordering and failure reporting. Native Docker, deployment/full release, version bump and push remain excluded. Root local_release.py retains the same4 inherited Ruff diagnostics and run_local_release C90159; the other6changed Python files pass. Do not claim whole-repository lint or release readiness.
