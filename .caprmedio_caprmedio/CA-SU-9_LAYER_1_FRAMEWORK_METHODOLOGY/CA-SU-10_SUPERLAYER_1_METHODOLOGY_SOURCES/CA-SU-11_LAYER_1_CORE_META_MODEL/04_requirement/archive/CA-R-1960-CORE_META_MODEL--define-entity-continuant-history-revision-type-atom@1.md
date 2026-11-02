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
  governs: 'Entity/Continuant/History/Revision/Type: Atom'
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:27:54 +0400"
---
# Summary

Define Entity/Continuant/History/Revision/Type: Atom

## Scope

preserved earlier states of Atoms.

## Claim

an Atom Revision **means** a preserved earlier state of an Atom, represented by the archived Atom itself. it is **not** a dependent property of the current Atom or another current Atom.

## Details

Candidate #5 explicitly retains Revision/Type: Atom with preserved historical Atom properties; Candidate #6 keeps History/Revision separate from Atom. CA-R-1371 defines recorded state but also permits metadata changes without a new semantic Revision; that clause needs separate alignment with the accepted every-update Version rule. This draft neither changes CA-R-1371 nor prescribes a new history mechanism.
