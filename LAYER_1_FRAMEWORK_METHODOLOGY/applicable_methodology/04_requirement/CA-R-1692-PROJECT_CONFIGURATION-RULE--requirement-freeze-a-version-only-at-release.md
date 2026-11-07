---
atom_id: CA-R-1692
ref_id: CA-R-1692
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 3
relations:
  depends_on:
  - CA-R-1712
status: Active
version: 38
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1692-PROJECT_CONFIGURATION-RULE--requirement-freeze-a-version-only-at-release.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1692-PROJECT_CONFIGURATION-RULE--requirement-freeze-a-version-only-at-release.md
  source_atom_id: CA-R-1692
  source_atom_revision: 38
  source_sha256: 3e3cb63472b682e357bd86073da860cd40ceafdc778b54ca7c04edc367d28c5b
  original_relations_sha256: 9524423f93502e18e8ae3356212fbe4edc2c2d857c1cf4b20d69da517033d424
---
## Summary

Requirement — Freeze a version only at release

## Claim

### Prose Claim


target Versions and their selected authorized release events.


a target Version **must** remain mutable **until** its selected authorized release event succeeds **and** the shared Journal records that outcome for the exact released candidate.

- the release record is a factual Journal Record under CA-R-1712, **not** an Operations Atom.
- its exact manifest binds the released governing Atom Revisions, Implementation **and** Delivery Revisions, applicable Evaluations **and** evidence, **and** release identifier.
- the selected release policy defines the event boundary. applicable Delivery authority defines the manifest **and** Journal representation; a selected Extension owns mechanism-specific references.
- planning allocation, implementation completion, readiness acceptance, **or** release-candidate naming does **not** freeze the Version **before** the successful event.

## Details

this Project Configuration Claim does **not** impose its release Workflow on **every** Project.
