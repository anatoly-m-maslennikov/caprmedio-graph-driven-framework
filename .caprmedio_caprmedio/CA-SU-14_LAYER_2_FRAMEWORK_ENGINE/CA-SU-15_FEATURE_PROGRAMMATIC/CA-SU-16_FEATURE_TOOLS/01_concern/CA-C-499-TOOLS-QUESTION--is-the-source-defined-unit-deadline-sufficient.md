---
atom_id: CA-C-499
ref_id: CA-C-499
container:
  scope_unit: CA-SU-16
role: Concern
form: Question
topics:
  main_subject: Release Unit deadline sufficiency
  dependencies:
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Test Suite
  - Subject/Engineering/Carrier/File Carrier
  - Evaluation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
relations:
  concern_about: [CA-P-1792, CA-P-1782, CA-D-579, CA-D-580]
status: Active
version: 2
updated_at: 2026-10-23 03:14:50 +0400
carrier_destination:
  file:
    name: CA-C-499-TOOLS-QUESTION--is-the-source-defined-unit-deadline-sufficient.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
---
# Summary

Is the source-defined Unit deadline sufficient

## Concern

does a source-sealed default of 3600 seconds, bounded by 7200 seconds and configurable through the Framework Instance, permit the complete Unit partition to finish without omitting tests or weakening timeout and currentness gates?

## Evidences

- N10 actual receipt outcome is timed_out after 934.4613934169975 seconds under the existing code-only 900-second ceiling. there is no complete JUnit/coverage report; its zero validated count does not mean zero execution.
- the full local image fixture module alone passed 53 tests in 862.154 seconds.
- actual N10 interruption receipts exist for Action, Step and Workflow. no candidate image, promotion or retirement occurred; installed N remains unchanged.

## Blast radius

only the source-owned Unit deadline, its exact existing settings carriers, private reference closure, resolver and bounded executor. preserve all Unit modules, the three separate Candidate E2E harnesses, public schemas and historical events.

## Details

choose the provisional finite default under the Operator's autonomous best-option authorization, implement it source-first with independent review, and require actual complete fresh-gate evidence. do not claim sufficiency from the number alone or replay failed N10.
