---
atom_id: CA-R-1989@7
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Status
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom/Content Role
relations:
  child_of:
  - CA-R-1174
version: 7
updated_at: 2026-10-24 01:37:42 +0400
tier: 1
type: Definition
---
# Summary

Define Atom Status

## Scope

Status borne by an Atom, including the recorded value preserved in an archived Atom.

## Claim

Atom.Status **means** the Atom's lifecycle classification under its applicable Status model. Status is a dependent property of the Atom; its allowed values resolve under the applicable Atom, Content Role and Type rules.

## Details

IS_BORNE_BY expresses the property-to-Atom relation. A Current Atom is not historical merely because it has a Version Number. An archived Atom preserves its recorded Status; preserving history does not rewrite that value. CA-R-1412 supplies the one-Status requirement. The separate allowed-value rules define inherited and additional values; this definition adds no values, transition procedure or mandatory history record. Shared Status meanings are derived in the Terms graph from source usage, not independently authored here for every owner.
