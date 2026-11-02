---
subjects:
  governs: "Entity/Node/Continuant/Atom.Summary"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.ID", "Entity/Node/Continuant/Atom.Substance"]
version: 9
updated_at: "2026-10-19 15:53:10 +0400"
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
  source_atom_revision: 9
  source_sha256: 77910303210ede4eeba069ec58e676a4b4c108aea11bb6da20b5214a5213e909
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Summary fixed for Atom identity

## Scope

the Summary of an Atom across its Revisions.

## Claim

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.

## Details
