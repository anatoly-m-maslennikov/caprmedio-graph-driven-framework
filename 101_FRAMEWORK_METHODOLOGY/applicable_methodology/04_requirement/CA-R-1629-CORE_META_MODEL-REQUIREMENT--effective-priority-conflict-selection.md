---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Concern.Priority"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Concern", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Project.Framework Settings", "Entity/Continuant/Actor/Type: Operator"]
version: 25
updated_at: "2026-10-16 12:08:36 +0000"
relations: {}
atom_id: "CA-R-1629"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1629-CORE_META_MODEL-REQUIREMENT--effective-priority-conflict-selection.md
  source_atom_id: CA-R-1629
  source_atom_revision: 25
  source_sha256: 5c6065b35280263646f3d0a96c4f839c96e68374b2131a7c54cc2c0b75002fba
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
