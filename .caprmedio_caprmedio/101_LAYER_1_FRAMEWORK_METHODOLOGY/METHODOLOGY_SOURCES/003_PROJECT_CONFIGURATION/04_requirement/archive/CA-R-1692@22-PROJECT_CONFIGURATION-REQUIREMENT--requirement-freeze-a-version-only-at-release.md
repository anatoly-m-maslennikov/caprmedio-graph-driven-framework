---
subjects:
  governs: Version/release
  depends_on:
  - Version
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Artifact/Revision
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
  - 'Atom/Content Role: Implementation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Extension
  - Project Configuration
version: 22
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-1712
  - CA-R-1646
  - CA-O-025
atom_id: CA-R-1692@22
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
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
