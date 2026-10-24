---
atom_id: CA-C-531
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: medium
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2434]
version: 2
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Align completed Epic Task status placement

## Concern

Ten manually completed Task carriers declared Done but remained directly inside the Active Epic's matching directory. D461v13 requires Done files in the local container's done subdirectory. The address-only mismatch has been repaired.

## Evidences

CA-P-2434 enumerated the exact ten files and refused unexpected bundles/collisions. All ten were moved into the Epic's local done directory with identical bytes, identity and Version; old source paths are absent and every SHA256 matched. Existing historical archive carriers remained in place. Canonical move_atom_revision likewise preserves the current Version during a pure address relocation. Actual exact old/new path and hash evidence is recorded in the append-only source-work Journal checkpoint.

## Blast radius

The current completed Task addresses now agree with carried Status. Subsequent completed Task updates must use the same local mapping. This bounded repair makes no native full-carrier, workflow/runtime or deployment claim.
