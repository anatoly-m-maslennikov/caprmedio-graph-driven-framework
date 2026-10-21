---
subjects:
  governs: "NARROWER_THAN"
  depends_on:
    ["Entity/Node/Continuant/Term", "Entity/Node/Continuant/Projection/Type: Terms Graph", "Entity/Relation", "Property", "Definition Atom"]
version: 11
updated_at: "2026-10-20 04:50:36 +0400"
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
  source_atom_revision: 11
  source_sha256: 9a76c307aa4ada69333cc2c31951e81f4480b971117072bf276794942afcbf49
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define NARROWER_THAN

## Scope

the NARROWER_THAN Relation **in** the Terms Graph.

## Claim

a NARROWER_THAN Relation from Term A **to** Term B **in** the Terms Graph **means** that, under their governing definitions, **if** Term A applies **to** a referent, **then** Term B applies **to** the same referent; this Relation does **not** express Property ownership **or** allowed-value membership.

## Semantics

Specialization and bearer dependence are distinct. A dependent kind can itself have narrower kinds. NARROWER_THAN does not establish that either endpoint is primary and does not substitute for IS_BORNE_BY.

## Details

### relation admission

- Status: the NARROWER_THAN Relation Kind is Active.
