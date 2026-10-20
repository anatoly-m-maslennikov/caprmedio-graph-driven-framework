---
subjects:
  governs: "Relation Kind Metadata"
  depends_on:
    ["Relation Kind", "CAPRMEDIO Graph", "Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom"]
version: 25
updated_at: "2026-10-20 00:10:03 +0400"
relations: {}
atom_id: "CA-R-806"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-806-CORE_META_MODEL-GENERAL--register-complete-relation-kind-metadata.md
  source_atom_id: CA-R-806
  source_atom_revision: 25
  source_sha256: 1e1949d39f621e7690aea2add875bee3726e7ae3a80a416e8cc7cddf57d09776
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register Complete Relation Kind Metadata

## Scope

admitted Relation Kinds.

## Claim

**every** admitted Relation Kind **must** have **`=1`** canonical descriptive metadata record derived from its governing authority that resolves its owning kind of CAPRMEDIO Graph, canonical name, meaning, declared direct direction, inverse direction, authority effect, transitivity, applicability, Status, **and** exclusive purpose.

## Details

Allowed source and target classes, allowed endpoint graph contexts, cardinality and other permissions or prohibitions belong in the governing Graph Rules, not in the Relation Kind definition. Descriptive meaning, transitivity and applicability explain the relation; any admissibility restriction belongs in its Graph Rules instead. A view may combine the definition with its governing Graph Rules without creating a second authoritative constraint. The declared direct direction identifies the one authored fact; its inverse is derived. A name such as IS_CONTAINED_BY does not make that direction an inverse. Moving existing constraints into formal Rule instances remains separate source work; this metadata contract does not itself rewrite them.
