---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
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
