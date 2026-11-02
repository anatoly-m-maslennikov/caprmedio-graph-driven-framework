---
atom_id: CA-R-1619
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Source-declared Relation Derivation"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Entity/Relation"
    - "Relation Derivation Class"
version: 5
updated_at: "2026-10-19 15:56:09 +0400"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CA-R-1687
    - CA-R-1746
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1619-PROJECT_CONFIGURATION-REQUIREMENT--define-source-declared-relation-derivation.md
  source_atom_id: CA-R-1619
  source_atom_revision: 5
  source_sha256: b163fa3fed4778a308323bff79d15bef21cc78193a0bc68f7200bf769e6f64c2
  original_relations_sha256: 9498a3bf925a4c9ab02a1ce984d38e81a4cea3f350b87deeacc61ca5f1581a30
---
# Summary

Define Source-declared Relation Derivation

## Scope

source-declared derivation of represented Realization Graph Relations.

## Claim

Source-declared Relation Derivation **means** that a represented Realization Graph Relation is explicitly encoded **in** an identified selected native source, manifest, **or** configuration.

## Details

the result **must** identify the exact source occurrence **and** the interpretation used **to** read that declaration. declaring a Relation does **not** establish that it executes, resolves successfully, **or** satisfies a Requirement.
