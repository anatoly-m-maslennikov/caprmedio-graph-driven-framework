---
subjects:
  governs: Entity
  depends_on:
  - Entity/Object/Continuant/Term//Artifact
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Projection/Type
  - 'Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - 'Entity/Object/Continuant/Projection/Type: Scope Unit Graph'
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
version: 42
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1655
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary
Resolve Artifact Classification from Authority and Configuration

## Claim scope

Artifact classifications resolved from Applicable Methodology and Project Configuration with structural context from authoritative Project Structure.

## Claim

CAPRMEDIO **must** resolve **every** Artifact's applicable classification from Applicable Methodology **and** Project Configuration, with structural context from authoritative Project Structure:

- resolve Artifact Type under the applicable Type authority.
- resolve Content Role **only** for an Atom; do **not** require a Journal **or** Projection **to** have an Atom Content Role.
- resolve a semantic route **only** **where** the applicable authority defines that classification.
- classify an unknown, disabled, stale, multiply mapped, **or** ambiguous value as an unresolved **or** failed classification, **not** as an accepted one.

a derived Scope Unit Graph **must not** replace Project Structure as structural authority. reporting a classification failure does **not** itself impose a universal mutation **or** execution prohibition; the applicable Authority Mode **and** admission rules govern that consequence.
