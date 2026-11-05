---
atom_id: CA-O-168
ref_id: CA-O-168
role: Operations
form: Action
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 17
updated_at: 2026-10-27 19:59:47 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-O-168-CAPRMEDIO-ACTION--verify-candidate-release-package-and-image.md
    path: .caprmedio_caprmedio/09_operations
---
# Summary

Verify candidate release package and image

## Action

Verify candidate release package and image **means** the Action that performs one bound `closed_unit_gate`, `candidate_image_build`, or `candidate_image_canary` phase for the frozen local boundary.

## Scope

The `closed_unit_gate` phase binds the Version, active source identities and digests, Project Structure, settings, exact private compiled candidate, and declared Unit/source partition. It is not host Candidate E2E or the complete Release Gate. `candidate_image_build` and `candidate_image_canary` bind the exact staged package, runtime, compiled product, and `ca` payload after that Unit gate. Host-capable Candidate E2E is CA-O-182; CA-O-184 alone aggregates the complete Release Gate. These phases do not create another release Workflow.

## Details

A partial, cached, focused, stale, source-only, or unjournaled result is not proof. This Action never clears, copies, installs, publishes, or retries. Each actual Action Run is journaled once with its exact inputs and result.
