---
subjects:
  governs: Subject/Graph Node/Engineering/Technical Configuration Boundary
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Governing Configuration
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Node/Domain/Continuant/Scope Unit
version: 22
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1429@22
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
