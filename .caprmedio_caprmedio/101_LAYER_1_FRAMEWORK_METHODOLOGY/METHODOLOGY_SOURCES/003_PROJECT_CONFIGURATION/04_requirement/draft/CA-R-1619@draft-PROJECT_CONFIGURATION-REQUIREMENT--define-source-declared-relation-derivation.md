---
atom_id: "CA-R-1619@draft"
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: "Draft"
subjects:
  governs: "Source-declared Relation Derivation"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Entity/Relation"
    - "Relation Derivation Class"
version: 5
updated_at: "2026-10-19 11:47:53 +0000"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1617
    - CA-R-1687
    - CA-R-1746
global_tier: 11
---
# Summary

Define Source-declared Relation Derivation

## Scope

source-declared derivation of represented Realization Graph Relations.

## Claim

Source-declared Relation Derivation **means** that a represented Realization Graph Relation is explicitly encoded **in** an identified selected native source, manifest, **or** configuration.

## Details

the result **must** identify the exact source occurrence **and** the interpretation used **to** read that declaration. declaring a Relation does **not** establish that it executes, resolves successfully, **or** satisfies a Requirement.
