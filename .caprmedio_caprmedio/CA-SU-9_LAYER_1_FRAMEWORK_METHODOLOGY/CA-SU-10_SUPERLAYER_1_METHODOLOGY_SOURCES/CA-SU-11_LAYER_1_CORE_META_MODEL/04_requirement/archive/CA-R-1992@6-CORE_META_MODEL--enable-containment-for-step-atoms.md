---
atom_id: CA-R-1992@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-1945
version: 6
updated_at: 2026-10-24 01:37:42 +0400
tier: 3
type: Rule
---
# Summary

Enable containment for Step Atoms

## Scope

Containment capability of Step Atoms, including nested substeps.

## Claim

`Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms.

## Details

A substep is a nested Step, not a separate Type. Containment is optional and can nest. This permission does not change a Step's Action reference or input bindings, prescribe how internal tool calls are modeled, or introduce a storage layout or execution protocol.
