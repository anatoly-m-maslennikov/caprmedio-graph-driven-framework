---
subjects:
  governs: settings specification
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Governing Configuration
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Scope Unit
version: 20
updated_at: 2026-10-24 12:41:34 +0400
relations: {}
atom_id: CA-R-1429@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Separate settings boundaries from field specifications

## Scope

the authority boundary between settings foundations, shared settings specifications, **and** concrete specifications.

## Claim

- the settings foundations for Project Settings, Framework Instance Settings, **and** Default Settings **must** define their purpose, content, **and** authority boundaries;
- an independently governable shared settings specification **must** preserve those foundations **without** selecting a concrete representation;
- **every** concrete section, field, **or** Carrier syntax specification **must** be specified explicitly.

a setting **must not** require a shared settings specification **unless** a distinct shared specification requires independent authority.

## Details
