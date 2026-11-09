---
atom_id: CA-D-529
ref_id: CA-D-529
container:
  scope_unit: CA-SU-16
role: Delivery
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure"
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure"
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
tier: 5
relations:
  delivery_for:
  - CA-D-527
  - CA-D-528
status: Active
version: 13
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-529-TOOLS-ENG_DECISION--place-shared-selected-run-support-at-the-existing-tools-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Place shared selected Run support at the existing TOOLS boundary

## Scope

Implementation placement for the shared service and its existing Journal
dependency. No new Scope Unit, executable Tool, workflow, or Journal is
declared by this Delivery.

## Claim

Shared selected-Run support **must** be delivered as the non-executable library
`LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/workflow_run_support.py`,
beside the existing non-executable `work_journal.py`, and callers must use that
one library rather than adapter-local Run/Journaling implementations.

## Details

- The library owns only request validation, currentness admission, Run
  provenance shaping, pending-recording recovery, and use of `work_journal`.
  Selected route executors, MCP adapters, and prompt/runtime components retain
  their existing ownership and inject their effects/results through the shared
  contract.
- Its only durable historical authority is the Project Work Journal configured
  by Project settings. Its runtime pending/receipt state is under the existing
  `.caprmedio_runtime/state/work_journal/` boundary and must not be projected
  as a competing Journal.
- No caller receives an implicit worker start, background run, new source
  campaign, or authority to mutate from importing the library. A later
  separately approved delivery may add route implementations only after this
  RMED packet has independent review.
