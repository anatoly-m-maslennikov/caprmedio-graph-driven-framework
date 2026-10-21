---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    - "Entity"
    - "Method"
atom_id: "CA-R-2006"
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
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-2006-CORE_META_MODEL-CORE--define-subject-target-roots.md
  source_atom_id: CA-R-2006
  source_atom_revision: 1
  source_sha256: 0c06df19ebbf65b521eb1b2f18a2270061ef740857b8e88eb8e3bf58e827ed84
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Subject Target Roots

## Scope

the first named component of a canonical Subject Target path.

## Claim

a canonical Subject Target path **must** begin with exactly one registered root:
`Entity` for what a Claim governs or `Method` for how a Method Claim guides work.

## Details

the roots are namespaces, not a hierarchy between Entity and Method. a Scope
Unit path, carrier path, owner path, or implementation-language folder does not
qualify a Subject Target unless it is explicitly part of the canonical target.
