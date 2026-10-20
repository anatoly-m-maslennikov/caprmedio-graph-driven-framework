---
atom_id: CA-C-546
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2477, CA-P-2478]
version: 2
updated_at: "2026-10-20T19:02:19.988Z"
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
