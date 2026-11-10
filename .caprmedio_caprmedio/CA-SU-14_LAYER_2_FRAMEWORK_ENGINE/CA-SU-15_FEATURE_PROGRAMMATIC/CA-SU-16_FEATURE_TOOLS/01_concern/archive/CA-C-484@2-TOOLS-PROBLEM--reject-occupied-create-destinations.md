---
atom_id: CA-C-484
ref_id: CA-C-484@2
container:
  scope_unit: CA-SU-16
role: Concern
form: Problem
topics:
  main_subject: Subject/Domain/Node/Continuant/Atom
  dependencies:
  - Subject/Engineering/Atom Creation/Destination Conflicts
  - Subject/Engineering/Filesystem Mutation/Collision Refusal
relations:
  concern_about:
  - CA-P-1758
status: Archived
version: 2
updated_at: 2026-10-23 01:47:30 +0400
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-484@2-TOOLS-PROBLEM--reject-occupied-create-destinations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern/archive
---
# Summary

Reject occupied Create destinations

## Concern

W01 treats any occupied destination as duplicate without proving equivalent intent or bytes; the selected executor turns that into a successful no-op.

## Evidences

At commit `c011b68fa`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/lifecycle_intents.py:749-751` returns pathname-only duplicate; `203_APPS/WORKFLOW_ORCHESTRATOR/selected_execution.py:293-295` terminalizes it as no_op. CA-O-128 requires destination absence/unused identity. Regression: `201_TOOLS/tests/test_lifecycle_create_conflicts.py`.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Reject destination collision before effects under O128; retain the existing carrier and test the conflict.

CA-P-1758 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
