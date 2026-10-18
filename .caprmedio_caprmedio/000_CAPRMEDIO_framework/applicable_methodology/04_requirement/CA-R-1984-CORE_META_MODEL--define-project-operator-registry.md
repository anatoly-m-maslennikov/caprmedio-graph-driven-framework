---
atom_id: CA-R-1984
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Project.Operator Registry"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:05 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1984-CORE_META_MODEL--define-project-operator-registry.md
  source_atom_id: CA-R-1984
  source_atom_revision: 2
  source_sha256: 7a62539cb7a74e63090b221ef23abdd5700c91a7f13341a627dc288555d60b9a
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Project.Operator Registry

## Scope

the authoritative Operator registry of a Project.

## Claim

Operator Registry **means** the Project's authoritative registry of its Operators **and** their declared identifying information. Registry membership does **not** itself grant execution permission.

## Details

Evidence: CA-D-494 defines registered Operator names and roles, exact membership and the no-permission distinction. Candidate #6 keeps Actor distinct from Project and permits abstract, project-independent Core definitions. File format, filename, location and concrete Operator identities remain separate Delivery/configuration concerns; this definition adds none.
