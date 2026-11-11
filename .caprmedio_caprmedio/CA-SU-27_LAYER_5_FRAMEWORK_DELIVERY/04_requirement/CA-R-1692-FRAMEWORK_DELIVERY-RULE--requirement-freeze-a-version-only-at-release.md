---
atom_id: CA-R-1692
ref_id: CA-R-1692
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Traceability
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 3
relations:
  depends_on:
  - CA-R-1712
status: Active
version: 39
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1692-FRAMEWORK_DELIVERY-RULE--requirement-freeze-a-version-only-at-release.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
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
