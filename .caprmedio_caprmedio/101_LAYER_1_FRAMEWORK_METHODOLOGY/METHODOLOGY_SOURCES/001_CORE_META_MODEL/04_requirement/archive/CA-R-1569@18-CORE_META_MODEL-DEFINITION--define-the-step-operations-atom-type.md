---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Type
version: 18
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1569@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define the Step Operations Atom Type

## Scope

the Step Type of Operations Atoms.

## Claim

the Operations Atom Type Step **means** the Type of an Operations Atom whose Claim defines **`=1`** Workflow node. a leaf Step, including a leaf substep, defines invocation of **`=1`** referenced reusable Action with its parameters **and** input bindings; a containing Step with nested substeps defines no own Action launch.

## Details

- a substep is a nested Step, not a separate Type.
- a Linear Step has ordered nonconditional substeps and no conditional substeps.
- a Conditional Step chooses **exactly one** branch in its own definition from its declared result condition and **may** use Actor input; result-based routing belongs to that definition.
- different Steps **may** reference the same Action with different bindings **without** copying or redefining that Action.
