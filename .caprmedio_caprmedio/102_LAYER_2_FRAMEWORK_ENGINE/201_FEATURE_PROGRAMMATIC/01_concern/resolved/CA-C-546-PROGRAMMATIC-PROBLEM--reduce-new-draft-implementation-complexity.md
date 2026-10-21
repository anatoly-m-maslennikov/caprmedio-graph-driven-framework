---
atom_id: CA-C-546
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2477, CA-P-2478]
version: 3
updated_at: "2026-10-20T20:11:04.671Z"
---
# Summary

Reduce new Draft implementation complexity

## Concern

Configured Ruff C901 output for the Draft increment includes new complex functions and increased complexity in touched dispatch paths; describing the whole output as pre-existing baseline debt is incorrect. Preserve the implemented guards while reducing new complexity through small cohesive extractions, not suppression or broad unrelated cleanup.

## Evidences

P2477 has removed all newly complex function findings: the frozen production files now report 12 C901 findings versus the 13-finding HEAD baseline. Root independently checked finding identities and exact function values. Two already-complex touched functions still increased: _run_create 13 to 14 and update_atom_action 61 to 71. P2478 is an explicit Backlog follow-up; this Problem remains Active for that residual debt. Do not report configured Ruff as clean or the two values as unchanged baseline. Static correctness review found no actionable defect in the frozen code; final test receipts remain separate evidence.

Root compared the same configured Ruff against exact HEAD source via stdin: atom_operations had 8 C901 findings and lifecycle_intents had 5. The reviewed working snapshot had 17 total, including newly complex recovery, publication, rename and preflight paths. P2477 owns the bounded correction, with regression and independent review required. Functional native 8/8 and owner promotion golden 22/22 results do not by themselves close this source-quality Problem.

## Blast radius

Maintainability and reviewability of changed Draft execution/recovery paths. This evidence does not assert a new production incident, authorize a release, or justify changing unrelated legacy behavior.

### Resolution checkpoint

P2478 completes the specific residual debt: _run_create is 13 and update_atom_action is 61, exactly their c75724811 configured C901 scores. Root checked each function identity/value, with no new/worsened C901 key; 12 inherited findings remain versus original 13, so this is not a global lint-clean claim. Exact strict lifecycle-only comparison also has no newly introduced diagnostic after precise marker/history annotations; 28 inherited diagnostics are tracked separately in C548. Final frozen independent acceptance passed 124/124: native promotion 8, semantic assessment 7, Draft promotion golden 22, Atom cohort 30, selected lifecycle 48 and version history 9. Every final receipt is a fresh run bound before/after to atom_operations SHA-256 4d25dae0e7efb8e6d36755902af1ae11178d18a982f54d6a926e7aa71d11d31e, lifecycle_intents 568516545c8bbd870d9022d157bcdb6382a394da46420458251cd341a7aff4ea and shared fixture 79925d47d09c43a524bab2cb0928460e0dad308b009029743a3db6059daf92be. Independent exact-diff review passed. P2488 repaired only the frozen D288/D378 materialization gap; exact HEAD reproduced the prior failure set. No production guard relaxation, live port, MCP effect, Docker, release, deployment, migration or held-batch replay. C547 fixture failure is independently resolved; C533 runtime adoption remains Active.
