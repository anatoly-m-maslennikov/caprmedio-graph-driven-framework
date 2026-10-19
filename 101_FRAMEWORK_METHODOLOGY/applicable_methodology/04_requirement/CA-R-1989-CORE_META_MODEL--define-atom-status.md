---
atom_id: CA-R-1989
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Atom.Status"
  depends_on:
  - "Entity/Continuant/Node/Atom"
  - "Entity/Continuant/Node/Atom/Content Role"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:06 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1989-CORE_META_MODEL--define-atom-status.md
  source_atom_id: CA-R-1989
  source_atom_revision: 2
  source_sha256: 6b065d0b2b1ac299e04ecdc0e03be8a8cdcf1c4cfa8f1af9762db67862ae7a39
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Atom Status

## Scope

Status borne by an Atom, including the recorded value preserved in an archived Atom.

## Claim

Atom.Status **means** the Atom's lifecycle classification under its applicable Status model. Status is a dependent property of the Atom; its allowed values resolve under the applicable Atom, Content Role and Type rules.

## Details

IS_BORNE_BY expresses the property-to-Atom relation. A current Atom is not a historical Revision merely because it has a Version Number. An archived Atom preserves its recorded Status; preserving history does not rewrite that value. CA-R-1412 supplies the one-Status requirement. The separate allowed-value rules define inherited and additional values; this definition adds no values, transition procedure or mandatory history record. Shared Status meanings are derived in the Terms graph from source usage, not independently authored here for every owner.
