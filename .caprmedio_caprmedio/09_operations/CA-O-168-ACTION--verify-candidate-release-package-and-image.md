---
atom_id: CA-O-168
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Verify candidate release package and image"
  depends_on: [Action, Test, Methodology, Artifact/Revision, Journal]
version: 7
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-O-164, CA-O-185, CA-R-1525]
---
# Summary

Verify candidate release package and image

## Action

Verify candidate release package and image **means** the Action that performs one bound `closed_unit_gate`, `candidate_image_build`, or `candidate_image_canary` phase for the frozen local boundary.

## Scope

The `closed_unit_gate` phase binds the Version, active source identities and digests, Project Structure, settings, exact private compiled candidate, and declared Unit/source partition. It is not host Candidate E2E or the complete Release Gate. `candidate_image_build` and `candidate_image_canary` bind the exact staged package, runtime, compiled product, and `ca` payload after that Unit gate. Host-capable Candidate E2E is CA-O-182; CA-O-184 alone aggregates the complete Release Gate. These phases do not create another release Workflow.

## Details

A partial, cached, focused, stale, source-only, or unjournaled result is not proof. This Action never clears, copies, installs, publishes, or retries. Each actual Action Run is journaled once with its exact inputs and result.
