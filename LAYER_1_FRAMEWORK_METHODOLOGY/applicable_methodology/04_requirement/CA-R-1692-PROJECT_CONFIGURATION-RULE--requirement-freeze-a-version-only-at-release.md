---
subjects:
  active: Entity/Object/Continuant/History/Release.ID
  passive:
  - Entity/Object/Continuant/History/Release.ID
  - Entity/Object/Continuant/History/Journal > Event Record
  - Aspects <+ Engineering <+ Traceability
  - Atom/(.Role := Operations)
  - Entity/Object/Continuant/Package/Project Implementation
  - Atom/(.Role := Delivery)
  - Atom/(.Role := Evaluation)
  - Scope Unit
  - Scope Unit//PROJECT_CONFIGURATION
version: 38
updated_at: 2026-11-02 18:35:20 +0400
relations:
  depends_on:
  - CA-R-1712
atom_id: CA-R-1692
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1692-PROJECT_CONFIGURATION-RULE--requirement-freeze-a-version-only-at-release.md
  source_atom_id: CA-R-1692
  source_atom_revision: 38
  source_sha256: e6a1b217566a382a94b6f01694911e0e641f768e42b4fe03fb34959cfa53e406
  original_relations_sha256: 9524423f93502e18e8ae3356212fbe4edc2c2d857c1cf4b20d69da517033d424
---
## Summary

Requirement — Freeze a version only at release

## Claim scope

target Versions and their selected authorized release events.

## Claim

a target Version **must** remain mutable **until** its selected authorized release event succeeds **and** the shared Journal records that outcome for the exact released candidate.

- the release record is a factual Journal Record under CA-R-1712, **not** an Operations Atom.
- its exact manifest binds the released governing Atom Revisions, Implementation **and** Delivery Revisions, applicable Evaluations **and** evidence, **and** release identifier.
- the selected release policy defines the event boundary. applicable Delivery authority defines the manifest **and** Journal representation; a selected Extension owns mechanism-specific references.
- planning allocation, implementation completion, readiness acceptance, **or** release-candidate naming does **not** freeze the Version **before** the successful event.

## Details

this Project Configuration Claim does **not** impose its release Workflow on **every** Project.
