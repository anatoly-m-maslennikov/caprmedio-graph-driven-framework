---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Type
version: 21
updated_at: 2026-10-29 07:45:27 +0400
relations: {}
atom_id: CA-R-1569@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define the Step Operations Atom Type

## Claim scope

the Step Type of Operations Atoms.

## Claim

the Operations Atom Type Step **means** the Type of an Operations Atom whose Claim defines **`=1`** Workflow node. a leaf Step, including a leaf substep, defines invocation of **`=1`** referenced reusable Action with its parameters **and** input bindings; a containing Step with nested substeps defines no own Action launch.

## Details

- a substep is a nested Step, not a separate Type.
- a Linear Step has ordered nonconditional substeps and no conditional substeps.
- a Conditional Step chooses **exactly one** branch in its own definition from its declared result condition and **may** use Actor input; result-based routing belongs to that definition.
- different Steps **may** reference the same Action with different bindings **without** copying or redefining that Action.
