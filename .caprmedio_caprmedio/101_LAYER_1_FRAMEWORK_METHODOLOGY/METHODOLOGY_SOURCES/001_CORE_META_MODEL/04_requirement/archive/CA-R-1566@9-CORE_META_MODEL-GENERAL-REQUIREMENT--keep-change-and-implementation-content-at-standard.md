---
subjects:
  governs: Entity/Node/Continuant/Atom.Local Tier
  depends_on:
  - Change Content Roles
  - Implementation
  - Subject/Domain/Node/Continuant/Atom
  - 'Entity/Node/Continuant/Atom.Local Tier: Standard'
version: 9
updated_at: 2026-10-23 03:06:32 +0400
relations: {"relates_to": ["CA-R-1549", "CA-R-1343", "CA-R-660"]}
atom_id: "CA-R-1566@9"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Keep Change **and** Implementation content at Standard

## Scope

Atoms whose Content Role is Concern, Analysis, Plan, Operations, **or** Implementation.

## Claim

an Atom whose Content Role is **in** (Concern, Analysis, Plan, Operations, Implementation) **must** resolve **to** Local Tier Standard.

- an omitted filename tier token denotes Standard, **not** the absence of the internally carried Local Tier; persistence, reuse, importance, **or** nesting **does** not promote that content **to** Core **or** General.
- the RMED Atoms specifying that content retain their own Local Tiers; the content **does** not inherit its specification's tier.

## Details
