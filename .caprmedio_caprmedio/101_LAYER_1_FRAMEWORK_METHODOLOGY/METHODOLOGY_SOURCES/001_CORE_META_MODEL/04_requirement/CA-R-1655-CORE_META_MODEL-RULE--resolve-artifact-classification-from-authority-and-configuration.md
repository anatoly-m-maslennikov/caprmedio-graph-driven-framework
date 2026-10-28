---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Scope Unit Graph'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
version: 39
updated_at: 2026-10-27 20:00:00 +0400
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
# Resolve Artifact Classification from Authority and Configuration

## Scope

Artifact classifications resolved from Applicable Methodology and Project Configuration with structural context from authoritative Project Structure.

## Claim

CAPRMEDIO **must** resolve **every** Artifact's applicable classification from Applicable Methodology **and** Project Configuration, with structural context from authoritative Project Structure:

- resolve Artifact Type under the applicable Type authority.
- resolve Content Role **only** for an Atom; do **not** require a Journal **or** Projection **to** have an Atom Content Role.
- resolve a semantic route **only** **where** the applicable authority defines that classification.
- classify an unknown, disabled, stale, multiply mapped, **or** ambiguous value as an unresolved **or** failed classification, **not** as an accepted one.

a derived Scope Unit Graph **must not** replace Project Structure as structural authority. reporting a classification failure does **not** itself impose a universal mutation **or** execution prohibition; the applicable Authority Mode **and** admission rules govern that consequence.

## Details
