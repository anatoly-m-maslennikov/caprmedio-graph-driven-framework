---
subjects:
  governs: "NARROWER_THAN"
  depends_on:
    ["Entity/Continuant/Term", "Entity/Continuant/Projection/Type: Terms Graph", "Entity/Continuant/Object/Relation", "Property", "Definition Atom"]
version: 9
updated_at: "2026-10-15 18:42:59 +0000"
relations: {}
atom_id: "CA-R-1435"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1435-CORE_META_MODEL-CORE--define-narrower-than.md
  source_atom_id: CA-R-1435
  source_atom_revision: 9
  source_sha256: 10e544470b2109c976e2856f7b47d6ac8d61799050cbf3d364fd4bb2d8d98e09
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define NARROWER_THAN

## Scope

the NARROWER_THAN Relation **in** the Terms Graph.

## Claim

a NARROWER_THAN Relation from Term A **to** Term B **in** the Terms Graph **means** that, under their governing definitions, **if** Term A applies **to** a referent, **then** Term B applies **to** the same referent; this Relation does **not** express Property ownership **or** allowed-value membership.

## Details

### relation admission

- Status: the NARROWER_THAN Relation Kind is Active.
