---
atom_id: "CA-R-1992@draft"
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains"
  depends_on:
  - "Entity/Node/Continuant/Atom.Enabled Relations.Contains"
relations:
  child_of:
  - CA-R-1945
version: 3
updated_at: "2026-10-19 11:43:10 +0000"
---
# Summary

Enable containment for Step Atoms

## Scope

Containment capability of Step Atoms, including nested substeps.

## Claim

`Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms.

## Details

A substep is a nested Step, not a separate Type. Containment is optional and can nest. This permission does not change a Step's Action reference or input bindings, prescribe how internal tool calls are modeled, or introduce a storage layout or execution protocol.
