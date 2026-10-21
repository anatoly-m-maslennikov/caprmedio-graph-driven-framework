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
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 4
updated_at: "2026-10-21T10:50:11Z"
---
# Summary

Accept automatic release image maintenance

## Objective

Accept automatic release image maintenance.

## Details

Review the frozen cleanup/caller/test/contract closure independently and run focused release/image functional checks in Project Temporary State. Cover negative cases and canonical version/date naming. Record exact results and retained-image reasons, then update dependent work. At most 15 minutes own work; split before extending. No actual Docker deletion, build/start, deployment, full release, version bump, push, new Workflow or duplicate historical-retag implementation.

### Earlier reviewed checkpoint

P2528's post-green ordering and positive-launcher proof are accepted with root59/59 checks and independent APPROVE. Retention policy code/active contracts are still held by C563's host-wide versus selected-Project scope decision. Keep this final retention acceptance Backlog until P2526/P2527 complete; no whole-feature or runtime completion claim.

### Acceptance activated after implementation freeze

P2530/P2531 implementation checks and root integrated102/102 gate pass16.084s. P2527 caller/helper integration is frozen; final independent code review and final frozen focused rerun belong here. Review Project-only complete ownership, exact candidate rather than fingerprint retention, selected exact-prior replacement, reference protection, green-suite/verified-smoke ordering and failure reporting. Native Docker, deployment/full release, version bump and push remain excluded. Root local_release.py retains the same4 inherited Ruff diagnostics and run_local_release C90159; the other6changed Python files pass. Do not claim whole-repository lint or release readiness.

### Final acceptance

Independent functional-safety review APPROVE and planning ownership review APPROVE. Root final frozen10-module synthetic gate102/102 passed9.632s after wording/test-name integration; earlier integrated run102/10216.084s is retained independently. The accepted behavior is automatic selected-Project candidate-only retention within normal Local release: canonical naming after the green full suite; image retirement only after exact candidate smoke. Foreign/unowned/in-use resources remain protected and failures remain pending. C564 tracks source-conformance bookkeeping, including stale runner exception and the two test-file size increases; no full E539/global-lint/typing readiness claim. No full release, real Docker mutation, deployment, version bump or push. Next existing Epic backlog remains separate.
