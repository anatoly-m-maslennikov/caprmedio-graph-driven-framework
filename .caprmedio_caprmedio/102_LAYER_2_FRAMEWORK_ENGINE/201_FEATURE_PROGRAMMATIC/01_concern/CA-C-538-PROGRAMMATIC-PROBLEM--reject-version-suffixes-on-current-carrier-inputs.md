---
atom_id: CA-C-538
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-D-290, CA-P-2401]
version: 1
updated_at: "2026-10-20 17:23:00 +0400"
---
# Summary

Reject Version suffixes on Current carrier inputs

## Concern

Current D290v14 forbids archived-style Version suffixes across Current statuses. Generated lifecycle addresses comply, but complete-carrier input validation does not explicitly reject an @N suffix on a non-Archived carrier.

## Evidences

Read-only identity-contract review found atom_operations._validate_revision_filename requires the suffix for Archived carriers, while the general CURRENT_FILENAME grammar can still admit an @N suffix for non-Archived inputs. No production invalid carrier, mutation or data loss was observed. This is an input-validation coverage gap, separate from the stale // parser and C533 edit-draft markers.

## Blast radius

Filename/property synchronization requires a bounded input-boundary fix and frozen positive/negative status matrix. Keep valid generated addresses unchanged and retain immutable archive names; do not rewrite existing carriers or claim this deferred gap was repaired by the parser release.
