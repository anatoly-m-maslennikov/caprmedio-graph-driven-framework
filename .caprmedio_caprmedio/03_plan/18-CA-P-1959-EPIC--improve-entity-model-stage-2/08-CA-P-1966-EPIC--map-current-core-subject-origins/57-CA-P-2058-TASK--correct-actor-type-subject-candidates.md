---
atom_id: CA-P-2058
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Actor, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-11 03:23:03 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
---
# Summary

Correct Actor Type Subject candidates

## Objective

Correct the 43 baseline proposals that incorrectly model Actor Types as narrower kinds.

## Details

Estimated own work: 15 minutes. The independent ledger check found 33 Operator → Actor/Operator and 10 AI Agent → Actor/AI Agent proposals. The confirmed candidate identifies Actors by Actor Type plus optional Name and gives Operator/AI Agent as Type values, not narrower kinds.

Read the supplement contract and every owning current source span. Produce supplements/actor_types.review.json with exact coverage of those 43 baseline proposed occurrences only. Use Actor.Type: Operator and Actor.Type: AI Agent when current role meaning is established; otherwise retain unresolved research. Add generic dependent and Actor identity rule basis. Preserve all original occurrence/source/quarantine fields and role distinctions. No instance or Actor Name is invented.

Keep the baseline ledger and frozen reports unchanged. The correction is a derived overlay, not a source edit, semantic acceptance, grammar/native admission or live migration approval. Root verifies it independently and commits the completed Task.

### Definition of Done

Not Done if selection/evidence is incomplete or stale, Type values are treated as subtypes, names are invented, unrelated rows or sources change, unresolved work is hidden, or own work exceeds 15 minutes without decomposition.
