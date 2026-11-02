---
atom_id: CA-C-550
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2484, CA-P-2491]
version: 1
updated_at: "2026-10-20T20:33:20.216Z"
---
# Summary

Complete Plan archive Draft promotion routing

## Concern

Independent review of the unaccepted P2484 resolver snapshot found two uncovered Draft promotion branches. Existing same-ID Plan promotion to Archived still derives local destination/history, conflicting with flat publication and its expected history verification. ID-free Plan promotion to Archived loses the constructed canonical filename because status destination derives its stem from the Draft Atom instead.

## Evidences

Reviewed atom_operations SHA-256 e4e3660fea2fb2f27da3345f3564b588451c768fb067d811b2ff50e18aca9733 and lifecycle_intents 4bf3ab19b6079f38cfcff6af664dedc2904929ec54f2c258de9b5fe9f2d9017f. The affected existing-promotion destination/history helpers are near lines 706-772; the new status archive branch near lifecycle line 936 ignores its supplied filename from fresh promotion near 1884. This is source-review evidence, not a deployed incident or live-data failure. Root retains P2484 Active and P2491 Backlog pending shared-owner completion and independent functional proof.

## Blast radius

Only the new flat Plan archive routing and its existing/fresh Draft promotion paths. Do not weaken identity, filename, Version, source/currentness or history verification to hide the mismatch. Reuse the exact canonical filename and Version already bound by promotion and the shared archive/preservation owner; non-Plan and unrelated Status behavior remains unchanged. C549 retained-history directory location is a separate unresolved Question.
