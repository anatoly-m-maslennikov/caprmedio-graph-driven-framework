---
atom_id: CA-P-2478@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 4
updated_at: 2026-10-24 06:04:44 +0400
tier: 3
---
# Summary

Reduce touched legacy Draft branch complexity

## Objective

Reduce or explicitly justify the retained complexity increases in _run_create (13 to 14) and update_atom_action (61 to 71), without changing behavior or inflating abstractions.

## Details

At most 15 minutes own work; split before extending. P2477 removed all newly complex function findings and reduced configured total C901 from 17 to 12 versus HEAD 13. Two already-complex touched legacy functions still increased; do not call those values unchanged baseline. CA-C-546 retains this residual quality issue. This is follow-up source-quality work, not a correctness or deployment completion claim. Preserve all validated Draft behavior, pins, rollback and transport callers; at most 15 minutes own work, split before extending.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review

The revised Stage 1 Epic and deferred Stage 2 Epic are saved. Execute behavior-preserving cohesive extraction only, using the current PROGRAMMATIC M projection and frozen functional corpus. Preserve guards, error/result shapes, byte pins, currentness, history, no-op and recovery. No lint suppression or unrelated legacy refactor. Root owns records and Git; no runtime changes.

### Verified execution checkpoint

Cohesive extraction restores _run_create 14 to 13 and update_atom_action 71 to 61, exactly their c75724811 scores. Root compared configured Ruff per-function identities/scores: no new or increased finding remains; total remains 12 versus original 13, not globally lint-clean. Precise existing DraftMarker and JSON history annotations remove all new type diagnostics; exact normalized strict comparison is 28 baseline and 28 current. Retained wider typing debt is C548, not resolved by this Task. Final frozen independent acceptance passed 124/124: native promotion 8, semantic assessment 7, Draft promotion golden 22, Atom cohort 30, selected lifecycle 48 and version history 9. Every final receipt is a fresh run bound before/after to atom_operations SHA-256 4d25dae0e7efb8e6d36755902af1ae11178d18a982f54d6a926e7aa71d11d31e, lifecycle_intents 568516545c8bbd870d9022d157bcdb6382a394da46420458251cd341a7aff4ea and shared fixture 79925d47d09c43a524bab2cb0928460e0dad308b009029743a3db6059daf92be. Independent exact-diff review passed. P2488 repaired only the frozen D288/D378 materialization gap; exact HEAD reproduced the prior failure set. No production guard relaxation, live port, MCP effect, Docker, release, deployment, migration or held-batch replay. Dependent P2484 is reviewed against current D461/E502 and remains Backlog for future bounded execution.
