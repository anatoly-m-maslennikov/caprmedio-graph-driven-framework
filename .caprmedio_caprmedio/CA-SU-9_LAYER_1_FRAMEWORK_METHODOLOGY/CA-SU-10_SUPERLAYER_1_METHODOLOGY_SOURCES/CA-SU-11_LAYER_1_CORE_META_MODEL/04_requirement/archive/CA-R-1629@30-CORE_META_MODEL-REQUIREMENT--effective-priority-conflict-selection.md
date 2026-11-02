---
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Concern.Priority'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern'
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 30
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1629@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Effective priority conflict selection

## Scope

priority-conflict selection for Concern Atoms.

## Claim

a Concern Atom has **`=1`** Priority value: High, Medium, **or** Low.

direct comparison of Concern Atoms **must** follow the admissible Operator-selected priority model governed by CA-R-1487:

- use the selected model, its effective parameters, **and** its active criteria.
- Scope Unit ancestry **must not** add an implicit Priority increment.
- **if** the model **or** its application does **not** justify a selection, leave the conflict unresolved **and** ask the Operator.

the Framework Instance Settings Artifact exposes **`=2`** selection modes:

- `ask_always`, the default, explains the conflict **and** asks the operator; **and**
- `auto_by_effective_priority`, which **may** select **only** one uniquely eligible winner.

the selection mode **must** ask the Operator **if** ties, incomparable structure, uncertainty, **or** multiple winners occur. mutually unsatisfiable external obligations stop for Operator **or** external resolution. PRMEDO Tier precedence, deterministic replacement, explicit scoped override, stale-view routing, **and** Implementation drift follow their own semantics rather than this selection mode.

## Details
