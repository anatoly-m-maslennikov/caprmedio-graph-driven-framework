---
subjects:
  governs: "Entity/Continuant/Object/Atom.Summary"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.ID", "Entity/Continuant/Object/Atom.Substance"]
version: 7
updated_at: "2026-10-15 18:43:22 +0000"
relations: {}
atom_id: "CA-R-1464"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1464-CORE_META_MODEL--keep-summary-fixed-for-atom-identity.md
  source_atom_id: CA-R-1464
  source_atom_revision: 7
  source_sha256: 886ccf08de89e1bf0a27579815c41725ca494cf042c16d5904a65405569b4558
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Summary fixed for Atom identity

## Scope

the Summary of an Atom across its Revisions.

## Claim

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.

## Details
