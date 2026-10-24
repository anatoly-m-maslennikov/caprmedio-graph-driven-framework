---
atom_id: CA-C-552
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
  concern_about: [CA-P-2491, CA-P-2493, CA-P-2496]
version: 4
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Unify promotion and publication history paths

## Concern

Existing-marker Draft promotion predicts predecessor history with a different policy from the shared Status publisher. Non-Plan promotion can expect archive/ while publication writes archived/; nested Plan non-Archived targets can also diverge. Postcondition failure occurs after publication, and recovery lacks the actual history path. The unaccepted increment must not be treated as complete.

## Evidences

Independent static review of atom_operations SHA-256 64f8917a57cf9e0a8e0149bf29cbe165e49781f5fb8d0ca0056a645d07106fde found _existing_promotion_history_path delegating to preserved_revision_destination, while _publish_status_atom_revision independently chooses status history paths. Root confirmed the mismatch in the exact call path. The 68 passing native singleton tests do not cover the non-Plan marker branch or nested Plan non-Archive history and do not waive this finding. No live or production mutation was attempted.

## Blast radius

P2496 owns the smallest shared Status-history calculation and its use in expected/actual publication and recovery. Preserve non-Plan established spelling and flat Plan predecessor preservation, exact old bytes, source pins, no-op and collision handling. Functional tests must include non-Plan marker promotion to Active, nested Plan promotion to Done, and cleanup failure with an exact unchanged file frontier after rollback. P2493 final native/Subject acceptance is withdrawn until the new source freeze; frozen validator-only acceptance remains independently valid. No automatic replay, new modes, deployment or migration.

## Resolution

Source implementation is independently accepted at atom_operations 537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284, lifecycle_intents 9e8f56400d8141f1e190f19dd499f2a39dd6346330e383d46ea7be1067107f0d and archive test d31a8c68673f8a71cad59e41060d91d7739fb3fcbdd6b7b2c372daac6c04c29e. Final native71/71 and independent code review APPROVE include exact predecessor placement and cleanup rollback. One Status-predecessor owner replaces the mismatched calculations; no source/history check was weakened. Earlier positive receipts did not waive the uncovered branch. This resolves this bounded source defect, not installed-runtime adoption, the missing recursive caller under C551/P2494, release or held-batch replay. C549 is answered.

### Carrier placement correction

Place this Resolved Concern under the owning role resolved/ directory according to applicable Status Delivery. Preserve the exact previous carrier as history; this correction does not reopen the decision or claim runtime implementation.
