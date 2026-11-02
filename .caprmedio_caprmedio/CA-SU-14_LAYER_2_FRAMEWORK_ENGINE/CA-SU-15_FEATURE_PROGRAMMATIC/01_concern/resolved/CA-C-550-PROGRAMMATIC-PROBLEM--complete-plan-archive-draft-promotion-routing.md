---
atom_id: CA-C-550
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2484, CA-P-2491]
version: 4
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Complete Plan archive Draft promotion routing

## Concern

Independent review of the unaccepted P2484 resolver snapshot found two uncovered Draft promotion branches. Existing same-ID Plan promotion to Archived still derives local destination/history, conflicting with flat publication and its expected history verification. ID-free Plan promotion to Archived loses the constructed canonical filename because status destination derives its stem from the Draft Atom instead.

## Evidences

Reviewed atom_operations SHA-256 e4e3660fea2fb2f27da3345f3564b588451c768fb067d811b2ff50e18aca9733 and lifecycle_intents 4bf3ab19b6079f38cfcff6af664dedc2904929ec54f2c258de9b5fe9f2d9017f. The affected existing-promotion destination/history helpers are near lines 706-772; the new status archive branch near lifecycle line 936 ignores its supplied filename from fresh promotion near 1884. This is source-review evidence, not a deployed incident or live-data failure. Root retains P2484 Active and P2491 Backlog pending shared-owner completion and independent functional proof.

## Blast radius

Only the new flat Plan archive routing and its existing/fresh Draft promotion paths. Do not weaken identity, filename, Version, source/currentness or history verification to hide the mismatch. Reuse the exact canonical filename and Version already bound by promotion and the shared archive/preservation owner; non-Plan and unrelated Status behavior remains unchanged. C549 retained-history directory location is a separate unresolved Question.

## Resolution

Source implementation is independently accepted at atom_operations 537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284, lifecycle_intents 9e8f56400d8141f1e190f19dd499f2a39dd6346330e383d46ea7be1067107f0d and archive test d31a8c68673f8a71cad59e41060d91d7739fb3fcbdd6b7b2c372daac6c04c29e. Final native71/71 and independent code review APPROVE include exact predecessor placement and cleanup rollback. One Status-predecessor owner replaces the mismatched calculations; no source/history check was weakened. Earlier positive receipts did not waive the uncovered branch. This resolves this bounded source defect, not installed-runtime adoption, the missing recursive caller under C551/P2494, release or held-batch replay. C549 is answered.

### Carrier placement correction

Place this Resolved Concern under the owning role resolved/ directory according to applicable Status Delivery. Preserve the exact previous carrier as history; this correction does not reopen the decision or claim runtime implementation.
