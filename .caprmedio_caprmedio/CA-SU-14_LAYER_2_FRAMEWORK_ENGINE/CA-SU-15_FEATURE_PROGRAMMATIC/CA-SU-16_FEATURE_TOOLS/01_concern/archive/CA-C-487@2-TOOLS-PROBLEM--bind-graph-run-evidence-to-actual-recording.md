---
atom_id: CA-C-487
ref_id: CA-C-487@2
container:
  scope_unit: CA-SU-16
role: Concern
form: Problem
topics:
  main_subject: Subject/Domain/Node/Occurrent/Execution
  dependencies:
  - Subject/Engineering/Projection Generation/Execution Recording
  - Subject/Engineering/Execution Recording/Observed Effects
relations:
  concern_about:
  - CA-P-1760
status: Archived
version: 2
updated_at: 2026-10-23 01:47:30 +0400
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-487@2-TOOLS-PROBLEM--bind-graph-run-evidence-to-actual-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern/archive
---
# Summary

Bind graph Run evidence to actual recording

## Concern

Graph construction accepts caller-provided confirmed receipt strings; selected execution must not use them as proof of actual same-invocation recording.

## Evidences

At commit `c011b68fa`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py:1464,1651` accepts caller receipt strings, and the selected executor records Action execution later. CA-O-133 and CA-R-1728 require actual Run recording.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Use genuine Action start recording before effects and terminal recording afterward; preserve unrecorded facts as pending without effect replay.

CA-P-1760 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
