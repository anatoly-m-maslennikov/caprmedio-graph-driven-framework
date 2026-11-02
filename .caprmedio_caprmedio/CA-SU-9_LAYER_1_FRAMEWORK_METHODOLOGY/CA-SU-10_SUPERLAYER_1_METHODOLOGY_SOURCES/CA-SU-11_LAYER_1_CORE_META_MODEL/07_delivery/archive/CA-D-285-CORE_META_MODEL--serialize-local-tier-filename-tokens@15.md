---
subjects:
  governs: "Atom Carrier.Filename.Local Tier"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.Local Tier", "Entity/Continuant/Object/Atom.Local Tier: Standard", "Change Content Roles", "Implementation", "Artifact Carrier"]
version: 15
updated_at: "2026-10-15 18:50:51 +0000"
relations: {"delivery_for": ["CA-R-1566"]}
atom_id: "CA-D-285"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize Local Tier Filename Tokens

## Scope

Ordinary Atom filenames subject **to** the role-tier restrictions under CA-R-1566.

## Claim

an ordinary Atom filename **must** serialize Principle as `PRINCIPLE`, Core as `CORE`, General as `GENERAL`, **and** the default Standard Local Tier by omitting the Local Tier segment at the registered descriptor position **after** its identity **and** current Scope owner. `PRINCIPLE` is admitted **only** for a Project-scoped Atom; `STD`, `STANDARD`, `DETAIL`, **and** combined tier segments **must not** be serialized. the external Project Goal's registered tierless grammar **must** be recognized **before** applying the ordinary omitted-Standard default; a tier token **must not** replace **or** alter the registered identity, owner, target, **or** sequence grammar of a Goal **or** Plan.

## Details
