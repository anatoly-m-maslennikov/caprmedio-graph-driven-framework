---
atom_id: CA-M-319
ref_id: CA-M-319
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
tier: 3
status: Active
version: 8
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-319-TOOLS-ENG_DECISION--observe-and-continue-saved-execution-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method
current_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Observe and continue saved execution evidence

## Scope

the TOOLS capability for Execution observation.

## Claim

**to** observe **or** continue a supported Run, the Implementation **must** derive its response from the existing saved evidence.

## Details

1. validate the Run identifier **and** resolve **`=1`** registered backend.
2. read saved status, complete Action reports, source bindings **and** evidence-recording state. preserve initial check outcomes when later fixes are present.
3. derive remaining check **or** fix work from saved coverage **and** dispositions. check current source **and** criteria fingerprints before proposing continuation.
4. bind a notification cursor **to** the Run **and** saved evidence frontier; return later confirmed Events **and** changes **to** status **or** recording state.
5. wait asynchronously **until** evidence changes **or** the bounded timeout expires. an observation timeout does **not** fail the Run.
