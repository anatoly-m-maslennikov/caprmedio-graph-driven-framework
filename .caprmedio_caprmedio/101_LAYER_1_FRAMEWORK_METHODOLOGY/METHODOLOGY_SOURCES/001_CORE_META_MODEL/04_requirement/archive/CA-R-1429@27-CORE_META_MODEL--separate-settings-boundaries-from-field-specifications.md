---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Governing Configuration
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - Entity/Object/Continuant/Structural Unit/Scope Unit
version: 27
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1429@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Separate settings boundaries from field specifications

## Claim scope

the authority boundary between settings foundations, shared settings specifications, **and** concrete specifications.

## Claim

- the settings foundations for Project Settings, Framework Instance Settings, **and** Default Settings **must** define their purpose, content, **and** authority boundaries;
- an independently governable shared settings specification **must** preserve those foundations **without** selecting a concrete representation;
- **every** concrete section, field, **or** Carrier syntax specification **must** be specified explicitly.

a setting **must not** require a shared settings specification **unless** a distinct shared specification requires independent authority.
