---
atom_id: CA-P-2692
ref_id: CA-P-2692
container:
  atom: CA-P-2683
role: Plan
form: Plan
label: Task
topics:
  main_subject: Entity
tier: 4
status: Done
version: 4
updated_at: 2026-10-29 11:24:13 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
## Summary

Retire superseded contracts after preserving their meanings

## Objective

Retire superseded sources only after their useful meaning and necessary consumers have been handled.

## Details

Stage 3 cleanup, per replacement group. Preserve definitions/constraints still needed by the Model before archiving an obsolete Current source. Reuse or split them into the appropriate adopted Definitions; repair affected direct relations and Subject consumers within this Epic's scope.

Reconcile duplicate/obsolete atoms and stale Graph Rule, Revision, Code/Implementation-wrapper, Resources or old Relation contracts only where the selected frontier actually contains them and the adopted replacement covers their useful meaning. A retired name alone is not evidence that every old Claim is useless.

Preserve historical archived versions and unrelated Drafts. Do not edit their contents as part of the migration. Mark superseded preparation as non-promotable. Do not wait for all unrelated R formalization when one replacement group and its consumers are already complete; do not archive first and hope to recover meaning later.

If a necessary consumer is in the separate Engine scope, record the exact dependency and coordinate that work rather than editing Engine sources here or concealing a broken link.

## Definition of Done

Each selected superseded source has a documented replacement/preservation/retention disposition, no useful operative meaning is lost, and required in-scope consumers are repaired. Necessary external dependencies are explicit; no broken required dependency is hidden by closure.

## Progress

Retirement is complete for this boundary: 24 superseded canonical sources and 17 malformed legacy carriers have recorded dispositions. Eight legacy meanings have canonical retained replacements; nine obsolete legacy meanings use existing authority. Useful relation, Claim, namespace-independence and representation meanings were preserved and Current native consumers repaired. Archives preserve the previous accepted versions without artificial archive-only Version bumps.
