---
atom_id: CA-M-319@7
content_role: Method
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
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
