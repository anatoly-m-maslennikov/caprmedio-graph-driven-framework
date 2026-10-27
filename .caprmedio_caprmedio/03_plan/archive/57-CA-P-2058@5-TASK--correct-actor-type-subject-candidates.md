---
atom_id: CA-P-2058@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Actor
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 5
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-1966
tier: 3
---
# Summary

Correct Actor Type Subject candidates

## Objective

Correct the 43 baseline proposals that incorrectly model Actor Types as narrower kinds.

## Details

Estimated own work: 15 minutes. The independent ledger check found 33 Operator → Actor/Operator and 10 AI Agent → Actor/AI Agent proposals. The confirmed candidate identifies Actors by Actor Type plus optional Name and gives Operator/AI Agent as Type values, not narrower kinds.

Read the supplement contract and every owning current source span. Produce supplements/actor_types.review.json with exact coverage of those 43 baseline proposed occurrences only. Use Actor.Type: Operator and Actor.Type: AI Agent when current role meaning is established; otherwise retain unresolved research. Add generic dependent and Actor identity rule basis. Preserve all original occurrence/source/quarantine fields and role distinctions. No instance or Actor Name is invented.

Keep the baseline ledger and frozen reports unchanged. The correction is a derived overlay, not a source edit, semantic acceptance, grammar/native admission or live migration approval. Root verifies it independently and commits the completed Task.

### Completion

All 43 baseline Actor Type correction candidates now have separately reviewed targets: 33 Actor.Type: Operator and 10 Actor.Type: AI Agent. CA-P-2072 independently accepted the original 36 supported rows; CA-P-2085 and its independent review supplied the seven remaining generic Operator meanings. Their disjoint union exactly covers the original selection and all 43 source hashes remain current. Evidence: `semantic-reviews/task-2058.accepted-subset.json` and `task-2058.receipt.json`. The raw supplement and original Subjects remain unchanged; this is not migration approval.

### Definition of Done

Not Done if selection/evidence is incomplete or stale, Type values are treated as subtypes, names are invented, unrelated rows or sources change, unresolved work is hidden, or own work exceeds 15 minutes without decomposition.
