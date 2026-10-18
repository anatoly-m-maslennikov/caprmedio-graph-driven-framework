---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Concern.Priority"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Concern", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Project.Framework Settings", "Entity/Continuant/Node/Actor/Type: Operator"]
version: 26
updated_at: "2026-10-18 03:33:46 +0400"
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
  source_atom_revision: 26
  source_sha256: eb5bb19bdf61b0e144f4b7aa1a17efb43329fe5f9f9f20cac9bd2138c1faaac5
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
