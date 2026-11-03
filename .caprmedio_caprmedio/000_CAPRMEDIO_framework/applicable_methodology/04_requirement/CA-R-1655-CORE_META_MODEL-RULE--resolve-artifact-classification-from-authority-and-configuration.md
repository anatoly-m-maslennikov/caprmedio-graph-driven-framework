---
subjects:
  active: Entity
  passive:
  - Term//Artifact
  - Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content Role
  - Entity/Object/Continuant/Projection.Type
  - 'Entity/Object/Continuant/Projection/(.Type: Applicable Methodology)'
  - Scope Unit//PROJECT_CONFIGURATION
  - Scope Unit
  - 'Entity/Object/Continuant/Projection/(.Type: Scope Unit Graph)'
  - Journal
  - Projection
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority
    Modes
version: 45
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-1655
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1655-CORE_META_MODEL-RULE--resolve-artifact-classification-from-authority-and-configuration.md
  source_atom_id: CA-R-1655
  source_atom_revision: 45
  source_sha256: 5b8c76c19276e5061ca331a3f082e9a3bfc74119831178a7c01c1d6a4d76504c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
