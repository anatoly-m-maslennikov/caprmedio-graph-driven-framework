---
subjects:
  governs: "Atom Scope"
  depends_on:
    ["Entity/Continuant/Object/Atom.Author", "Scope Unit Scope", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Atom.Governed Subject", "Entity/Continuant/Object/Atom.Substance"]
version: 20
updated_at: "2026-10-15 18:41:02 +0000"
relations:
  child_of:
    - CA-R-1596
atom_id: "CA-R-1014"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1014-CORE_META_MODEL-CORE-REQUIREMENT--resolve-atom-scope-contextually.md
  source_atom_id: CA-R-1014
  source_atom_revision: 20
  source_sha256: 4d9c312dfd4f4a45a5e6025960e8d4aedb4874454fef998dfc2ea09d6984a825
  original_relations_sha256: bb6e7449127f6a7b5fd2adfab279201f33fd1e44c746e3974b29f5c557c9b581
---
# Summary

Resolve Atom Scope Contextually

## Scope

Atom Scope.

## Claim

an Atom Scope **must** include its current Scope Unit Scope **or** its Author's registered Operator fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.

## Details
