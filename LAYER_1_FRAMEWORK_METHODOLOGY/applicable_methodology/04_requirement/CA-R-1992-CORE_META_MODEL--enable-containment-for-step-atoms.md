---
atom_id: CA-R-1992
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains"
  depends_on:
  - "Entity/Node/Continuant/Atom.Enabled Relations.Contains"
relations:
  child_of:
  - CA-R-1945
version: 3
updated_at: "2026-10-19 15:54:18 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1992-CORE_META_MODEL--enable-containment-for-step-atoms.md
  source_atom_id: CA-R-1992
  source_atom_revision: 3
  source_sha256: 96f8e88bc1a0c5bba9d45ee4b67bcb7d9760768d027078f808aa1d2a55d04bc6
  original_relations_sha256: 2fc855d77171d79c5f946e04ce0f770d15c7c80d8f7c81f058e114045a6a5f49
---
# Summary

Enable containment for Step Atoms

## Scope

Containment capability of Step Atoms, including nested substeps.

## Claim

`Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains` **must** be True. a Step Atom **may** contain other Step Atoms.

## Details

A substep is a nested Step, not a separate Type. Containment is optional and can nest. This permission does not change a Step's Action reference or input bindings, prescribe how internal tool calls are modeled, or introduce a storage layout or execution protocol.
