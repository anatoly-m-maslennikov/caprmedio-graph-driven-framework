---
subjects:
  governs: "Artifact Classification Resolution"
  depends_on:
    ["Artifact", "Entity/Continuant/Object/Atom", "Atom/Content Role", "Type", "Entity/Continuant/Projection/Type: Applicable Methodology", "Project Configuration", "Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Projection/Type: Scope Unit Graph", "Entity/Continuant/History/Journal", "Entity/Continuant/Projection", "Authority Mode"]
version: 26
updated_at: "2026-10-15 18:45:18 +0000"
relations: {}
atom_id: "CA-R-1655"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1655-CORE_META_MODEL-GENERAL-REQUIREMENT--resolve-artifact-classification-from-authority-and-configuration.md
  source_atom_id: CA-R-1655
  source_atom_revision: 26
  source_sha256: 803f6c79ecb01ca2cd3262fc282906bfa637ca7ebd16bbd4e2d3fffa9320ca3b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
