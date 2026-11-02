---
atom_id: CA-R-1992@13
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains'
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-2478
version: 13
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
---
## Summary

Enable containment for Step Atoms

## Claim scope

Containment capability of Step Atoms, including nested substeps.

## Claim

`Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms. a containing Step with substeps has no own Action launch.

## Details

A substep is a nested Step, not a separate Type. a leaf Step, including a leaf substep, launches **exactly one** referenced reusable Action with its parameters **and** input bindings; a containing Step owns its nested substeps and launches no Action of its own. Containment is optional and can nest. This permission does not change a Step's Action reference or input bindings, prescribe how internal tool calls are modeled, or introduce a storage layout or execution protocol.
