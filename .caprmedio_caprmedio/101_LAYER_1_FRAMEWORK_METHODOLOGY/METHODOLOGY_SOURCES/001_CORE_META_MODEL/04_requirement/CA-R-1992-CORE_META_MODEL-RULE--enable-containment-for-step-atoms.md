---
atom_id: CA-R-1992
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-1945
version: 9
updated_at: 2026-10-26 17:20:40 +0400
tier: 3
type: Rule
---
# Summary

Enable containment for Step Atoms

## Scope

Containment capability of Step Atoms, including nested substeps.

## Claim

`Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms. a containing Step with substeps has no own Action launch.

## Details

A substep is a nested Step, not a separate Type. a leaf Step, including a leaf substep, launches **exactly one** referenced reusable Action with its parameters **and** input bindings; a containing Step owns its nested substeps and launches no Action of its own. Containment is optional and can nest. This permission does not change a Step's Action reference or input bindings, prescribe how internal tool calls are modeled, or introduce a storage layout or execution protocol.
