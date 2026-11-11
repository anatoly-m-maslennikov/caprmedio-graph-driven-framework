---
atom_id: CA-C-557
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
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2513, CA-P-2514, CA-P-2515, CA-P-2516]
version: 2
updated_at: "2026-10-21T01:02:51Z"
---
# Summary

Align Plan predecessor test expectations with flat archive placement

## Concern

The complete local-release suite found an uncovered stale test expectation after the canonical flat Plan archive increment. A release cannot pass while its golden fixture expects the superseded Plan predecessor destination.

## Evidences

During local-20261021-mcp-health-verified-env, ATOM_UPDATE/tests/test_subject_intent_materialization.py test_intent_exact_shape_hash_and_old_metadata_proposal failed: expected 03_plan/archive but actual predecessorArchive is 03_plan/archived. Read-only Luna diagnosis confirms atom_operations shared Plan resolver and current D461/E502 require the latter. A second read-only scan identifies WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply_portfolio.py paths() using archive for both Plan and Requirement; only its Plan branch is likely stale. That second module has not yet supplied a failure receipt at publication. Intentional retained legacy archive fixtures are not migration targets.

The suite also confirmed Plan Done/Backlog portfolio path mismatches. Two status-bundle modules fail because the generic primary fixture declares no owner for amber, while independent predecessor assertions/collision and fault-injection targets still use nested Plan history. Two independent read-only reviews confirm exact-owner fail-closed production and flat shared Plan history match D461/E502; recovery guards are not to be weakened. W04 fixture lookup uses an obsolete Plan archive target, and its status matrix separately reports Plan Draft preview blocked by mismatched declared/observed selected-binding digests. The latter remains under bounded fixture diagnosis; expected matrix29/8/8 is not changed. At this checkpoint six failing module reports are known; full collection is still running.

## Blast radius

P2514 owns the intent/portfolio expectation pair; P2515 owns exact owner setup and flat Plan history targets in the two status-bundle modules; P2516 owns W04 fixture paths/fresh binding diagnosis. All are separate bounded Tasks with exclusive test/fixture files and wait for the current full run to finish. Preserve Requirement archive, Operations/Step local history, deliberate legacy bytes, exact recovery snapshots, injected-fault reachability, native admission, currentness guards and matrix totals. Independent review and fresh focused/full-release checks are required. No gate is waived, production behavior changed or held/uncertain Run replayed.
