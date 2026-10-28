---
atom_id: CA-O-168@16
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Delivery
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Verification
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 16
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
---
# Summary

Verify candidate release package and image

## Action

Verify candidate release package and image **means** the Action that performs one bound `closed_unit_gate`, `candidate_image_build`, or `candidate_image_canary` phase for the frozen local boundary.

## Scope

The `closed_unit_gate` phase binds the Version, active source identities and digests, Project Structure, settings, exact private compiled candidate, and declared Unit/source partition. It is not host Candidate E2E or the complete Release Gate. `candidate_image_build` and `candidate_image_canary` bind the exact staged package, runtime, compiled product, and `ca` payload after that Unit gate. Host-capable Candidate E2E is CA-O-182; CA-O-184 alone aggregates the complete Release Gate. These phases do not create another release Workflow.

## Details

A partial, cached, focused, stale, source-only, or unjournaled result is not proof. This Action never clears, copies, installs, publishes, or retries. Each actual Action Run is journaled once with its exact inputs and result.
