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
  concern_about: [CA-P-2513, CA-P-2514]
version: 1
updated_at: "2026-10-21 04:52:56 +0400"
---
# Summary

Align Plan predecessor test expectations with flat archive placement

## Concern

The complete local-release suite found an uncovered stale test expectation after the canonical flat Plan archive increment. A release cannot pass while its golden fixture expects the superseded Plan predecessor destination.

## Evidences

During local-20261021-mcp-health-verified-env, ATOM_UPDATE/tests/test_subject_intent_materialization.py test_intent_exact_shape_hash_and_old_metadata_proposal failed: expected 03_plan/archive but actual predecessorArchive is 03_plan/archived. Read-only Luna diagnosis confirms atom_operations shared Plan resolver and current D461/E502 require the latter. A second read-only scan identifies WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply_portfolio.py paths() using archive for both Plan and Requirement; only its Plan branch is likely stale. That second module has not yet supplied a failure receipt at publication. Intentional retained legacy archive fixtures are not migration targets.

## Blast radius

P2514 owns only the two named test expectation sites after the running full suite ends. Preserve Requirement archive, byte-exact retained-history assertions, native admission and production code. Independently review the diff and rerun both focused modules plus a narrow adjacent check. P2513 then requires a fresh complete normal release gate; no failing receipt is waived or reused as acceptance. The original production MCP remains unchanged and no held Run or uncertain call is replayed.
