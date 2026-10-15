---
subjects:
  governs: "settings specification"
  depends_on:
    ["Entity/Continuant/Object/Project.Settings", "Entity/Continuant/Object/Project.Framework Settings", "Default Settings", "Entity/Continuant/Object/Atom.Local Tier", "Entity/Continuant/Object/Scope Unit"]
version: 12
updated_at: "2026-10-15 18:14:57 +0000"
relations: {}
atom_id: "CA-R-1429@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate settings boundaries from field specifications

## Scope

the authority boundary between settings foundations, shared settings specifications, **and** concrete specifications.

## Claim

- the Core-tier Atoms for Project Settings, Framework Instance Settings, **and** Default Settings **must** define their purpose, content, **and** authority boundaries;
- an independently governable shared settings specification **must** belong **to** General **when** General is admitted **in** its current Scope Unit **and** it preserves those foundations **without** selecting a concrete representation;
- **every** concrete section, field, **or** Carrier syntax specification **must** belong **to** Standard.

a setting **must not** require a General Atom **unless** a distinct shared specification requires independent authority.

## Details
