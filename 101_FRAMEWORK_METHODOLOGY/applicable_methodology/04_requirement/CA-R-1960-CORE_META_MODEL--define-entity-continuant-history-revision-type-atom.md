---
atom_id: CA-R-1960
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/History/Revision/Type: Atom"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:02 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1960-CORE_META_MODEL--define-entity-continuant-history-revision-type-atom.md
  source_atom_id: CA-R-1960
  source_atom_revision: 2
  source_sha256: 23bff5ca3d9c989546a4ff5681fff914e54d8f799c4094fb607f52055ac14fa0
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Entity/Continuant/History/Revision/Type: Atom

## Scope

preserved earlier states of Atoms.

## Claim

an Atom Revision **means** a preserved earlier state of an Atom, represented by the archived Atom itself. it is **not** a dependent property of the current Atom or another current Atom.

## Details

Candidate #5 explicitly retains Revision/Type: Atom with preserved historical Atom properties; Candidate #6 keeps History/Revision separate from Atom. CA-R-1371 defines recorded state but also permits metadata changes without a new semantic Revision; that clause needs separate alignment with the accepted every-update Version rule. This draft neither changes CA-R-1371 nor prescribes a new history mechanism.
