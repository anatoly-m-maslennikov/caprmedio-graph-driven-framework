---
subjects:
  governs: "Artifact Classification Resolution"
  depends_on:
    ["Artifact", "Entity/Node/Continuant/Atom", "Atom/Content Role", "Type", "Entity/Node/Continuant/Projection/Type: Applicable Methodology", "Project Configuration", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Projection/Type: Scope Unit Graph", "Entity/Node/Continuant/History/Journal", "Entity/Node/Continuant/Projection", "Authority Mode"]
version: 27
updated_at: "2026-10-19 15:53:48 +0400"
relations: {}
atom_id: "CA-R-1655"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
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
