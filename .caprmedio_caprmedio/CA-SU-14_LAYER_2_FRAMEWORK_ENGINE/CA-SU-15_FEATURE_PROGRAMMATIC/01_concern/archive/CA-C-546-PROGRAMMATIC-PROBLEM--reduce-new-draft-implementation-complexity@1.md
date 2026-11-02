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
  concern_about: [CA-P-2401, CA-P-2477]
version: 1
updated_at: "2026-10-20T18:54:09.573Z"
---
# Summary

Reduce new Draft implementation complexity

## Concern

Configured Ruff C901 output for the Draft increment includes new complex functions and increased complexity in touched dispatch paths; describing the whole output as pre-existing baseline debt is incorrect. Preserve the implemented guards while reducing new complexity through small cohesive extractions, not suppression or broad unrelated cleanup.

## Evidences

Root compared the same configured Ruff against exact HEAD source via stdin: atom_operations had 8 C901 findings and lifecycle_intents had 5. The reviewed working snapshot had 17 total, including newly complex recovery, publication, rename and preflight paths. P2477 owns the bounded correction, with regression and independent review required. Functional native 8/8 and owner promotion golden 22/22 results do not by themselves close this source-quality Problem.

## Blast radius

Maintainability and reviewability of changed Draft execution/recovery paths. This evidence does not assert a new production incident, authorize a release, or justify changing unrelated legacy behavior.
