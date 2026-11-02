---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Release.ID
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Release.ID
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Engineering/Traceability
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - Subject/Graph Node/Implementation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Product/Extension
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 32
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1712
atom_id: CA-R-1692@32
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Requirement — Freeze a version only at release

## Scope

target Versions and their selected authorized release events.

## Claim

a target Version **must** remain mutable **until** its selected authorized release event succeeds **and** the shared Journal records that outcome for the exact released candidate.

- the release record is a factual Journal Record under CA-R-1712, **not** an Operations Atom.
- its exact manifest binds the released governing Atom Revisions, Implementation **and** Delivery Revisions, applicable Evaluations **and** evidence, **and** release identifier.
- the selected release policy defines the event boundary. applicable Delivery authority defines the manifest **and** Journal representation; a selected Extension owns mechanism-specific references.
- planning allocation, implementation completion, readiness acceptance, **or** release-candidate naming does **not** freeze the Version **before** the successful event.

## Details

this Project Configuration Claim does **not** impose its release Workflow on **every** Project.
