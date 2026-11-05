---
atom_id: CA-C-538
ref_id: CA-C-538
container:
  scope_unit: CA-SU-15
role: Concern
form: Problem
topics:
  main_subject: Subject/Domain/Node/Continuant/Atom
relations:
  concern_about: [CA-D-290, CA-P-2401]
status: Active
version: 2
updated_at: 2026-10-23 03:06:32 +0400
carrier_destination:
  file:
    name: CA-C-538-PROGRAMMATIC-PROBLEM--reject-version-suffixes-on-current-carrier-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
priority: medium
---
# Summary

Reject Version suffixes on Current carrier inputs

## Concern

Current D290v14 forbids archived-style Version suffixes across Current statuses. Generated lifecycle addresses comply, but complete-carrier input validation does not explicitly reject an @N suffix on a non-Archived carrier.

## Evidences

Read-only identity-contract review found atom_operations._validate_revision_filename requires the suffix for Archived carriers, while the general CURRENT_FILENAME grammar can still admit an @N suffix for non-Archived inputs. No production invalid carrier, mutation or data loss was observed. This is an input-validation coverage gap, separate from the stale // parser and C533 edit-draft markers.

## Blast radius

Filename/property synchronization requires a bounded input-boundary fix and frozen positive/negative status matrix. Keep valid generated addresses unchanged and retain immutable archive names; do not rewrite existing carriers or claim this deferred gap was repaired by the parser release.
