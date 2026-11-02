---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    - "Entity"
    - "Method"
atom_id: "CA-R-2004"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
version: 1
updated_at: "2026-10-21 01:47:52 +0400"
author: "Anatoly Maslennikov"
global_tier: 9
relations: {}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-2004-CORE_META_MODEL-CORE--define-subject-target.md
  source_atom_id: CA-R-2004
  source_atom_revision: 1
  source_sha256: 79424806df8799b8317d685a890b94027bf373ec04462574ce6de820a22601df
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Subject Target

## Scope

a direct Subject Relation target.

## Claim

a Subject Target **means** exactly one canonical target addressed by a Subject
Expression. a Subject Target **must** be either an Entity or a Method Topic.

## Details

a Subject Target is the endpoint of GOVERNS or DEPENDS_ON. the reference does
not assign the target as the referencing Atom's owning Scope Unit or Carrier.
resolving a Subject Target does not create an Entity, Method Topic, or relation fact.
