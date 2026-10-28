---
atom_id: CA-M-319
content_role: Method
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
relations: {}
type: Eng Decision
tier: 3
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
